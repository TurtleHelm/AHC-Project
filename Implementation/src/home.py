# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from .instructions import InstructionsRun
from .highscores import RunHighscore
from .settings import SettingsRun
from .game import GameRun
import pygame as game

# Initialize Pygame
game.init()
game.event.set_allowed([game.QUIT, game.KEYDOWN])

# Create the games clock and settings objects
clock, settings = (game.time.Clock(), Settings())

# List of GUI Objects
GUIObjects = [
    Text([480, 90], 'Netris', 106), # Game Title
    Btn('New Game', [480, 310], 260, 41, 32), # New Game Button
    Btn('Instructions', [480, 360], 400, 41, 32), # Instructions Button
    Btn('Settings', [480, 410], 260, 41, 32), # Settings Button
    Btn('Exit Game', [480, 460], 300, 41, 32) # Exit Button
]

def run():
    # Initialize settings
    settings.init()

    # Create new window obj & set title & background color
    win = Window('Netris - Main Menu', (0, 0, 0))
    # Create the window
    win.CreateNewWindow()

    # Draw the GUI objects on the screen
    win.drawGUIObjs(GUIObjects)

    # While the game is running
    while 1:
        
        GUIObjects[1].isHovering(GameRun, settings.effectState) # Check if the new game button is clicked & navigate to the new game page
        GUIObjects[2].isHovering(InstructionsRun, settings.effectState) # Check if the instructions button is clicked & navigate to the instructions page
        GUIObjects[3].isHovering(SettingsRun, settings.effectState) # Check if the settings button is clicked & navigate to the settings page
        GUIObjects[4].isHovering(quit, settings.effectState) # Check if the exit game button is clicked & exit the game

        # Check for keyboard input
        for event in game.event.get():
            # If the exit button is clicked (top right of window), exit
            if event.type == game.QUIT:
                game.quit()
                quit(0)
            
            # If escape key is pressed, exit
            if event.type == game.KEYDOWN:
                # Check for any matches in the key down events
                match event.key:
                    # If Esc key is pressed, exit
                    case game.K_ESCAPE:
                        game.quit()
                        print('Exiting Program...')
                        quit(0)
                    # Default case
                    case _: pass

        game.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS