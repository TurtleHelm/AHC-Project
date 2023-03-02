# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from src.utils.ClrTerminal import Color
import pygame as game

game.init() # initialise pygame library
game.event.set_allowed([game.QUIT])
clock, settings = (game.time.Clock(), Settings()) # initialise settings & game clock

# List of GUI Objects
GUIObjects = [Text([480, 90], 'Settings', 69),
              Btn('Music: Off', [480, 260], 330, 48, 32),
              Btn('Sound Effects: Off', [480, 360], 580, 48, 32),
              Btn('Main Menu', [480, 490], 300, 48, 32)]

def ChangeMusicState() -> None:
    """Change State of Music Button"""
    
    game.mixer.Channel(1).set_volume(0) if not settings.musicState else game.mixer.Channel(1).set_volume(.2)
    GUIObjects[1].ChangeState('Music: On', True) if not settings.musicState else GUIObjects[1].ChangeState('Music: Off', False)
    settings.ChangeSettings(True) if not settings.musicState else settings.ChangeSettings(False)
    Color.prints(f'Toggled Music ({settings.musicState})')

def ChangeEffectsState():
    """Change State of Sound Effects Button"""
    
    game.mixer.Channel(0).set_volume(0) if not settings.effectState else game.mixer.Channel(0).set_volume(.3)
    GUIObjects[2].ChangeState('Sound Effects: On', True) if not settings.effectState else GUIObjects[2].ChangeState('Sound Effects: Off', False)
    settings.ChangeSettings(None, True) if not settings.effectState else settings.ChangeSettings(None, False) 
    Color.prints(f'Toggled SE ({settings.effectState})')

def OnRun():
    """Set Buttons to Default Values on Window Run"""
    
    settings.init() # Initialise Settings
    GUIObjects[1].ChangeState('Music: On', True) if settings.musicState else GUIObjects[1].ChangeState('Music: Off', False) # Change text depending on setting state (Music)
    GUIObjects[2].ChangeState('Sound Effects: On', True) if settings.effectState else GUIObjects[2].ChangeState('Sound Effects: Off', False) # Change text depending on setting state (SE)

def SettingsRun():
    """Change to Settings Window"""

    win = Window('Netris - Settings', (0, 0, 0)) # Instantiate Window Object & Create New Window
    win.CreateNewWindow()
    
    win.drawGUIObjs(GUIObjects) # Draw the GUI
    OnRun() # Get Settings & Change Button States Accordingly

    # While the game is running
    while 1:

        GUIObjects[1].isHovering(ChangeMusicState, settings.effectState)
        GUIObjects[2].isHovering(ChangeEffectsState, settings.effectState)
        GUIObjects[-1].isHovering(win.Leave, settings.effectState)
        
        game.mixer.Channel(0).set_volume(.2) if settings.effectState else game.mixer.Channel(0).set_volume(0)
        game.mixer.Channel(1).set_volume(.2) if settings.musicState else game.mixer.Channel(1).set_volume(0)
        
        # Check for keyboard input
        for event in game.event.get():
            
            # If exit button is clicked (top right of window), exit
            if event.type == game.QUIT: win.Leave() # Input Validation

        game.display.update()
        clock.tick(30)