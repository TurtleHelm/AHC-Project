from .classes import Text, Btn, Window, Settings, Game
from time import sleep
import pygame as game

game.init() # Initialise Pygame
clock = game.time.Clock() # Games Clock (Frames Per Second)

width, height = (960, 720) # Window Width & Height
centerScreen = (width // 2) # The Centre of the Screen (Floor Division)

playWidth, playHeight = ((960 // 2), (720 // 4))

GUIObjects = [Text([centerScreen, (height // 12)], 'Tetris', 40)] # Title Text

settings = Settings() # Initialise Settings

# Sound Effects
rotateBlockSound = game.mixer.Sound('src/resources/sounds/rotateBlock.wav')
lineClearSound = game.mixer.Sound('src/resources/sounds/lineClear.wav')
moveBlockSound = game.mixer.Sound('src/resources/sounds/moveBlock.wav')

def drawGUI() -> None:
    '''Draws GUI Objects to the Screen'''
    
    for GUIObj in GUIObjects:

        match str(GUIObj): # Check if the object in the list is a render-able object
            case  Text.__name__: GUIObj.RenderText() # If Object in list is text, render text
            case Btn.__name__: GUIObj.RenderBtn() # If Object in list is a button, render button
            case _: pass # Defaults to this if all other cases = False

    game.display.flip()

def Leave():
    from .home import run
    game.mixer.Channel(1).stop()
    run()

def GameRun():

    Window((width, height), 'Tetris - Game', (0, 0, 0)).CreateNewWindow() # Instantiate Window Object & Create New Window

    sleep(0.1) # Wait for 0.1s until the main window loads (Used because calling the draw func does not work unless the surface is initialised)
    drawGUI() # Draw the GUI

    settings.init() # Initialise Settings with settings from settings file

    game.mixer.Channel(1).play(game.mixer.Sound('src/resources/sounds/tetris.wav'), -1) # Play music
    game.mixer.Channel(1).set_volume(.2) if settings.musicState else game.mixer.Channel(1).set_volume(0) # if music settings off, then turn off the music otherwise play the music 

    # While the game is running
    while True:

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
                    case game.K_ESCAPE: Leave()
                    case game.K_UP: game.mixer.Channel(0).play(rotateBlockSound) if settings.effectState else game.mixer.Channel(0).set_volume(0)
                    case game.K_DOWN: pass
                    case game.K_RIGHT: game.mixer.Channel(0).play(moveBlockSound) if settings.effectState else game.mixer.Channel(0).set_volume(0)
                    case game.K_LEFT: game.mixer.Channel(0).play(moveBlockSound) if settings.effectState else game.mixer.Channel(0).set_volume(0)
                    case _: pass

        game.display.update()
        clock.tick(30)