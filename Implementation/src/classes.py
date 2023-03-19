# Import main libraries
from pathlib import Path
import pygame

class Window:
    '''Window Class'''
    
    def __init__(self, window_title:str='Title', bg_color:tuple=(255, 255, 255)) -> None:
        '''Initialise Window Class

        Args:
        - window_title (str, optional): window title. Defaults to 'Title'.
        - bg_color (tuple, optional): background color. Defaults to (255, 255, 255).
        '''
        
        self.screen_size = (960, 720)
        self.window_title = window_title
        self.bg_color = bg_color
        self.icon = pygame.image.load(f'{str(Path(__file__).parents[0])}\\resources\\images\\icon.png')
        
    def CreateNewWindow(self) -> None:
        '''Creates new Window using appropriate values'''
        
        self.win = pygame.display.set_mode(size=self.screen_size)
        self.win.fill(self.bg_color)
        pygame.display.set_caption(self.window_title)
        pygame.display.set_icon(self.icon)
        pygame.display.flip()

    @staticmethod
    def ExitWindow():
        '''Exits the Game'''
        
        from src.utils.ClrTerminal import Color
        pygame.display.quit()
        Color.printd('Exiting Window...')
        pygame.quit()
        quit(0)

    def drawGUIObjs(self, GUIObjects:list=None) -> None:
        '''Draw GUI Objects to the Screen

        Args:
        - GUIObjects (list): List of Objects. Defaults to None.
        '''

        if GUIObjects == None: pass # if no GUI Objects, stop

        else:
            for GUIObj in GUIObjects: # for each gui object in the list

                match GUIObj.__name__(): # Check if the object in the list is a render-able object
                    case  Text.__name__: # If Object in list is text, render text
                        GUIObj.RenderText()
                        
                    case Btn.__name__: # If Object in list is a button, render button
                        GUIObj.RenderBtn()
                        
                    case _: pass # Defaults to this if all other cases = False
            
        pygame.display.flip()

    @staticmethod
    def Leave() -> None:
        '''Navigate Back to the Home Page'''
        from .home import run
        run()

class Text(pygame.sprite.Sprite):
    '''Text Class (GUI)'''

    def __init__(self, pos:list=[0, 0], text:str='Text', fontsize:int=20, color:tuple=(255, 255, 255)):
        '''Intialises Text Object

        Args:
        - text (str, optional): Text to be created. Defaults to 'Text'.
        - pos (list, optional): Position of Text on Screen. Defaults to [0, 0].
        - fontsize (int, optional): size of text. Defaults to 20.
        - color (tuple, optional): color of text. Defaults to (255, 255, 255).
        
        Instance Variables:
        - surface (pygame.Surface): Surface to be drawn to
        - givenPos (list): Position of Text on Screen before transformations
        - caption (str): String to be displayed
        '''
        
        super().__init__() # Initialise the inherited class
        if not pygame.font.get_init: pygame.font.init() # Initialise Font 
        
        self.surface = pygame.display.get_surface() # Get Window Surface
        self.givenPos = pos
        
        self.color = color
        
        self.fontsize = fontsize
        self.text = pygame.font.Font(f'{str(Path(__file__).parents[0])}\\resources\\fonts\\font.ttf', self.fontsize).render(text, False, self.color) # Creates Font Object
        
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # Set Position of Text
        self.caption = text

    def RenderText(self) -> None:
        '''Render Text to Screen'''
        pygame.display.get_surface().blit(self.text, self.pos) # Render Text to current Surface
        pygame.display.flip() # Update Screen
    
    def ChangeText(self, text:str='', draw=None) -> None:
        '''Change Currently Displayed Text

        Args:
        - text (str): Text to be drawn
        - draw (method, optional): Draw method. Defaults to None.
        '''
        
        self.caption = text # Change Caption Contents
        self.text = pygame.font.Font(f'{str(Path(__file__).parents[0])}\\resources\\fonts\\font.ttf', self.fontsize).render(self.caption, False, self.color) # Sets new Text
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # Set Position Again
        draw() if draw is not None else self.RenderText() # Draw only if the draw procedure exists, otherwise use default draw procedure

    def ChangeColor(self, color:tuple=(255, 255, 255)) -> None:
        '''Change Color of Currently Displayed Text

        Args:
        - color (tuple): Color to be drawn. Defaults to (255, 255, 255)
        '''
        
        self.color = color
        self.text = pygame.font.Font(f'{str(Path(__file__).parents[0])}\\resources\\fonts\\font.ttf', self.fontsize).render(self.caption, False, color) # update text
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # update position
        self.RenderText() # Rerender text

    def UpdateText(self, color:tuple=(255, 255, 255), text:str='') -> None:
        '''Update the Text on the screen
        
        Args:
        - color (tuple, optional): Color to Shift to whilst changing text, Defaults to (255, 255, 255)
        - text (string, optional): Text to Shift to,  Defaults to ''
        '''
        
        self.ChangeColor(color) # change color to another color
        self.ChangeText(text) # Change Text Contents
        self.ChangeColor((255, 255, 255)) # change color back to white
    
    @staticmethod
    def __name__(): return 'Text'
    def ReturnText(self): return self.caption # Returns Text Content Of Instance of the class

class Btn(pygame.sprite.Sprite):
    '''Btn Class (GUI)'''
    
    def __init__(self, text:str='', pos:list=[0, 0], width:int=113, height:int=41, fontsize:int=16):
        '''Initialise Btn object

        Args:
        - caption (str): Text to be drawn to screen
        - pos (list, optional): Position of Button. Defaults to [0, 0].
        - width (int, optional): Width of Button. Defaults to 112.
        - height (int, optional): Height of Button. Defaults to 40.
        - fontsize (int, optional): Size of Text. Defaults to 16.
            
        Instance Variables
        - surf (pygame.Surface): Surface to draw to
        - face (pygame.Rect): Button rectangle
        - hovering (bool): If cursor hovering over button
        - textColor (tuple): Button text color
        - text (Text): Text Object
        - state (bool): If button has been clicked
        - hoverSound (filePath): hover sound file
        - selectSound (filePath): select sound file
        '''
        
        super().__init__() # initialises default values from inherited class
        
        self.pos = pos
        self.surf = pygame.display.get_surface()
        self.face = pygame.Rect(self.pos, (width, height))
        self.face.center = self.pos
        self.hovering = False
        self.fontsize = fontsize
        self.textColor = (255, 255, 255)
        self.text = Text(self.pos, text, self.fontsize, self.textColor)
        self.caption = text
        self.state = False
        self.hoverSound = f'{str(Path(__file__).parents[0])}\\resources\\sounds\\hoverSound.wav'
        self.selectSound = f'{str(Path(__file__).parents[0])}\\resources\\sounds\\selectSound.wav'

    def ChangeState(self, txt:str, state:bool) -> None:
        '''Changes State of Button

        Args:
        - txt (str): Text to be drawn to screen
        - bool (bool): has button changed state
        '''
        
        self.state = state # Change Clicked State
        self.text.ChangeText(txt, self.RenderBtn) # Change color of text depending on state

    def isHovering(self, click, effectState:bool, color:tuple=(255, 0, 0), *args) -> None:
        '''Checks to See if the mouse is hovering over a button

        Args:
        - click (method): click function
        - effectState (bool): sound effect state
        - color (tuple): Color to set text to on hover
        - *args: Any other values to be passed into the click method
        '''
        
        # If mouse is hovering
        if self.face.collidepoint(pygame.mouse.get_pos()):
            
            # If the button is not already being hovered
            if not self.hovering:
                self.hovering = True # Sets button being hovered to true
                self.text.ChangeColor(color) # Change Text Color
                
                # Sound Effect Volume
                pygame.mixer.Channel(0).set_volume(.3) if effectState else pygame.mixer.Channel(0).set_volume(0)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.hoverSound)) if effectState else pygame.mixer.Channel(0).set_volume(0)
                
                self.RenderBtn() # Redraw Button

            # If the button is already being hovered
            else: self.HasClicked(click, *args) # Check if the button has been clicked
            
        # If mouse is not over the button but the button is still being hovered    
        elif not self.face.collidepoint(pygame.mouse.get_pos()) and self.hovering:
            self.hovering = False # Make sure when not hovered hover is set to false
            self.text.ChangeColor((255, 255, 255)) # Changes button color to white
            self.RenderBtn() # Redraw Button

    def HasClicked(self, click, *args) -> None:
        '''Check if a button has been clicked'''

        if pygame.mouse.get_pressed()[0]: # If button has been pressed with left click
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.selectSound)) # Play select sound
            click() if not args else click(args if len(args) > 1 else args[0]) # Run Click Method
            
            from time import sleep
            sleep(.3) # Stop multiple clicks being registered
    
    def RenderBtn(self) -> None:
        '''Render Button to Screen'''
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), self.face) # Render button rect
        self.text.RenderText() # Render button text

    @staticmethod
    def __name__(): return 'Btn' # Returns name of class (Button)

class Game:
    '''Game Class'''
        
    class Block(pygame.sprite.Sprite):
        '''Class for Blocks'''

        def __init__(self, struct:tuple[tuple], color:tuple): # Initialise Values
            '''Initialise Block Class

            Args:
            - struct (tuple): Shape of Block
            - color (tuple): Color of Block
            - pos (list, optional): Position to Draw Block at. Defaults to [450, 100]
                
            Instance Variables:
            - realPos (list[int]): Real Position of Block on Grid
            - blockSize (int): Block Rectangle Size
            - group (pygame.sprite.Group): Group of Rectangles in Block
            '''
            
            super().__init__()
            self.struct = struct
            self.color = color
            self.realPos = [450, 100]
            self.blockSize = 30
            self.rotNum = 1
            self.group = pygame.sprite.Group()

        def draw(self) -> None:
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
                    
            self.group.draw(pygame.display.get_surface()) # draw all rectangle sprites to the screen at once

        def Move(self, dirName:str, effectState:bool, sound:pygame.mixer.Sound) -> None:
            '''Moves Block in one direction one space

            Args:
                effectState (bool): Should SE play
                dirName (str): Direction of travel
                sound (pygame.mixer.Sound): Sound Object to Play
            '''
            
            self.UpdateColor((0, 0, 0)) # Update color of previous blocks
            self.group.empty() # empty sprite group
            
            match dirName: # check for direction of travel
                case 'left': 
                    self.group.update((30, 0))
                    self.realPos[0] -= 30
            
                case 'right':
                    self.group.update((-30, 0))
                    self.realPos[0] += 30
                        
                case 'down': 
                    if self.realPos[1] < 670:
                        self.group.update((0, 30))
                        self.realPos[1] += 30
            
            if effectState: pygame.mixer.Channel(0).play(sound)
            Game.Block.draw(self) # draw new block to screen

        def CheckCollision(self, blockGroup:pygame.sprite.Group, dir:str) -> bool:
            '''Checks for Block Collisions between the ground & other blocks

            Args:
            - blockGroup (pygame.sprite.Group): group of blocks to check for collision with
            - dir (string): Direction to Check for Collision Against

            Returns:
            - Bool: Whether or not the current block is about to collide 
            '''

            for i in range(len(blockGroup.sprites())):
                for j in range(len(self.group.sprites())):
                    if dir == 'down':
                        if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i], 'down'):
                            return True
                        
                    if dir == 'right':
                        if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i], 'right'):
                            return True
                        
                    if dir == 'left':
                        if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i], 'left'):
                            return True

            for i in range(len(self.group.sprites())): 
                if self.group.sprites()[i].posY == 670: return True

            return False

        def CheckMovable(self, dir:str, group:pygame.sprite.Group) -> bool:
            '''Checks to see if the current sprite is movable

            Args:
            - dir (str): Direction of Travel
            - group (pygame.sprite.Group): Block Group to Check For Collision Against

            Returns:
            - Bool: If the block is movable
            '''
            
            for i in range(len(self.group.sprites())):
                match dir:
                    case 'right':
                        if self.group.sprites()[i].posX == 600: return False
                        else:
                            for rect in self.group.sprites():
                                for gridRect in group.sprites():
                                    if self.WillCollide(rect, gridRect, 'right'): return False

                    case 'left':
                        if self.group.sprites()[i].posX == 360: return False
                        else:
                            for rect in self.group.sprites():
                                for gridRect in group.sprites():
                                    if self.WillCollide(rect, gridRect, 'left'): return False

            return True
                    
        def UpdateColor(self, color:tuple) -> None: # Temp fix for screen flashing
            '''Update Color of Sprite

            Args:
            - color (tuple): Color to Draw Sprite with
            '''
            
            originalColor = self.color # store original color
            self.color = color # set new color
            self.draw() # draw new colored block to screen
            self.color = originalColor # set color back to original color

        def Rotate(self, effectState:bool, sound:pygame.mixer.Sound, group:pygame.sprite.Group) -> None:
            '''Rotate Blocks clockwise 90 degrees

            Args:
            - effectState (Bool): Sound Effects Bool
            - sound (filePath): File Path to Sound File
            - group (pygame.sprite.Group): Block Group to Check Collision Against
            '''
            
            if not isinstance(self, Game.SquareBlock): # check if the block is not square, if its not square continue
                if self.CheckMovable('right', group) and self.CheckMovable('left', group):
                    if effectState: pygame.mixer.Channel(0).play(sound)
                    self.UpdateColor((0, 0, 0)) # update color of previous block
                    
                    if self.rotNum != len(self.rots)-1: self.rotNum += 1
                    else: self.rotNum = 0
                    
                    self.struct = self.rots[self.rotNum-1]
                    self.draw() # redraw new block positions

        # def Rotate(self, effectState:bool, sound:pygame.mixer.Sound, group:pygame.sprite.Group) -> None:
        #     '''Rotate Blocks clockwise 90 degrees

        #     Args:
        #     - effectState (Bool): Sound Effects Bool
        #     - sound (filePath): File Path to Sound File
        #     - group (pygame.sprite.Group): Block Group to Check Collision Against
        #     '''
            
        #     if not isinstance(self, Game.SquareBlock): # check if the block is not square, if its not square continue
        #         if self.CheckMovable('right', group) and self.CheckMovable('left', group):
        #             if effectState: pygame.mixer.Channel(0).play(sound)
        #             self.UpdateColor((0, 0, 0)) # update color of previous block
                    
        #             from numpy import rot90
        #             self.struct = rot90(self.struct) # rotate array 90 degrees clockwise
        #             self.draw() # redraw new block positions

        @staticmethod
        def WillCollide(sprite:pygame.sprite.Sprite, groupSprite:pygame.sprite.Sprite, dir:str) -> bool:
            '''Checks for Collision to determine whether a sprite is about to collide with a group

            Args:
            - sprite (pygame.Sprite): Sprite to check for collision with
            - group (pygame.sprite.Group): Group to check for collision with

            Returns:
            - Bool: If the Sprite is about to collide with the group or not
            '''
            
            import copy
            spriteRect = copy.copy(sprite.rect)
            
            match dir:
                case 'down': spriteRect.move_ip((0, 30))
                case 'right': spriteRect.move_ip((30, 0))
                case 'left': spriteRect.move_ip((-30, 0))
            
            if spriteRect.colliderect(groupSprite): return True
                
            return False

        @staticmethod
        def reachedTop(blockGroup:pygame.sprite.Group) -> bool:
            '''Check to see if the blockGroup has reached the top of the grid

            Args:
            - blockGroup (pygame.sprite.Group): group of Rectangles

            Returns:
            - Bool: Whether or not the group has reached the top
            '''
            
            for sprite in blockGroup:
                if sprite.posY == 130: return True
            return False

        @staticmethod
        def CheckCompletedRow(blockGroup:pygame.sprite.Group, effectState:bool, sound:pygame.mixer.Sound) -> bool:
            
            gridList = [
                [100, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [130, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [160, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [190, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [220, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [250, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [280, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [310, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [340, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [370, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [400, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [430, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [460, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [490, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [520, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [550, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [580, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [610, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [640, [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [670, [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            ]
            
            for block in blockGroup.sprites():
                for j in range(len(gridList)):
                    if block.posY == gridList[j][0]:
                        match block.posX: # Check for X Position & add 1 to correct position in grid object (1 means there's a rectangle, 0 means empty)
                            case 360: gridList[j][1][0] += 1 if gridList[j][1][0] != 1 else 0
                            case 390: gridList[j][1][1] += 1 if gridList[j][1][1] != 1 else 0
                            case 420: gridList[j][1][2] += 1 if gridList[j][1][2] != 1 else 0
                            case 450: gridList[j][1][3] += 1 if gridList[j][1][3] != 1 else 0
                            case 480: gridList[j][1][4] += 1 if gridList[j][1][4] != 1 else 0
                            case 510: gridList[j][1][5] += 1 if gridList[j][1][5] != 1 else 0
                            case 540: gridList[j][1][6] += 1 if gridList[j][1][6] != 1 else 0
                            case 570: gridList[j][1][7] += 1 if gridList[j][1][7] != 1 else 0
                            case 600: gridList[j][1][8] += 1 if gridList[j][1][8] != 1 else 0
                            case _: pass
                    
            row = 0
            
            for i in range(len(gridList)):
                count = 0
                
                for j in range(len(gridList[i][1])):
                    count += gridList[i][1][j]
                
                if count >= 9: 
                    return Game.Block.RemoveCompletedRow(blockGroup, gridList, row, effectState, sound)
                
                row += 1
            
            return False

        @staticmethod
        def RemoveCompletedRow(blockGroup:pygame.sprite.Group, gridList:list, rowPos:int, effectState:bool, sound:pygame.mixer.Sound) -> tuple:
            
            for rect in blockGroup.sprites():
                if rect.posY == gridList[rowPos][0]:
                    rect.color = (0, 0, 0)
                    rect.draw()
                    blockGroup.remove(rect)
            
            for i in range(len(gridList[rowPos][1])):
                if gridList[rowPos][1][i] == 1:
                    gridList[rowPos][1][i] -= 1
            
            if effectState: 
                pygame.mixer.Channel(3).set_volume(.2)
                pygame.mixer.Channel(3).play(sound)
            
            for rect in blockGroup:
                if rect.posY < gridList[rowPos][0]:
                    rect.UpdateColor((0, 0, 0))
                    rect.update((0, 30))

            blockGroup.draw(pygame.display.get_surface())
            
            return True

        @staticmethod
        def GetRandBlock():
            '''Choose Random Block From List of Blocks

            Returns:
            - Block: Different Block Shapes 
            '''
            
            from random import choice
            return choice((Game.LBlock, Game.SquareBlock, Game.TBlock, Game.SBlock, Game.ZBlock, Game.LineBlock, Game.JBlock))() # Returns Random Block

    class Rectangle(pygame.sprite.Sprite):
        '''Rectangle Class'''
        
        def __init__(self, pos:tuple, color:tuple, size:int):
            '''Initialises Rectangle Class

            Args:
            - pos (tuple): Position of the Rectangle
            - color (tuple): color of Rectangle
            - size (int): size of Rectangle
                
            Instance Variables:
            - posX (int): horizontal position of the Rectangle
            - posY (int): vertical position of the Rectangle
            - rect (pygame.Rect): Rectangle Rect
            - image (pygame.Surface): Rectangle Surface
            '''
            
            super().__init__() # get values from inherited class
            self.posX, self.posY = pos
            self.size = size
            self.color = color
            self.rect = pygame.Rect(self.posX, self.posY, self.size, self.size)
            self.image = pygame.Surface([self.size, self.size])
            self.image.fill(self.color) # fill rect with appropriate color
            
        def update(self, dir:str): 
            self.rect.move_ip(dir) # update position of rect
            self.posX, self.posY = self.rect[0], self.rect[1]
        
        def draw(self): pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect) # draw rect to screen
            
        def UpdateColor(self, color:tuple) -> None: # Temp fix for screen flashing
            '''Update Color of Sprite

            Args:
            - color (tuple): Color to Draw Sprite with
            '''
            
            originalColor = self.color # store original color
            self.color = color # set new color
            self.draw() # draw new colored block to screen
            self.color = originalColor # set color back to original color

    class LBlock(Block):
        def __init__(self): 
            super().__init__(((0, 0, 0), (0, 0, 1), (1, 1, 1)), (255, 165, 0)) # initialise values for class
            self.rots = [
                ((0, 0, 0), (0, 0, 1), (1, 1, 1)),
                ((1, 0, 0), (1, 0, 0), (1, 1, 0)),
                ((0, 0, 0), (1, 1, 1), (1, 0, 0)),
                ((1, 1, 0), (0, 1, 0), (0, 1, 0))
            ]

    class SquareBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (1, 1, 0), (1, 1, 0)), (255, 255, 0)) # initialise values for class

    class TBlock(Block):
        def __init__(self): 
            super().__init__(((0, 0, 0), (0, 1, 0), (1, 1, 1)), (128, 0, 128)) # initialise values for class
            self.rots = [
                ((0, 0, 0), (0, 1, 0), (1, 1, 1)),
                ((1, 0, 0), (1, 1, 0), (1, 0, 0)),
                ((0, 0, 0), (1, 1, 1), (0, 1, 0)),
                ((0, 1, 0), (1, 1, 0), (0, 1, 0))
            ]
    
    class SBlock(Block):
        def __init__(self): 
            super().__init__(((0, 0, 0), (0, 1, 1), (1, 1, 0)), (0, 128, 0)) # initialise values for class
            self.rots = [
                ((0, 0, 0), (0, 1, 1), (1, 1, 0)),
                ((1, 0, 0), (1, 1, 0), (0, 1, 0)),
            ]
    
    class ZBlock(Block):
        def __init__(self): 
            super().__init__(((0, 0, 0), (1, 1, 0), (0, 1, 1)), (128, 0, 0)) # initialise values for class
            self.rots = [
                ((0, 0, 0), (1, 1, 0), (0, 1, 1)),
                ((0, 1, 0), (1, 1, 0), (1, 0, 0))
            ]

    class LineBlock(Block): # TODO: Fix
        def __init__(self): 
            super().__init__(((0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0)), (0, 255, 255)) # initialise values for class
            self.rots = [
                ((0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0)),
                ((0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0))
            ]

    class JBlock(Block):
        def __init__(self): 
            super().__init__(((0, 0, 0), (1, 0, 0), (1, 1, 1)), (0, 0, 255)) # initialise values for class
            self.rots = [
                ((0, 0, 0), (1, 0, 0), (1, 1, 1)),
                ((1, 1, 0), (1, 0, 0), (1, 0, 0)),
                ((0, 0, 0), (1, 1, 1), (0, 0, 1)),
                ((0, 1, 0), (0, 1, 0), (1, 1, 0))
            ]

class GridRect(pygame.sprite.Sprite):
    '''GridRect Class'''
    
    def __init__(self, pos:tuple, size:int, color:tuple=(200, 200, 200)): # initialise values
        '''Initialises GridRect Class

        Args:
        - pos (tuple): represents block position
        - size (int): represents block size
            
        Instance Variables:
        - posX (int): represents x position of block
        - posY (int): represents y position of block
        - size (int): represents size of block
        - color (tuple): represents color of block
        - rect (pygame.Rect): represents Rect object of block
        - image (pygame.Surface): represents surface of block
        '''
    
        super().__init__() # initialise default values from inherited class
        self.posX, self.posY = pos
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.posX, self.posY, self.size, self.size)
        self.image = pygame.Surface([self.size, self.size])

    def drawRect(self):
        '''Draw Rect Object of GridRect to screen'''
        
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect, 1)

class Grid:
    '''Grid Class'''
    
    def __init__(self, gridPos:tuple, totalGridSize:tuple=(630, 700)): # initialise values       
        '''Initialises a new instance of the Grid Class
        
        Args:
        - gridPos (tuple): represents position of where to start drawing the grid
        - totalGridSize (tuple, optional): represents the total size of the grid
        
        Instance Variables:
        - sizeX (int): represents the horizontal position of the grid
        - sizeY (int): represents the vertical position of the grid
        - blockSize (int): represents the size of each grid block
        - gridX (int): represents the total horizontal size of the grid
        - gridY (int): represents the total vertical size of the grid
        - gridGroup (pygame.sprite.Group): A sprite group containing the grid blocks
        '''
        
        self.posX, self.posY = gridPos
        self.blockSize = 30
        self.gridX, self.gridY = totalGridSize
        self.gridGroup = pygame.sprite.Group()

    def DrawGrid(self) -> None:
        '''Draws Grid to Screen'''
        
        # for horizontal grid blocks, starting & ending at limits with each step being of size blockSize
        for x in range(self.posX, self.gridX, self.blockSize): 
            # for vertical grid blocks, starting & ending at limits with each step being of size blockSize
            for y in range(self.posY, self.gridY, self.blockSize):
                # create a GridRect instance, add it to gridGroup & draw it to the screen
                if y != 160 or x != 300: gridBlock = GridRect((x, y), self.blockSize)
                if y == 160: gridBlock = GridRect((x, y), self.blockSize, (255, 0, 0)) # Draw Height Limit of Grid in Diff Color
                if x == 420: gridBlock = GridRect((x, y), self.blockSize, (255, 0, 0))
                self.gridGroup.add(gridBlock)
                gridBlock.drawRect()

class Settings:
    '''Class for Game Settings'''
    
    def __init__(self, musicState:bool=True, effectState:bool=True):
        '''Initialises Settings Class

        Args:
        - musicState (bool, optional): Allow Music. Defaults to True.
        - effectState (bool, optional): Allow Sound Effects. Defaults to True.
        '''
        
        self.musicState = musicState
        self.effectState = effectState
        self.filePath = f'{str(Path(__file__).parents[1])}\\settings.txt'

    def init(self) -> None:
        '''Get Settings from File'''
        
        import os.path # to find file paths on device (windows only)
        
        if not os.path.isfile(self.filePath): self.WriteSettings(False) # create the settings file if it does not exist

        else: # Otherwise
            with open(self.filePath) as f: # Open the file
                settings = f.read().split(',') # Split value(s) by comma

            self.musicState = True if settings[0] == 'True' else False # Set the music state to true if the settings value is true
            self.effectState = True if settings[1] == 'True' else False # Set the sound effects state to true if the settings value is true            

    def WriteSettings(self, rem:bool=False) -> None:
        '''Write Settings to Settings file

        Args:
        - rem (bool, optional): remove file if True. Defaults to False
        '''
        
        from src.utils.ClrTerminal import Color # Debugging Tool
        from os import remove # Removes Files from device (windows only)
        
        if rem: 
            try: remove(self.filePath) # if we set rem to True, remove settings file
            except OSError as e: Color.printe(f'An Unexpected Error Occurred Whilst Removing {self.filePath}\n{e}') # Log Errors to Terminal
            
        with open(self.filePath, 'w') as f: # open settings file as write
            f.write(f'{str(self.musicState)},') # write new musicState value to file
            f.write(f'{str(self.effectState)}') # write new effectState value to file
            
        self.init() # re-initialise settings

    def ChangeSettings(self, musicBool=None, effectsBool=None) -> None:
        '''Changes Setting Bool's & Writes any changes to settings file

        Args:
        - musicBool (bool, optional): value to set musicState to. Defaults to None.
        - effectsBool (bool, optional): value to set effectState to. Defaults to None.
        '''
        
        self.musicState = musicBool if musicBool != None else self.musicState # ternary operation
        self.effectState = effectsBool if effectsBool != None else self.effectState # ternary operation
        self.WriteSettings(True)

class Highscore:
    '''Highscore Class'''
    
    def __init__(self, name:str='PLA', score:int=0):
        '''
        Initialises Highscore class

        Args:
            name (str, optional): name of user. Defaults to 'PLA'.
            score (int, optional): score of user. Defaults to 0.
        '''
        
        self.name = name
        self.score = score

    def BubbleSortScores(self, scoreList:list) -> list[list]:
        '''Sorts Scores in Order of Highest First, Lowest Last

        Args:
            scoreList (list): List of Highscore Objects

        Returns:
            list[list]: List of lists in the form of [name, score]
        '''
        
        scoreList.append(Highscore(self.name, self.score))
        
        for i in range(len(scoreList)):
            for j in range (len(scoreList)-i-1):
                if scoreList[j+1].score > scoreList[j].score:
                    scoreList[j], scoreList[j+1] = scoreList[j+1], scoreList[j]
        
        return [[score.name, score.score] for score in scoreList]

    @staticmethod
    def GetScoresFromFile(filePath:str) -> list:
        '''Retrieves Score Data from a Given File

        Returns:
            list: list of Highscore(name, score)
        '''
        
        from .utils.ClrTerminal import Color # Import for Color Coding Terminal Output
        
        try:
            with open(filePath) as f: # open file
                data = f.read().split(',') # read data from file and split by commas
            
            names, scores = [], [] # Temporary arrays for data from file
            
            for value in data: # for value (str | int) in file data
                try:
                    scores.append(int(value)) # try to cast value to int
                except ValueError: # if cast fails, assume its a name
                    names.append(value)
                
            highscores = [Highscore(name, score) for name, score in zip(names, scores)] # create list of Highscore objects

            Color.prints(f'Successfully Retrieved Score data from {filePath}')
            
            return highscores

        except Exception as e:
            Color.printe(f'Unexpected Error Occurred during data retrieval\n{e}')
            return []

    @staticmethod
    def WriteScoresToFile(filePath:str, scores:list) -> bool:
        '''
            Writes Scores to File Passed in\n
            Return(s):
                - True if Success
                - False if Error
        '''

        from src.utils.ClrTerminal import Color
        
        scores = Highscore.CheckForDupes(scores)
        
        try:
        
            with open(filePath, 'w') as f:
                for score in scores:
                
                    if score == ['DEV', 100000] or score == ['PLA', 0]: pass
                    else: f.write(f'{score[0]},{score[1]},')
                
            Color.prints(f'Successfully written scores to {filePath}')   
            return True

        except Exception as e: 
            Color.printe(f'Unexpected Error occurred whilst writing scores to {filePath}\n{e}')
            return False
        
    @staticmethod
    def CheckForDupes(scores:list) -> list:
        arr = []
        
        for i in range(len(scores)):
            if scores[i] != scores[i-1]:
                arr.append(scores[i])

        return arr
    
    @staticmethod
    def CommitToDb(scores:list) -> list[tuple]:
        '''
            Commits Score Data to SQL Database
            Return(s): None
        '''
        
        from src.utils.ClrTerminal import Color
        import pyodbc as dbc
        
        topScores = []
        
        try:
        
            Color.printd('Please Wait Whilst The Program Attempts to connect to the database, this could take some time...')
            Color.printd('WARNING: This May Cause an Error Message if you do not have an SQL Server Active')
        
            # Connection string for SQL Server
            conn_str = f'''
            DRIVER=SQL SERVER;
            SERVER=HelmsRig;
            DATABASE=highscores;
            Trust_Connection=yes;
            '''

            # Establish Connection & create cursor
            conn = dbc.connect(conn_str)
            cursor = conn.cursor()
            
            Color.prints('Successfully Connected to the Database!')
            Color.printd('Attempting to Commit Data...')
            
            cursor.execute('TRUNCATE TABLE highscore;') # Clear out existing data in 'highscore' table
            
            # define insert query
            ins_query = f'''INSERT INTO highscore (name, score) VALUES (?, ?);'''
            
            # iterate over scores list & insert each score into database
            for name, score in scores: cursor.execute(ins_query, (name, score))
                
            # commit changes to db & print success msg
            conn.commit() 
            
            Color.prints('Committed Data to Database Successfully')
            Color.printd('Attempting to Retrieve Committed Data from Database...')
        
            # Attempt to retrieve score data
            try:
                data = cursor.execute('SELECT * FROM highscore;')
            
                # iterate over retrieved data & append each row to topScores
                topScores = [[name, score] for name, score in data]
                
                # print success msg
                Color.prints('Successfully retrieved score data from database')
                
                conn.close() # closes connection to db
                
                Color.prints(f'Data: {topScores}')
                return topScores # return the top scores that were retrieved (if any)
            
            # If there was an error retrieving the data, print an error message
            except Exception as e: Color.printe(f'Error whilst trying to retrieve score data\n{e}')
        
        # If there was an error committing data to the database, print an error message
        except Exception as e:
            Color.printe(f'Error: There was an unexpected error whilst trying to commit data to the sql database\n{e}')