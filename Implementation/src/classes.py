import pygame as game

class Window:
    
    def __init__(self, window_title: str='Title', bg_color: tuple=(255, 255, 255)) -> None:
        """Initialisation for The Window Class

        Args:
            window_title (str, optional): window title. Defaults to 'Title'.
            bg_color (tuple, optional): background color. Defaults to (255, 255, 255).
        """
        
        self.screen_size = (960, 720)
        self.window_title = window_title
        self.bg_color = bg_color
        
    def CreateNewWindow(self):
        """Creates a new Window using the specified values that have been initialised"""
        self.win = game.display.set_mode(size=self.screen_size) # Set Window Size
        self.win.fill(self.bg_color) # Set Background Colour
        game.display.set_caption(self.window_title) # Set Window Title
        game.display.flip() # Used To Show Background Colour

    def ReturnWindowSurface(self): return self.win

    def ExitWindow() -> None:
        '''Exits the Game'''
        game.display.quit()
        quit(0)

    # GUI Instantiation
    def drawGUIObjs(self, GUIObjects:list=None):
        """Draw GUI Objects to the Screen

        Args:
            GUIObjects (list, optional): List of Objects. Defaults to None.
        """

        if GUIObjects == None: pass

        else:
            for GUIObj in GUIObjects:

                match str(GUIObj): # Check if the object in the list is a render-able object
                    case  Text.__name__: # If Object in list is text, render text
                        GUIObj.RenderText()
                        
                    case Btn.__name__: # If Object in list is a button, render button
                        GUIObj.RenderBtn()
                        
                    case _: pass # Defaults to this if all other cases = False
            
        game.display.flip()

    def getScreenSize(): return (960, 720)

    def __repr__(self): return __qualname__

# GUI Classes

class Text(game.sprite.Sprite):
    '''Class for Text Objects (GUI)'''

    def __init__(self, pos=[0, 0], text='Text', fontsize=20, color=(255, 255, 255)):
        """Intialises Text Object

        Args:
            pos (list, optional): Position of Text on Screen. Defaults to [0, 0].
            text (str, optional): Text to be created. Defaults to 'Text'.
            fontsize (int, optional): size of text. Defaults to 20.
            color (tuple, optional): color of text. Defaults to (255, 255, 255).
        """
        
        super().__init__() # Initialise the inherited class
        
        if not game.font.get_init: game.font.init() # Initialise Font 
        
        self.surface = game.display.get_surface() # Get Window Surface
        self.givenPos = pos # Given Position of Text
        
        self.color = color # Color of Text
        
        self.fontsize = fontsize
        self.text = game.font.Font('Implementation/src/resources/fonts/font.ttf', self.fontsize).render(text, False, self.color) # Creates Font
        
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # Set Position of Text
        self.caption = text # Raw text

    def RenderText(self) -> None:
        game.display.get_surface().blit(self.text, self.pos) # draw text
        game.display.flip() # update screen
    
    def ChangeText(self, text, draw=None) -> None:
        self.caption = text
        self.text = game.font.Font('Implementation/src/resources/fonts/font.ttf', self.fontsize).render(self.caption, False, self.color) # Sets new Text
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)]
        draw() if draw is not None else self.RenderText()

    def ChangeColor(self, color) -> None:
        self.color = color # update color
        self.text = game.font.Font('Implementation/src/resources/fonts/font.ttf', self.fontsize).render(self.caption, False, color) # update text
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # update position
        self.RenderText() # Rerender text

    def __str__(self): return 'Text' # Returns only when str() function called
    def __name__(self): return 'Text' # Returns name of class (Text)
    def ReturnText(self): return self.caption # Returns Text Content Of Instance of the class

class Btn(game.sprite.Sprite):
    '''Class for Button Objects (GUI)'''
    
    def __init__(self, text, pos=[0, 0], width=113, height=41, fontsize=16):
        """Initialise Btn object

        Args:
            text (Text): Text Object
            pos (list, optional): Position of Button. Defaults to [0, 0].
            width (int, optional): Width of Button. Defaults to 113.
            height (int, optional): Height of Button. Defaults to 41.
            fontsize (int, optional): Size of Text. Defaults to 16.
        """
        
        super().__init__()
        
        self.pos = pos # Get Center Pos of Btn
        self.surf = game.display.get_surface() # Get Window Surface
        self.face = game.Rect(self.pos, (width, height)) # Create Rect
        self.face.center = self.pos # position size
        self.hovering = False # Checks if button is being hovered
        self.fontsize = fontsize # text size
        self.textColor = (255, 255, 255) # Color of the text
        self.text = Text(self.pos, text, self.fontsize, self.textColor) # text object
        self.caption = text # raw text
        self.state = False # has been clicked or not
        self.hoverSound = 'Implementation/src/resources/sounds/hoverSound.wav' # sound for hovering
        self.selectSound = 'Implementation/src/resources/sounds/selectSound.wav' # sound for selecting (clicking)

    def ChangeState(self, txt:str, bool:bool) -> None:
        self.state = bool # Change Clicked State
        self.text.ChangeText(txt, self.DrawBtn) # Change color of text depending on state

    def isHovering(self, click, effectState) -> None:
        """Checks to See if the mouse is hovering over a button

        Args:
            click (function/procedure): click function
            effectState (bool): sound effect state
        """
        
        # If mouse is hovering
        if self.face.collidepoint(game.mouse.get_pos()):
            
            # If the button is not already being hovered
            if not self.hovering:
                self.hovering = True # Sets button being hovered to true
                self.text.ChangeColor((255, 0, 0)) # Change Text Color
                
                # Sound Effect Volume
                game.mixer.Channel(0).set_volume(.3) if effectState else game.mixer.Channel(0).set_volume(0)
                game.mixer.Channel(0).play(game.mixer.Sound(self.hoverSound)) if effectState else game.mixer.Channel(0).set_volume(0)
                
                self.DrawBtn() # Redraw Button

            # If the button is already being hovered
            else: self.HasClicked(click) # Check if the button has been clicked
            
        # If mouse is not over the button but the button is still being hovered    
        elif not self.face.collidepoint(game.mouse.get_pos()) and self.hovering:
            self.hovering = False # Make sure when not hovered hover is set to false
            self.text.ChangeColor((255, 255, 255)) # Changes button color to white
            self.DrawBtn() # Redraw Button

    def HasClicked(self, click) -> None:
        """Check if a button has been clicked"""
        
        if game.mouse.get_pressed()[0]: # If button has been pressed with left click
            game.mixer.Channel(0).play(game.mixer.Sound(self.selectSound)) # Play select sound
            click() # Run Click Method
            
            from time import sleep
            sleep(.2) # Stop multiple clicks being registered
    
    def RenderBtn(self) -> None:
        game.draw.rect(game.display.get_surface(), (0, 0, 0), self.face) # Render button rectangle
        self.text.RenderText() # Render button text
    
    def DrawBtn(self) -> None:
        self.RenderBtn() # Render button
        game.display.flip() # Update display
    
    def __str__(self): return 'Btn' # Returns only when str() function called
    def __name__(self): return 'Btn' # Returns name of class (Button)

# Game Class
class Game: 
        
    class Block(game.sprite.Sprite):
        '''Class for Blocks'''
          
        @staticmethod
        def GetRandBlock(): 
            from random import choice
            return choice((Game.LBlock, Game.SquareBlock, Game.TBlock, Game.SBlock, Game.ZBlock, Game.LineBlock))() # Returns Random Block

        def __init__(self, struct, color): # Initialise Values
            super().__init__()
            self.struct = struct
            self.color = color
            self.realPos = [450, 100]
            self.blockSize = 30
            self.group = game.sprite.Group()
            self.image = game.surface.Surface([30, 30])

        def draw(self, screen):
            '''Draws a block to the screen at the appropriate coordinates'''
            posX, posY = self.realPos
            
            for y in range(len(self.struct)): # vertical
                for x in range(len(self.struct[y])): # horizontal
                    if y > 0 and x == 0: # if reached end of row in 2d array
                        posY += 30 # move down 1 block
                        posX -= (30*3) # move left 3 blocks

                    if self.struct[y][x] == 1: # if block is to be drawn
                        self.group.add(Game.Rectangle((posX, posY), self.color, self.blockSize)) # draw block with appropriate attributes
                        posX += 30 # move over right a block space

                    else: posX += 30 # if no block to draw, move over a block space
                    
            self.group.draw(screen) # draw all rectangle sprites to the screen at once

        def Move(self, screen, dir, dirName):
            self.UpdateColor((0, 0, 0), screen) # Update color of previous blocks
            self.group.empty() # empty sprite group
            self.group.update(dir) # draw new block at new location (gives impression of movement)
            
            match dirName: # check for direction of travel
                case 'left': self.realPos[0] -= 30
                case 'right': self.realPos[0] += 30
                case 'down': self.realPos[1] += 30
                
            Game.Block.draw(self, screen) # draw new block to screen

        def CheckCollision(self, blockGroup):
            for i in range(len(blockGroup.sprites())):
                if self == blockGroup.sprites()[i]: continue
                else: 
                    for j in range(len(self.group.sprites())):
                        collide = game.sprite.spritecollideany(self.group.sprites()[j], blockGroup.sprites()[i].group) # still causes issues with collision but it doesn't crash now
                        if collide is not None: return True
            
            for i in range(len(self.group.sprites())): 
                if self.group.sprites()[i].posY == 670: return True

            return False

        def CheckMovable(self, dir):
            if dir == 'right':
                for i in range(len(self.group.sprites())):
                    if self.group.sprites()[i].posX == 600: return False
                return True
            
            if dir == 'left':
                for i in range(len(self.group.sprites())):
                    if self.group.sprites()[i].posX == 360: return False
                return True
                    
        def UpdateColor(self, color, screen): # Temp fix for screen flashing
            originalColor = self.color # store original color
            self.color = color # set new color
            self.draw(screen) # draw new colored block to screen
            self.color = originalColor # set color back to original color

        def Rotate(self, screen, effectState, sound):
            if not isinstance(self, Game.SquareBlock): # check if the block is not square, if its not square continue
                if self.CheckMovable('right') and self.CheckMovable('left'): # temp fix for bugging through grid walls
                    if effectState: game.mixer.Channel(0).play(sound)
                    self.UpdateColor((0, 0, 0), screen) # update color of previous block
                    
                    from numpy import rot90
                    self.struct = rot90(self.struct) # rotate array 90 degrees clockwise
                    self.draw(screen) # redraw new block positions

        @staticmethod
        def reachedTop(blockGroup):
            for sprite in blockGroup:
                for block in sprite.group:
                    if block.posY == 130: return True
            return False

    class Rectangle(game.sprite.Sprite):
        def __init__(self, pos, color, size): # intialise values
            super().__init__() # get values from inherited class
            self.posX, self.posY = pos # set position
            self.size = size # set size of each rect
            self.color = color # set color of each rect
            self.rect = game.Rect(self.posX, self.posY, self.size, self.size) # create rect
            self.image = game.Surface([self.size, self.size]) # create surface of rect
            self.image.fill(self.color) # fill rect with appropriate color
            
        def update(self, dir): self.rect.move_ip(dir) # update position of rect     
        def hasCollided(self, sprite): return self.rect.colliderect(sprite.rect) # return if rect has been collided with

    class LBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (1, 0, 0), (1, 1, 1)), (255, 165, 0)) # initialise values for class

    class SquareBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (1, 1, 0), (1, 1, 0)), (255, 255, 0)) # initialise values for class

    class TBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (0, 1, 0), (1, 1, 1)), (128, 0, 128)) # initialise values for class
    
    class SBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (0, 1, 1), (1, 1, 0)), (0, 128, 0)) # initialise values for class
    
    class ZBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (1, 1, 0), (0, 1, 1)), (128, 0, 0)) # initialise values for class
    
    class LineBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0)), (0, 255, 255)) # initialise values for class

class GridRect(game.sprite.Sprite):
    def __init__(self, pos, size): # initialise values
            super().__init__() # initialise default values from inherited class
            self.posX, self.posY = pos # set position
            self.size = size # set block size 
            self.color = (200, 200, 200) # set grid line color
            self.rect = game.Rect(self.posX, self.posY, self.size, self.size) # create grid rect
            self.image = game.Surface([self.size, self.size]) # create grid rect surface

    def drawRect(self, screen):
        game.draw.rect(screen, self.color, self.rect, 1) # draw grid rect with appropriate values

class Grid(Game):
    def __init__(self, gridSize): # initialise values 
        super().__init__() # initialise values from inherited class
        self.sizeX = gridSize[0] # grid horizontal size
        self.sizeY = gridSize[1] # grid vertical size
        self.blockSize = 30 # grid block size
        self.gridX = 630 # grid x size
        self.gridY = 700 # grid y size
        self.gridGroup = game.sprite.Group() # grid block sprite group
        # self.fakeGrid = [[0 for x in range(9)] for y in range(20)]

    def DrawGrid(self, screen):
        for x in range(self.sizeX, self.gridX, self.blockSize): # for horizontal grid blocks, starting & ending at limits with each step being of size blockSize
            for y in range(self.sizeY, self.gridY, self.blockSize): # for vertical grid blocks, starting & ending at limits with each step being of size blockSize
                gridBlock = GridRect((x, y), self.blockSize) # create a GridRect instance with appropriate values
                self.gridGroup.add(gridBlock) # add the new GridRect object to the grid sprite group
                gridBlock.drawRect(screen) # draw new gridRect object to the screen

class Settings():
    '''Class for Game Settings'''
    
    def __init__(self, musicState:bool=True, effectState:bool=True):
        self.musicState = musicState # initialise musicState
        self.effectState = effectState # initialise effectState

    def init(self) -> None:
        '''Gets Settings From File'''
        
        from os import path
        if not path.isfile('settings.txt'): self.WriteSettings(False) # If there is no settings file, Make one

        else: # Otherwise
            with open('settings.txt') as f: # Open the file
                settings = f.read().split(',') # Split values by comma
                f.close() # Close File

            self.musicState = True if settings[0] == 'True' else False # Set the music state to true if the settings value is true
            self.effectState = True if settings[1] == 'True' else False # Set the sound effects state to true if the settings value is true            

    def WriteSettings(self, rem) -> None:
        
        from os import remove
        if rem: remove('settings.txt') # if we set rem to True, remove settings file
            
        with open('settings.txt', 'w') as f: # open settings file as write
            f.write(f'{str(self.musicState)},') # write new musicState value to file
            f.write(f'{str(self.effectState)}') # write new effectState value to file
            f.close() # close file
            
        self.init() # reinitialise settings

    def ChangeSettings(self, musicBool=None, effectsBool=None) -> None:
        self.musicState = musicBool if musicBool != None else self.musicState # set musicState to musicBool if musicBool has a value otherwise just set it back to musicState
        self.effectState = effectsBool if effectsBool != None else self.effectState # set effectState to effectBool if effectBool has a value otherwise just set it back to effectSte
        self.WriteSettings(True) # Write new changes to settings file