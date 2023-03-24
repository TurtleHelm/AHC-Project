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
        
        self.screen_size = (960, 720) # set window size
        self.window_title = window_title # set window title
        self.bg_color = bg_color # set background color
        self.icon = pygame.image.load(f'{str(Path(__file__).parents[0])}\\resources\\images\\icon.png') # set window icon
        
    def CreateNewWindow(self) -> None:
        '''Creates new Window using appropriate values'''
        
        self.win = pygame.display.set_mode(size=self.screen_size) # initialise window with set size
        self.win.fill(self.bg_color) # fill window with background color
        pygame.display.set_caption(self.window_title) # give window title
        pygame.display.set_icon(self.icon) # give window icon
        pygame.display.flip() # update window

    @staticmethod
    def ExitWindow():
        '''Exits the Game'''
        
        from src.utils.ClrTerminal import Color
        pygame.display.quit() # exit display
        Color.printd('Exiting Window...')
        pygame.quit() # exit pygame
        quit(0) # exit program

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
            
        pygame.display.flip() # update screen

    @staticmethod
    def Leave() -> None:
        '''Navigate Back to the Home Page'''
        from .home import run
        run() # run home page procedure

class Text(pygame.sprite.Sprite):
    '''Text Class (GUI)'''

    def __init__(self, pos:list=[0, 0], text:str='Text', fontsize:int=20, color:tuple=(255, 255, 255)):
        '''Intialises Text Object

        Args:
        - text (str, optional): Text to be created. Defaults to 'Text'.
        - pos (list, optional): Position of Text on Screen. Defaults to [0, 0].
        - fontsize (int, optional): size of text. Defaults to 20.
        - color (tuple, optional): color of text. Defaults to (255, 255, 255).
        '''
        
        super().__init__() # Initialise the inherited class
        if not pygame.font.get_init: pygame.font.init() # Initialise Font 
        
        self.surface = pygame.display.get_surface() # Get Window Surface
        self.givenPos = pos # set text position
        
        self.color = color # set text color
        
        self.fontsize = fontsize # set text size
        self.text = pygame.font.Font(f'{str(Path(__file__).parents[0])}\\resources\\fonts\\font.ttf', self.fontsize).render(text, False, self.color) # Creates Font Object
        
        self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # Set Position of Text
        self.caption = text # set caption to text string

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
    def __name__(): return 'Text' # Used to determine object type whilst rendering
    def ReturnText(self): return self.caption # Returns Text Content Of Instance

class Btn(pygame.sprite.Sprite):
    '''Btn Class (GUI)'''
    
    def __init__(self, text:str='', pos:list=[0, 0], width:int=112, height:int=40, fontsize:int=16):
        '''Initialise Btn object

        Args:
        - caption (str): Text to be drawn to screen
        - pos (list, optional): Position of Button. Defaults to [0, 0].
        - width (int, optional): Width of Button. Defaults to 112.
        - height (int, optional): Height of Button. Defaults to 40.
        - fontsize (int, optional): Size of Text. Defaults to 16.
        '''
        
        super().__init__() # initialises default values from inherited class
        
        self.pos = pos # set btn position
        self.surf = pygame.display.get_surface() # set window surface to current surface
        self.face = pygame.Rect(self.pos, (width, height)) # set btn face to rectangle
        self.face.center = self.pos # set rectangle centre to be btn position
        self.hovering = False # set hover checking False initially
        self.fontsize = fontsize # set btn text size
        self.textColor = (255, 255, 255) # set btn text color initially white
        self.text = Text(self.pos, text, self.fontsize, self.textColor) # Create Btn Text Object
        self.state = False # set state initially False
        self.hoverSound = f'{str(Path(__file__).parents[0])}\\resources\\sounds\\hoverSound.wav' # set hover sound
        self.selectSound = f'{str(Path(__file__).parents[0])}\\resources\\sounds\\selectSound.wav' # set select sound

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
        if self.face.collidepoint(pygame.mouse.get_pos()): # if mouse is hovering over btn rectangle
            if not self.hovering: # If the button is not already being hovered
                self.hovering = True # Sets button being hovered to true
                self.text.ChangeColor(color) # Change Text Color
            
                pygame.mixer.Channel(0).set_volume(.3) if effectState else pygame.mixer.Channel(0).set_volume(0) # set volume of SE only if allowed
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.hoverSound)) if effectState else pygame.mixer.Channel(0).set_volume(0) # play SE only if allowed
                
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

        def __init__(self, struct:tuple[tuple], color:tuple):
            '''Initialise Block Class

            Args:
            - struct (tuple[tuple]): Shape of Block
            - color (tuple): Color of Block
            - pos (list, optional): Position to Draw Block at. Defaults to [450, 100]
            '''
            
            super().__init__() # initialise values from inherited class
            self.struct = struct # set default structure
            self.color = color # set color of block
            self.realPos = [450, 100] # set default position
            self.blockSize = 30 # set size of each rectangle
            self.rotNum = 1 # set initial rotation number
            self.group = pygame.sprite.Group() # set rectangle group

        def draw(self) -> None:
            '''Draws a block to the screen at the appropriate coordinates'''
            posX, posY = self.realPos # set positions to draw to
            
            for y in range(len(self.struct)): # vertical
                for x in range(len(self.struct[y])): # horizontal
                    if y > 0 and x == 0: # if reached end of row in tuple
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
                dirName (str): Direction of travel
                effectState (bool): Should SE play
                sound (pygame.mixer.Sound): Sound Object to Play
            '''
            
            self.UpdateColor((0, 0, 0)) # Update color of previous blocks
            self.group.empty() # empty sprite group
            
            match dirName: # check for direction of travel
                case 'left': 
                    self.group.update((30, 0)) # move whole group left 1 space
                    self.realPos[0] -= 30 # update position
            
                case 'right': 
                    self.group.update((-30, 0)) # move whole group right 1 space
                    self.realPos[0] += 30 # update position
                        
                case 'down': 
                    if self.realPos[1] < 670: # as long as block hasn't reached the grid base
                        self.group.update((0, 30)) # move whole group down 1 space
                        self.realPos[1] += 30 # update position
            
            if effectState: pygame.mixer.Channel(0).play(sound) # play SE if SE allowed
            Game.Block.draw(self) # draw new block to screen

        def CheckCollision(self, blockGroup:pygame.sprite.Group, dir:str) -> bool:
            '''Checks for Block Collisions between the ground & other blocks

            Args:
            - blockGroup (pygame.sprite.Group): group of blocks to check for collision with
            - dir (string): Direction to Check for Collision Against

            Returns:
            - Bool: Whether or not the current block is about to collide 
            '''

            for i in range(len(blockGroup.sprites())): # for each Rectangle in the block group
                for j in range(len(self.group.sprites())): # for each rectangle in the current block
                    if dir == 'down': 
                        if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i], 'down'): # if the block will collide on the next turn
                            return True
                        
                    if dir == 'right':
                        if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i], 'right'): # if the block will collide on the next turn
                            return True
                        
                    if dir == 'left':
                        if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i], 'left'): # if the block will collide on the next turn
                            return True

            for block in self.group.sprites: # for each rectangle in the current block
                if block.posY == 670: return True # if any of the blocks are at the grid base, return True

            return False # if there is no collisions, return False

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
                    
        def UpdateColor(self, color:tuple) -> None:
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
                if self.CheckMovable('right', group) and self.CheckMovable('left', group): # if the block is movable in both directions
                    if effectState: pygame.mixer.Channel(0).play(sound) # if SE allowed, play SE
                    self.UpdateColor((0, 0, 0)) # update color of previous block
                    
                    if self.rotNum != len(self.rots)-1: self.rotNum += 1 # if number of rotation is not at max, add 1 to rotation number
                    else: self.rotNum = 0 # otherwise reset rotation number
                    
                    self.struct = self.rots[self.rotNum-1] # set block structure to next rotation in list
                    self.draw() # redraw new block positions

        @staticmethod
        def WillCollide(sprite:pygame.sprite.Sprite, groupSprite:pygame.sprite.Sprite, dir:str) -> bool:
            '''Checks for Collision to determine whether a sprite is about to collide with a group

            Args:
            - sprite (pygame.Sprite): Sprite to check for collision with
            - group (pygame.sprite.Group): Group to check for collision with

            Returns:
            - bool: If the Sprite is about to collide with the group or not
            '''
            
            import copy
            spriteRect = copy.copy(sprite.rect) # make a copy of the rectangle
            
            match dir: # check direction of checking & move the duplicate rectangle
                case 'down': spriteRect.move_ip((0, 30)) 
                case 'right': spriteRect.move_ip((30, 0))
                case 'left': spriteRect.move_ip((-30, 0))
            
            if spriteRect.colliderect(groupSprite): return True # Check for collision between the duplicate rectangle & the sprite group, return True is there's a collision
                
            return False # Return False if there's no collision

        @staticmethod
        def reachedTop(blockGroup:pygame.sprite.Group) -> bool:
            '''Check to see if the blockGroup has reached the top of the grid

            Args:
            - blockGroup (pygame.sprite.Group): group of Rectangles

            Returns:
            - Bool: Whether or not the group has reached the top
            '''
            
            for sprite in blockGroup: # for each rectangle in the sprite group
                if sprite.posY == 130: return True # if the rectangle is at y position 130, return True
            return False # if no rectangles are at 130, return False

        @staticmethod
        def CheckCompletedRow(blockGroup:pygame.sprite.Group, effectState:bool, sound:pygame.mixer.Sound) -> bool:
            '''Checks for a Completed Row in the Grid
            
            Args:
            - blockGroup (pygame.sprite.Group): Sprite Group of blocks to check over
            - effectState (bool): Whether or not Sound should be played
            - sound (pygame.mixer.Sound): The Sound to be Played on line clear
            
            Returns:
            - bool: Whether or not a row has been completed
            '''
            
            
            gridList = [ # fake grid to check for line completions with, y = grid position of row, x = row of grid squares
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
            
            for block in blockGroup.sprites(): # for each rectangle in the sprite group
                for j in range(len(gridList)): # for each row in the gridList
                    if block.posY == gridList[j][0]: # if a block is at the same position as the gridList position
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
                            case _: pass # if there's no match, simply ignore
                    
            row = 0 # row counter
            
            for i in range(len(gridList)): # go through each row in the grid
                count = 0 # rectangle counter
                
                for j in range(len(gridList[i][1])): # go through each grid square in the row
                    count += gridList[i][1][j] # add to the counter if there's a rectangle at the current grid square
                
                if count >= 9: # if there's a full row
                    return Game.Block.RemoveCompletedRow(blockGroup, gridList, row, effectState, sound) # remove the row & return True
                
                row += 1 # if there's no row, add 1 to the row counter
            
            return False # Return False if there is no completed rows

        @staticmethod
        def RemoveCompletedRow(blockGroup:pygame.sprite.Group, gridList:list, rowPos:int, effectState:bool, sound:pygame.mixer.Sound) -> bool:
            '''Removes Completed Row from screen & moves all other blocks down
            
            Args:
            - blockGroup (pygame.sprite.Group): Group of Blocks to Check over
            - gridList (list): Fake Grid Used to Check for Row Completions
            - rowPos (int): Row Position in Grid at which the row is cleared
            - effectState (bool): Whether or not Sound should be played
            - sound (pygame.mixer.Sound): The Sound to be Played on line clear
            
            Returns:
            - bool (True): Returns True once the line is cleared
            '''
            
            for rect in blockGroup.sprites(): # for each Rectangle object in the block group
                if rect.posY == gridList[rowPos][0]: # if rectangle is in the row to be cleared
                    rect.color = (0, 0, 0) # set rectangle to black to hide it
                    rect.draw() # draw rectangle
                    blockGroup.remove(rect) # remove rectangle from group
            
            if effectState: # if SE allowed
                pygame.mixer.Channel(3).set_volume(.2) # set volume
                pygame.mixer.Channel(3).play(sound) # play sound
            
            for rect in blockGroup.sprites(): # for each Rectangle object in the block group
                if rect.posY < gridList[rowPos][0]: # if rectangle is in any row above the row to be cleared
                    rect.UpdateColor((0, 0, 0)) # Update Rectangle Color
                    rect.update((0, 30)) # Update rectangle position

            blockGroup.draw(pygame.display.get_surface()) # Draw Block Group to screen
            
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
            '''
            
            super().__init__() # get values from inherited class
            self.posX, self.posY = pos # set default position
            self.size = size # set size
            self.color = color # set color
            self.rect = pygame.Rect(self.posX, self.posY, self.size, self.size) # set Rect Object
            self.image = pygame.Surface([self.size, self.size]) # set Surface Object
            self.image.fill(self.color) # fill rect with appropriate color
            
        def update(self, dir:str) -> None: 
            self.rect.move_ip(dir) # update position of rect
            self.posX, self.posY = self.rect[0], self.rect[1] # set positions to new positions
        
        def draw(self) -> None: pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect) # draw rect to screen
            
        def UpdateColor(self, color:tuple) -> None:
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
            self.rots = [ # All Rotations of Block
                ((0, 0, 0), (0, 0, 1), (1, 1, 1)),
                ((1, 0, 0), (1, 0, 0), (1, 1, 0)),
                ((0, 0, 0), (1, 1, 1), (1, 0, 0)),
                ((1, 1, 0), (0, 1, 0), (0, 1, 0))
            ]
            super().__init__(self.rots[0], (255, 165, 0)) # initialise values for class

    class SquareBlock(Block):
        def __init__(self): super().__init__(((0, 0, 0), (1, 1, 0), (1, 1, 0)), (255, 255, 0)) # initialise values for class

    class TBlock(Block):
        def __init__(self): 
            self.rots = [ # All Rotations of Block
                ((0, 0, 0), (0, 1, 0), (1, 1, 1)),
                ((1, 0, 0), (1, 1, 0), (1, 0, 0)),
                ((0, 0, 0), (1, 1, 1), (0, 1, 0)),
                ((0, 1, 0), (1, 1, 0), (0, 1, 0))
            ]
            super().__init__(self.rots[0], (128, 0, 128)) # initialise values for class

    class SBlock(Block):
        def __init__(self): 
            self.rots = [ # All Rotations of Block
                ((0, 0, 0), (0, 1, 1), (1, 1, 0)),
                ((1, 0, 0), (1, 1, 0), (0, 1, 0)),
            ]
            super().__init__(self.rots[0], (0, 128, 0)) # initialise values for class
    
    class ZBlock(Block):
        def __init__(self): 
            self.rots = [ # All Rotations of Block
                ((0, 0, 0), (1, 1, 0), (0, 1, 1)),
                ((0, 1, 0), (1, 1, 0), (1, 0, 0))
            ]
            super().__init__(self.rots[0], (128, 0, 0)) # initialise values for class

    class LineBlock(Block):
        def __init__(self): 
            self.rots = [ # All Rotations of Block
                ((0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0)),
                ((0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0))
            ]
            super().__init__(self.rots[0], (0, 255, 255)) # initialise values for class
            self.realPos = [420, 130]

    class JBlock(Block):
        def __init__(self): 
            self.rots = [ # All Rotations of Block
                ((0, 0, 0), (1, 0, 0), (1, 1, 1)),
                ((1, 1, 0), (1, 0, 0), (1, 0, 0)),
                ((0, 0, 0), (1, 1, 1), (0, 0, 1)),
                ((0, 1, 0), (0, 1, 0), (1, 1, 0))
            ]
            super().__init__(self.rots[0], (0, 0, 255)) # initialise values for class

class GridRect(pygame.sprite.Sprite):
    '''GridRect Class'''
    
    def __init__(self, pos:tuple, size:int, color:tuple=(200, 200, 200)):
        '''Initialises GridRect Class

        Args:
        - pos (tuple): represents block position
        - size (int): represents block size
        - color (tuple): set the grid rectangle border to a color, defaults to (200, 200, 200)
        '''
    
        super().__init__() # initialise default values from inherited class
        self.posX, self.posY = pos # set position
        self.size = size # set size
        self.color = color # set color
        self.rect = pygame.Rect(self.posX, self.posY, self.size, self.size) # set Rect object
        self.image = pygame.Surface([self.size, self.size]) # set Surface object

    def drawRect(self) -> None:
        '''Draw Rect Object of GridRect to screen'''
        
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect, 1) # draw Grid Rectangle to screen

class Grid:
    '''Grid Class'''
    
    def __init__(self, gridPos:tuple, totalGridSize:tuple=(630, 700)):
        '''Initialises a new instance of the Grid Class
        
        Args:
        - gridPos (tuple): represents position of where to start drawing the grid
        - totalGridSize (tuple, optional): represents the total size of the grid
        '''
        
        self.posX, self.posY = gridPos # set position of grid
        self.blockSize = 30 # set block size for grid rectangles
        self.gridX, self.gridY = totalGridSize # set total grid size
        self.gridGroup = pygame.sprite.Group() # set grid rectangle group

    def DrawGrid(self) -> None:
        '''Draws Grid to Screen'''
        
        # for horizontal grid blocks, starting & ending at limits with each step being of size blockSize
        for x in range(self.posX, self.gridX, self.blockSize): 
            # for vertical grid blocks, starting & ending at limits with each step being of size blockSize
            for y in range(self.posY, self.gridY, self.blockSize):
                # create a GridRect instance, add it to gridGroup & draw it to the screen
                if y != 160: gridBlock = GridRect((x, y), self.blockSize) # if the gridBlock y position isn't at 160, draw normally
                if y == 160: gridBlock = GridRect((x, y), self.blockSize, (255, 0, 0)) # Draw Height Limit of Grid in red
                self.gridGroup.add(gridBlock) # add new gridBlock to group
                gridBlock.drawRect() # draw new gridBlock

class Settings:
    '''Class for Game Settings'''
    
    def __init__(self, musicState:bool=True, effectState:bool=True):
        '''Initialises Settings Class

        Args:
        - musicState (bool, optional): Allow Music. Defaults to True.
        - effectState (bool, optional): Allow Sound Effects. Defaults to True.
        '''
        
        self.musicState = musicState # set musicState
        self.effectState = effectState # set MusicState
        self.filePath = f'{str(Path(__file__).parents[1])}\\settings.txt' # Set settings file path

    def init(self) -> None:
        '''Get Settings from File'''
        
        import os.path # to find file paths on device
        
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
        
        self.musicState = musicBool if musicBool != None else self.musicState # ternary operation to check for changes to the musicState
        self.effectState = effectsBool if effectsBool != None else self.effectState # ternary operation to check for changes to the effectState
        self.WriteSettings(True) # Write Settings to File

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
        
        scoreList.append(Highscore(self.name, self.score)) # Append users score & name to the list before sorting
        
        for i in range(len(scoreList)): # for each Highscore Object in scoreList
            for j in range (len(scoreList)-i-1): # for each Highscore Object below the previous one in scoreList
                if scoreList[j+1].score > scoreList[j].score: # if the score below the score above is higher
                    scoreList[j], scoreList[j+1] = scoreList[j+1], scoreList[j] # switch the score positions
        
        return [[score.name, score.score] for score in scoreList] # List Comprehension to return all scores & names in sorted order

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
                    names.append(value) # append name to names array
                
            highscores = [Highscore(name, score) for name, score in zip(names, scores)] # create list of Highscore objects

            Color.prints(f'Successfully Retrieved Score data from {filePath}')
            
            return highscores # return array of Highscore Objects

        except OSError as e: # If No File, make one
            Color.printe(f'Unexpected Error Occurred during data retrieval\n{e}')
            with open(filePath, 'w') as f: f.write('BEN,6900,')
            
            return [Highscore('BEN', 6900)]

    @staticmethod
    def WriteScoresToFile(filePath:str, scores:list) -> bool:
        '''
            Writes Scores to File Passed in\n
            Return(s):
                - True if Success
                - False if Error
        '''

        from src.utils.ClrTerminal import Color
        
        scores = Highscore.CheckForDupes(scores) # Check for any duplicate scores in the list of scores & reassign the rest back
        
        try:
            with open(filePath, 'w') as f: # open score file
                for score in scores: # for each score in the scores file
                
                    if score[0] == 'DEV' or score[0] == 'PLA': pass # if the users nanme is either 'DEV' or 'PLA' then ignore this user
                    else: f.write(f'{score[0]},{score[1]},') # write the new scores back to the scores file
                
            Color.prints(f'Successfully written scores to {filePath}')  
            return True # Return True if successful

        except Exception as e: # If there was an error
            Color.printe(f'Unexpected Error occurred whilst writing scores to {filePath}\n{e}') # log to console
            return False # Return False due to error
        
    @staticmethod
    def CheckForDupes(scores:list) -> list:
        arr = [] # Temp array for sorting
        
        for i in range(len(scores)): # for each item in scores
            if scores[i] != scores[i-1]: # if the item below the item above are different
                arr.append(scores[i]) # append the item to the temp array

        return arr # return array of Highscores without the duplicate scores
    
    @staticmethod
    def CommitToDb(scores:list) -> list[tuple]:
        '''
            Commits Score Data to SQL Database
            
            Args:
            - scores (list): List of scores to write to the database table
            
            Returns:
            - list[tuple]: A list of tuples of the names & scores retrieved from the database
        '''
        
        from src.utils.ClrTerminal import Color
        import pyodbc as dbc # database management module
        
        topScores = [] # array to get the top scores with
        
        try: # Attempt to commit scores to the database
            Color.printd('Please Wait Whilst The Program Attempts to connect to the database, this could take some time...')
            Color.printd('WARNING: This May Cause an Error Message if you do not have an SQL Server Active')
        
            # Connection string for SQL Server
            conn_str = f'''
            DRIVER=SQL SERVER;
            SERVER=HelmsRig;
            DATABASE=highscores;
            Trust_Connection=yes;
            '''

            conn = dbc.connect(conn_str) # Establish Connection With Database
            cursor = conn.cursor() # Create a cursor object
            
            Color.prints('Successfully Connected to the Database!')
            Color.printd('Attempting to Commit Data...')
            
            cursor.execute('TRUNCATE TABLE highscore;') # Clear out existing data in 'highscore' table
            ins_query = f'''INSERT INTO highscore (name, score) VALUES (?, ?);''' # define insert query
            
            for name, score in scores: cursor.execute(ins_query, (name, score)) # iterate over scores list & insert each score into database
                
            conn.commit() # commit changes to db & print success msg
            
            Color.prints('Committed Data to Database Successfully')
            Color.printd('Attempting to Retrieve Committed Data from Database...')
            
            try: # Attempt to retrieve score data
                data = cursor.execute('SELECT * FROM highscore;')
                
                topScores = [[name, score] for name, score in data] # iterate over retrieved data & append each row to topScores
                Color.prints('Successfully retrieved score data from database') # print success msg
                
                conn.close() # closes connection to database
                
                Color.prints(f'Data: {topScores}')
                return topScores # return the top scores that were retrieved (if any)
            
            # If there was an error retrieving the data, print an error message
            except Exception as e: Color.printe(f'Error whilst trying to retrieve score data\n{e}')
        
        # If there was an error committing data to the database, print an error message
        except Exception as e: Color.printe(f'Error: There was an unexpected error whilst trying to commit data to the sql database\n{e}')