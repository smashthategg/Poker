import os
import re
import pandas as pd
import numpy as np

player = "smashthategg"

# Iterate through each pokernow.club csv file in game_logs
for fileName in os.listdir('./game_logs'): 
    logs = pd.read_csv('./game_logs/{}'.format(fileName))\
    
    # Put each row entry into an array
    entries = []
    for i in range(logs.shape[0]):
        entries.append(logs.loc[i, 'entry'])

        # (Reformatting) Replace all instances of "username @xxxxxxxx" with "username"
        entries[i] = re.sub(r'\s@.*?"','"',entries[i])

    entries = entries[::-1] # Reverse the order of the array (to Oldest -> Newest entry)

    # Prase hands and insert to new data frame

    
    btn_players = []
    players = []
    mystacksbb = []
    stacks = []
    bbs = []
    hands = []
    blinds = []

    my_player_index = 0
    index = 0
    stacks_index = 0
    while index < len(entries):

        btn_players.append(re.search(r'r\:\s".*?"', entries[index]).group()[4:-1])
        index += 1

        while entries[index][0] != 'P':
            index += 1

        players.append(re.findall(r'"(.*?)"', entries[index]))
        stacks.append(re.findall(r'\((.*?)\)', entries[index]))
        stacks[stacks_index] = list(map(int, stacks[stacks_index]))
        my_player_index = players[stacks_index].index(player)
        index += 1

        hands.append(entries[index][13:])
        index += 1

        if 'posts a big blind' in entries[index]:
            blinds.append(int(entries[index].split()[-1]))
        else:
            index += 1
            blinds.append(int(entries[index].split()[-1]))

        bbs.append([round(x / blinds[stacks_index], 1) for x in stacks[stacks_index]])
        mystacksbb.append(bbs[stacks_index][my_player_index])
        stacks_index += 1
        
        while index < len(entries) and entries[index][:4] != '-- s':
            index += 1

    data =  {
                'Hands': hands,
                'My Stack Size (BBs)': mystacksbb,
                'Players': players,
                'Stacks': stacks,
                'Stacks (BBs)': bbs
            }
    
    df = pd.DataFrame(data)

    print(df)