from src.classes import Text, Btn, Window, Settings
from time import sleep
import pygame as game

game.init()
clock = game.time.Clock()
settings = Settings()

width, height = (960, 720)
centerScreen = (width // 2)

# List of GUI Objects
GUIObjects = [Text([centerScreen, (height // 2 - 300)], 'Instructions', 69),
              Text([centerScreen, (height // 2 - 240)], 'You need to stack blocks to create a full ', 20),
              Text([centerScreen, (height // 2 - 200)], 'horizontal line, clearing them to earn points.', 20),
              Text([centerScreen, (height // 2 - 160)], 'If the blocks reach the top of the', 20),
              Text([centerScreen, (height // 2 - 120)], 'screen, you lose!', 20),
              
              Text([centerScreen, (height // 2 - 50)], 'How to Play', 32),
              Text([centerScreen, (height // 2 + 10)], '- Use the up arrow key to rotate the block ', 20),
              Text([centerScreen, (height // 2 + 50)], '90 degrees', 20),
              Text([centerScreen, (height // 2 + 90)], '- Use the left & right arrow keys to move the', 20),
              Text([centerScreen, (height // 2 + 130)], 'block', 20),
              Text([(width // 2.08), (height // 2 + 170)], '- Use the down arrow to move the block down faster', 20),
              Text([centerScreen, (height // 2 + 210)], 'Have Fun Playing!', 20),
              Btn('Main Menu', [centerScreen, (height // 2 + 260)], 300, 48, 32)]

def Leave():
    from .home import run
    run()

# GUI Instantiation
def drawGUI():

    for GUIObj in GUIObjects:

        match str(GUIObj): # Check if the object in the list is a render-able object
            case  Text.__name__: # If Object in list is text, render text
                GUIObj.RenderText()
                
            case Btn.__name__: # If Object in list is a button, render button
                GUIObj.RenderBtn()
                
            case _: pass # Defaults to this if all other cases = False

    game.display.flip()

def InstructionsRun():

    Window((width, height), 'Tetris - Instructions', (0, 0, 0)).CreateNewWindow() # Instantiate Window Object & Create New Window

    sleep(0.1) # Wait for 0.1s until the main window loads (Used because calling the draw func does not work unless the surface is initialised)
    drawGUI() # Draw the GUI
    settings.init()

    # While the game is running
    while True:

        GUIObjects[-1].isHovering(drawGUI, Leave, settings.effectState) # Used to navigate to a New Game Page

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