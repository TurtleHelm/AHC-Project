# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from src.instructions import InstructionsRun
from src.settings import SettingsRun
from src.game import GameRun
from src.dev import DevRun
import pygame

pygame.init() # Initialize Pygame
pygame.event.set_allowed([pygame.QUIT]) # limit event checks
clock, settings = (pygame.time.Clock(), Settings()) # Create the games clock and settings objects

GUIObjects = [ # List of GUI Objects
    Text([480, 90], 'Netris', 106), # Game Title
    Btn('New Game', [480, 310], 260, 41, 32), # New Game Button
    Btn('Instructions', [480, 360], 400, 41, 32), # Instructions Button
    Btn('Settings', [480, 410], 260, 41, 32), # Settings Button
    Btn('Developer Mode', [480, 650], 210, 41, 16),
    Btn('Exit Game', [480, 460], 300, 41, 32) # Exit Button
]

def run(): # run procedure for this page
    """Change to Home Window"""
    
    settings.init() # Initialize settings

    # Create new window obj & set title & background color
    win = Window('Netris - Main Menu', (0, 0, 0))
    win.CreateNewWindow() # Create the window
    win.drawGUIObjs(GUIObjects) # Draw the GUI objects on the screen

    # While the game is running
    while 1: 
        
        GUIObjects[1].isHovering(GameRun, settings.effectState) # Check if the new pygame button is clicked & navigate to the new pygame page
        GUIObjects[2].isHovering(InstructionsRun, settings.effectState) # Check if the instructions button is clicked & navigate to the instructions page
        GUIObjects[3].isHovering(SettingsRun, settings.effectState) # Check if the settings button is clicked & navigate to the settings page
        GUIObjects[4].isHovering(DevRun, settings.effectState)
        GUIObjects[-1].isHovering(win.ExitWindow, settings.effectState) # Check if the exit pygame button is clicked & exit the pygame

        for event in pygame.event.get(): # Check for keyboard input
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT: win.ExitWindow() # If escape key is pressed, exit

        pygame.display.update() # Update the display
        clock.tick(30) # Set the pygame's frame rate to 30 FPS