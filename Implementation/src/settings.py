from src.classes import Text, Btn, Window, Settings
from time import sleep
import pygame as game

game.init()
clock = game.time.Clock()

width, height = (960, 720)
centerScreen = (width // 2)

# GUI Instantiation
Title = Text([centerScreen, (height // 8)], 'Settings', 69)

# List of GUI Objects
GUIObjects = [Text([centerScreen, (height // 8)], 'Settings', 69),
              Btn('Music: Off', [centerScreen, (height // 2 - 100)], 330, 48, 32),
              Btn('Sound Effects: Off', [centerScreen, (height // 2)], 580, 48, 32),
              Btn('Main Menu', [centerScreen, (height // 2 + 100)], 225, 48, 32)]

settings = Settings()

def Leave():
    from .home import run
    run()

def ChangeMusicState():
    game.mixer.Channel(1).set_volume(0) if not settings.musicState else game.mixer.Channel(1).set_volume(.2)
    GUIObjects[1].ChangeState('Music: On', True, drawGUI) if not settings.musicState else GUIObjects[1].ChangeState('Music: Off', False, drawGUI)
    settings.ChangeSettings(True) if not settings.musicState else settings.ChangeSettings(False)

def ChangeEffectsState():
    game.mixer.Channel(0).set_volume(0) if not settings.effectState else game.mixer.Channel(0).set_volume(.3)
    GUIObjects[2].ChangeState('Sound Effects: On', True, drawGUI) if not settings.effectState else GUIObjects[2].ChangeState('Sound Effects: Off', False, drawGUI)
    settings.ChangeSettings(None, True) if not settings.effectState else settings.ChangeSettings(None, False)

def OnRun():
    settings.init()
    GUIObjects[1].ChangeState('Music: On', True, drawGUI) if settings.musicState else GUIObjects[1].ChangeState('Music: Off', False, drawGUI)
    GUIObjects[2].ChangeState('Sound Effects: On', True, drawGUI) if settings.effectState else GUIObjects[2].ChangeState('Sound Effects: Off', False, drawGUI)

def drawGUI():
    
    for GUIObj in GUIObjects:

        match str(GUIObj): # Check if the object in the list is a render-able object
            case  Text.__name__: # If Object in list is text, render text
                GUIObj.RenderText()
                
            case Btn.__name__: # If Object in list is a button, render button
                GUIObj.RenderBtn()
                
            case _: pass # Defaults to this if all other cases = False
    
    game.display.flip()

def SettingsRun():

    Window((width, height), 'Tetris - Settings', (0, 0, 0)).CreateNewWindow() # Instantiate Window Object & Create New Window

    sleep(0.1) # Wait for 0.1s until the main window loads (Used because calling the draw func does not work unless the surface is initialised)
    
    drawGUI() # Draw the GUI
    OnRun() # Get Settings & Change Button States Accordingly

    # While the game is running
    while True:

        GUIObjects[1].isHovering(drawGUI, ChangeMusicState, settings.effectState)
        GUIObjects[2].isHovering(drawGUI, ChangeEffectsState, settings.effectState)
        GUIObjects[-1].isHovering(drawGUI, Leave, settings.effectState)
        
        game.mixer.Channel(0).set_volume(.2) if settings.effectState else game.mixer.Channel(0).set_volume(0)
        game.mixer.Channel(1).set_volume(.2) if settings.musicState else game.mixer.Channel(1).set_volume(0)
        
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