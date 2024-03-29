# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
import pygame

pygame.init() # initialise pygame library
pygame.event.set_allowed([pygame.QUIT]) # reduces lag
clock, settings = (pygame.time.Clock(), Settings()) # initialise settings & game clock

GUIObjects = [ # List of GUI Objects
              Text([480, 40], 'Instructions', 48),
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

def InstructionsRun():
    """Change to Instructions Window"""

    win = Window('Netris - Instructions', (0, 0, 0)) # Instantiate Window Object & Create New Window
    win.CreateNewWindow()
    
    win.drawGUIObjs(GUIObjects) # Draw GUI
    settings.init() # initialise settings from file

    while 1: # While game is running

        GUIObjects[-1].isHovering(win.Leave, settings.effectState) # Used to navigate to a New Game Page

        if pygame.event.get(pygame.QUIT): win.ExitWindow() # Exit Window if Top Right X clicked

        pygame.display.update()
        clock.tick(30)