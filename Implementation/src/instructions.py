from src.classes import Text, Btn, Window, Settings
import pygame as game

game.init() # initialise pygame library
game.event.set_allowed([game.QUIT, game.KEYDOWN]) # reduces lag
clock, settings = (game.time.Clock(), Settings()) # initialise settings & game clock

# List of GUI Objects
GUIObjects = [Text([480, 40], 'Instructions', 48),
              Text([480, 100], 'Stack blocks to create a full horizontal line', 20),
              Text([320, 140], 'clearing them to earn points', 20),
              Text([447, 220], 'If the blocks reach the top of the screen,', 20),
              Text([119, 260], 'you lose!', 20),
              
              Text([480, 320], 'How to Play', 32),
              Text([381, 380], '- Use the ↑ key to rotate the block', 20),
              Text([410, 430], '- Use the ← & → keys to move the block', 20),
              Text([480, 470], '- Use the ↓ key to move the block down faster', 20),
              Text([480, 535], 'Have Fun Playing!', 20),
              Btn('Main Menu', [480, 620], 300, 48, 32)]

def Leave():
    from .home import run
    run()

def InstructionsRun():

    win = Window('Netris - Instructions', (0, 0, 0)) # Instantiate Window Object & Create New Window
    win.CreateNewWindow()
    
    win.drawGUIObjs(GUIObjects) # Draw GUI
    settings.init()

    # While game is running
    while 1:

        GUIObjects[-1].isHovering(Leave, settings.effectState) # Used to navigate to a New Game Page

        # Check keyboard input
        for event in game.event.get():
            
            # If exit button clicked (top right of window), exit
            if event.type == game.QUIT:
                game.quit()
                quit(0)
            
            # if escape key pressed, exit
            if event.type == game.KEYDOWN:
                
                # Check for any matches in key down events
                match event.key:

                    # If Esc key
                    case game.K_ESCAPE:
                        game.quit()
                        print('Exiting Program...')
                        quit(0)
                    
                    case _: pass

        game.display.update()
        clock.tick(30)