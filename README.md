# Pokernow.club logs parser: How to Use

This guide assumes very basic knowledge of directories, programming in IDEs, and Python

1. Create a folder that will be your workspace in your IDE. Name it your choice.
2. Download reader.py and put it into the folder
3. In that folder, also create a new folder called "game_logs"
4. "game_logs" is where you download the full logs (should be csv files) from a pokernow game. **NOTE: the reader will not work if any log contains hands where the specified player is not involved.**
5. In your IDE, edit line 6 of reader.py to contain the correct pokernow username (the current one is my username, smashthategg)
6. Run reader.py (you may need to run "pip install pandas" in the terminal)
7. Should be all set!
