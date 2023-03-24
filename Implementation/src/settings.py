# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from src.utils.ClrTerminal import Color
import pygame

pygame.init() # initialise pygame library
pygame.event.set_allowed([pygame.QUIT]) # limits event checks, reduces lag
clock, settings = (pygame.time.Clock(), Settings()) # initialise settings & game clock

GUIObjects = [ # List of GUI Objects
              Text([480, 90], 'Settings', 69), # Title
              Btn('Music: Off', [480, 260], 330, 48, 32), # Music State Button
              Btn('Sound Effects: Off', [480, 360], 580, 48, 32), # Sound Effect State Button
              Btn('Main Menu', [480, 520], 300, 48, 32) # Main Menu Button
            ] 

def ChangeMusicState() -> None:
    """Change State of Music Button"""
    
    GUIObjects[1].ChangeState('Music: On', True) if not settings.musicState else GUIObjects[1].ChangeState('Music: Off', False) # Change Text on Music Btn depending on curr settings
    settings.ChangeSettings(True) if not settings.musicState else settings.ChangeSettings(False) # Change Music State depending on current settings
    Color.prints(f'Toggled Music ({settings.musicState})') # Print New State

def ChangeEffectsState() -> None:
    """Change State of Sound Effects Button"""
    
    GUIObjects[2].ChangeState('Sound Effects: On', True) if not settings.effectState else GUIObjects[2].ChangeState('Sound Effects: Off', False) # Change Text on SE Btn depending on curr settings
    settings.ChangeSettings(None, True) if not settings.effectState else settings.ChangeSettings(None, False) # Change SE State depending on current settings
    Color.prints(f'Toggled SE ({settings.effectState})') # Print New State

def OnRun() -> None:
    """Set Buttons to Default Values on Window Run"""
    
    settings.init() # Initialise Settings
    GUIObjects[1].ChangeState('Music: On', True) if settings.musicState else GUIObjects[1].ChangeState('Music: Off', False) # Change text depending on setting state (Music)
    GUIObjects[2].ChangeState('Sound Effects: On', True) if settings.effectState else GUIObjects[2].ChangeState('Sound Effects: Off', False) # Change text depending on setting state (SE)

def SettingsRun():
    """Change to Settings Window"""

    win = Window('Netris - Settings', (0, 0, 0)) # Instantiate Window Object
    win.CreateNewWindow() # Create new Window
    win.drawGUIObjs(GUIObjects) # Draw the GUI
    
    OnRun() # Get Settings & Change Button States Accordingly

    while 1: # Game loop

        GUIObjects[1].isHovering(ChangeMusicState, settings.effectState) # Check for Hover Events
        GUIObjects[2].isHovering(ChangeEffectsState, settings.effectState) # Check for Hover Events
        GUIObjects[-1].isHovering(win.Leave, settings.effectState) # Check for Hover Events
        
        pygame.mixer.Channel(0).set_volume(.2) if settings.effectState else pygame.mixer.Channel(0).set_volume(0) # Change Volume of SE on this page
        
        if pygame.event.get(pygame.QUIT): win.ExitWindow() # Exit Window if Exit event occurs

        pygame.display.update() # Update Display
        clock.tick(30) # Limit page to 30 FPS