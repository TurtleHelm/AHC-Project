from src.utils.ClrTerminal import Color
from src.home import run

# If this file is the main file, run the startup code
if __name__ == '__main__':

    Color.ClrPrint('orange', 'Loading Tetris...')
    run() # Run Game Using Main Window Surface for GUI Drawing