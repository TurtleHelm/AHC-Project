from src.classes import Text, Btn, Window, Settings
from .instructions import InstructionsRun
from .settings import SettingsRun
from .game import GameRun
from time import sleep
import pygame as game

game.init() # Initialise Pygame
clock = game.time.Clock() # Games Clock (Frames Per Second)
settings = Settings()

width, height = (960, 720) # Window Width & Height
centerScreen = (width // 2) # The Centre of the Screen (Floor Division)

# GUI Instantiation
Title = Text([centerScreen, (height // 8)], 'Tetris', 106) # Title Text

# List of GUI Objects
GUIObjects = [Btn('New Game', [centerScreen, (height // 2 - 50)], 230, 41, 32), # New Game Button
              Btn('Instructions', [centerScreen, (height // 2)], 300, 41, 32), # Instructions Button
              Btn('Settings', [centerScreen, (height // 2 + 50)], 200, 41, 32), # Settings Button
              Btn('Exit Game', [centerScreen, (height // 2 + 100)], 235, 41, 32)] # Exit Button

def drawGUI() -> None:
    '''Draws GUI Objects to the Screen'''

    Title.RenderText()
    
    for GUIObj in GUIObjects:

        match str(GUIObj): # Check if the object in the list is a render-able object
            case  Text.__name__: # If Object in list is text, render text
                GUIObj.RenderText()
                
            case Btn.__name__: # If Object in list is a button, render button
                GUIObj.RenderBtn()
                
            case _: pass # Defaults to this if all other cases = False

    game.display.flip()

def run():

    settings.init()

    Window((width, height), 'Tetris - Main Menu', (0, 0, 0)).CreateNewWindow() # Instantiate Window Object & Create New Window

    sleep(0.1) # Wait for 0.1s until the main window loads (Used because calling the draw func does not work unless the surface is initialised)
    drawGUI() # Draw the GUI

    # While the game is running
    while True:

        GUIObjects[0].isHovering(drawGUI, GameRun, settings.effectState) # Used to navigate to a New Game Page
        GUIObjects[1].isHovering(drawGUI, InstructionsRun, settings.effectState) # Used to navigate to the Instructions Page
        GUIObjects[2].isHovering(drawGUI, SettingsRun, settings.effectState) # Used to navigate to the settings page
        GUIObjects[3].isHovering(drawGUI, quit, settings.effectState) # Used to Exit the game

        # Check for keyboard input
        for event in game.event.get():
            
            # If exit button is clicked (top right of window), exit
            if event.type == game.QUIT:
                game.quit()
                quit(0)
            
            # if escape key pressed, exit
            if event.type == game.KEYDOWN:

                # Check for any matches in the key down events
                match event.key:

                    # If Esc key
                    case game.K_ESCAPE:
                        game.quit()
                        print('Exiting Program...')
                        quit(0)
                    
                    case _: pass

        game.display.update()
        clock.tick(30)