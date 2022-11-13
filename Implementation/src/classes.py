from os import path, remove
from random import choice
from time import sleep
import pygame as game

class Window:
    '''Main Window Class'''
    
    def __init__(self, screen_size: tuple=(500, 500), window_title: str='Title', bg_color: tuple=(255, 255, 255)) -> None:
        '''Initialisation for The Window Class'''
        self.screen_size = screen_size
        self.window_title = window_title
        self.bg_color = bg_color
        
    def CreateNewWindow(self):
        '''Creates a new Window using the specified values that have been initialised'''
        self.win = game.display.set_mode(size=self.screen_size) # Set Window Size 
        self.win.fill(self.bg_color) # Set Background Colour
        game.display.set_caption(self.window_title) # Set Window Title
        game.display.flip() # Used To Show Background Colour

    def ReturnWindowSurface(self): return self.win

    def ExitWindow(self) -> None:
        '''Exits the Game'''
        game.display.quit()
        quit(0)

    def __repr__(self): return __qualname__

# GUI Classes

class Text(game.sprite.Sprite):
    '''Class for Text Objects (GUI)'''

    def __init__(self, pos=[0, 0], text='Text', fontsize=20, color=(255, 255, 255)):
        super().__init__() # Initialise the inherited class
        
        if not game.font.get_init: game.font.init() # Initialise Font 
        self.surface = game.display.get_surface() # Get Window Surface
        self.givenPos = (pos[0], pos[1]) # Given Position of Text
        self.color = color # Color of Text
        self.fontsize = fontsize
        self.text = game.font.Font('src/resources/fonts/font.ttf', self.fontsize).render(text, False, self.color) # Creates Font
        self.pos = [pos[0] - (self.text.get_width() // 2), pos[1] - (self.text.get_height() // 2)] # Set Position of Text
        self.caption = text

    def RenderText(self) -> None:
        game.display.flip()
        game.display.get_surface().blit(self.text, self.pos)
    
    def ChangeText(self, text, draw) -> None:
        self.caption = text
        self.text = game.font.Font('src/resources/fonts/font.ttf', self.fontsize).render(self.caption, False, self.color) # Sets new Text
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)]
        draw()

    def ChangeColor(self, color) -> None:
        self.color = color
        self.text = game.font.Font('src/resources/fonts/font.ttf', self.fontsize).render(self.caption, False, color)
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)]
        self.RenderText()

    def __str__(self): return 'Text' # Returns only when str() function called
    def __name__(self): return 'Text' # Returns name of class (Text)
    def ReturnText(self): return self.caption # Returns Text Content Of Instance of the class

class Btn(game.sprite.Sprite):
    '''Class for Button Objects (GUI)'''
    
    def __init__(self, text, pos=[0, 0], width=113, height=41, fontsize=16):
        super().__init__()
        
        self.pos = pos # Get Center Pos of Btn
        self.surf = game.display.get_surface() # Get Window Surface
        self.face = game.Rect(self.pos, (width, height)) # Create Rect
        self.face.center = self.pos
        self.hovering = False # Checks if button is being hovered
        self.fontsize = fontsize
        self.textColor = (255, 255, 255)
        self.text = Text(self.pos, text, self.fontsize, self.textColor)
        self.caption = text
        self.state = False
        self.hoverSound = 'src/resources/sounds/hoverSound.wav'
        self.selectSound = 'src/resources/sounds/selectSound.wav'

    def ChangeState(self, txt:str, bool:bool, draw) -> None:
        self.state = bool
        self.text.ChangeText(txt, draw)

    def isHovering(self, draw, click, effectState) -> None:
        ''' Procedure: Checks to See if the mouse is hovering over a button '''
        
        if self.face.collidepoint(game.mouse.get_pos()): # If mouse is hovering
            if not self.hovering: # If the button is not already being hovered
                self.hovering = True # Sets button being hovered to true
                self.text.ChangeColor((255, 0, 0))
                game.mixer.Channel(0).set_volume(.3) if effectState else game.mixer.Channel(0).set_volume(0)
                game.mixer.Channel(0).play(game.mixer.Sound(self.hoverSound)) if effectState else game.mixer.Channel(0).set_volume(0)
                draw()

            else: # If the button is already being hovered
                self.HasClicked(click) # Check if the button has been clicked
            
        # If mouse is not over the button but the button is still being hovered    
        elif not self.face.collidepoint(game.mouse.get_pos()) and self.hovering:
            self.hovering = False
            self.text.ChangeColor((255, 255, 255))
            draw()

    def HasClicked(self, click) -> None:
        '''Procedure: Check if a button has been clicked'''
        if game.mouse.get_pressed()[0]:
            game.mixer.Channel(0).play(game.mixer.Sound(self.selectSound))
            click() # Run Click Method
            sleep(.1) # Stop multiple clicks being registered
    
    def RenderBtn(self):
        game.draw.rect(game.display.get_surface(), (0, 0, 0), self.face)
        self.text.RenderText()
    
    def __str__(self): return 'Btn' # Returns only when str() function called
    def __name__(self): return 'Btn' # Returns name of class (Button)

# Game Class
class Game: pass

# Misc

class Settings():
    '''Class for Game Settings'''
    def __init__(self, musicState:bool=True, effectState:bool=True):
        self.musicState = musicState
        self.effectState = effectState

    def init(self) -> None:
        '''Gets Settings From File'''
        
        if not path.isfile('settings.txt'): self.WriteSettings(False) # If there is no settings file, Make one

        else: # Otherwise
            with open('settings.txt') as f: # Open the file
                settings = f.read().split(',') # Split values by comma
                f.close() # Close File

            self.musicState = True if settings[0] == 'True' else False # Set the music state to true if the settings value is true
            self.effectState = True if settings[1] == 'True' else False # Set the sound effects state to true if the settings value is true            

    def WriteSettings(self, rem) -> None:
        if rem: remove('settings.txt')
            
            
        with open('settings.txt', 'w') as f:
            f.write(f'{str(self.musicState)},')
            f.write(f'{str(self.effectState)}')
            f.close()
        self.init()

    def ChangeSettings(self, musicBool=None, effectsBool=None) -> None:
        self.musicState = musicBool if musicBool != None else self.musicState
        self.effectState = effectsBool if effectsBool != None else self.effectState
        self.WriteSettings(True)

    def ReturnStates(self):
        return f'Music: {self.musicState}nEffects: {self.effectState}'
