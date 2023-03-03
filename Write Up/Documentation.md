# Documentation

## Table

| Classes   | Quick Search       |
| :-------: | :----------------: |
| Window    | [Link](#window)    |
| Btn       | [Link](#btn)       |
| Text      | [Link](#text)      |
| Game      | [Link](#game)      |
| GridRect  | [Link](#gridrect)  |
| Grid      | [Link](#grid)      |
| Settings  | [Link](#settings)  |
| Highscore | [Link](#highscore) |

| [Subclasses](#subclasses) | Quick Search         |
| :-----------------------: | :----------------:   |
| Block                     | [Link](#block)       |
| Rectangle                 | [Link](#rectangle)   |
| LBlock                    | [Link](#lblock)      |
| SquareBlock               | [Link](#squareblock) |
| TBlock                    | [Link](#tblock)      |
| SBlock                    | [Link](#sblock)      |
| ZBlock                    | [Link](#zblock)      |
| LineBlock                 | [Link](#lineblock)   |
| JBlock                    | [Link](#jblock)      |

---

## Classes

---

## Window

## Init Method

https://github.com/TurtleHelm/AHC-Project/blob/e1bdabbde852ff1835daa4849894cce7a2c3f6c8/Implementation/src/classes.py#L7-L18

### Usage

```python
variable = class Window(window_title:str='Title', bg_color:tuple=(255, 255, 255))
```

### Arguments

- window_title (string, optional): Window Title
- bg_color (tuple, optional): Background Color of Window

---

## Methods

### CreateNewWindow

```python
def CreateNewWindow(self) -> None:
    self.win = game.display.set_mode(size=self.screen_size)
    self.win.fill(self.bg_color)
    game.display.set_caption(self.window_title)
    game.display.set_icon(self.icon)
    game.display.flip()
```

#### Usage

```python
variable.CreateNewWindow()
```

---

### ExitWindow

```python
@staticmethod
def ExitWindow():
    '''Exits the Game'''
    
    from src.utils.ClrTerminal import Color
    game.display.quit()
    Color.printd('Exiting Window...')
    game.quit()
    quit(0)
```

#### Usage

```python
variable.ExitWindow()
```

---

### drawGUIObjs

```python
def drawGUIObjs(self, GUIObjects:list=None) -> None:
    '''Draw GUI Objects to the Screen

    Args:
    - GUIObjects (list, optional): List of Objects. Defaults to None.
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
```

#### Usage

```python
variable.drawGUIObjs(GUIObjects)
```

#### Arguments

- GUIObjects (list): List of Objects to be Drawn to Screen

--- 

### Leave

```python
@staticmethod
def Leave() -> None:
    from .home import run
    run()
```

#### Usage

```python
variable.Leave()
```

---

## Text

### Init Method

```python
def __init__(self, pos:list=[0, 0], text:str='Text', fontsize:int=20, color:tuple=(255, 255, 255)):    
    super().__init__() # Initialise the inherited class
    if not game.font.get_init: game.font.init() # Initialise Font 
    
    self.surface = game.display.get_surface() # Get Window Surface
    self.givenPos = pos
    
    self.color = color
    
    self.fontsize = fontsize
    self.text = game.font.Font('Implementation/src/resources/fonts/font.ttf', self.fontsize).render(text, False, self.color) # Creates Font
    
    self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # Set Position of Text
    self.caption = text
```

#### Usage

```python
variable = Text(pos, text, fontsize, color)
```

#### Arguments

- text (str): Text to be Created
- pos (list): Position of Text on Screen
- fontsize (int): Size of Text
- color (tuple): Color of Text

---

### Methods

#### RenderText

```python
def RenderText(self) -> None:
    pygame.display.get_surface().blit(self.text, self.pos)
    pygame.display.flip()
```

##### Usage

```python
variable.RenderText()
```

---

#### ChangeText

```python
def ChangeText(self, text:str='', draw=None) -> None:    
    self.caption = text
    self.text = game.font.Font('Implementation/src/resources/fonts/font.ttf', self.fontsize).render(self.caption, False, self.color) # Sets new Text
    self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)]
    draw() if draw is not None else self.RenderText()
```

##### Usage

```python
variable.ChangeText(text, draw)
```

##### Arguments

- text (str): Text to be drawn
- draw (method): Draw method

---

#### ChangeColor

```python
def ChangeColor(self, color:tuple=(255, 255, 255)) -> None:
    self.color = color
    self.text = game.font.Font('Implementation/src/resources/fonts/font.ttf', self.fontsize).render(self.caption, False, color) # update text
    self.pos = [self.givenPos[0] - (self.text.get_width() // 2), self.givenPos[1] - (self.text.get_height() // 2)] # update position
    self.RenderText() # Rerender text
```

##### Usage

```python
variable.ChangeColor(color)
```

##### Arguments

- color (tuple): Color to Change Text to

---

#### UpdateText

```python
def UpdateText(self, color:tuple=(255, 255, 255), text:str='') -> None:
    self.ChangeColor(color) # change color to another color
    self.ChangeText(text)
    self.ChangeColor((255, 255, 255)) # change color back to white
```

##### Usage

```python
variable.UpdateText(color, text)
```

##### Arguments

- color (tuple): Color to Update Text With
- text (str): Text to Update To

#### __name__

```python
@staticmethod
def __name__(): return 'Text'
```

##### Usage

```python
variable.__name__()
```

##### Returns

- 'Text' (str)

#### ReturnText

```python
def ReturnText(self): return self.caption
```

##### Usage

```python
variable.ReturnText()
```

##### Returns

- self.caption (str): Raw Text

---

## Btn

### Init Method

```python
def __init__(self, text:str='', pos:list=[0, 0], width:int=113, height:int=41, fontsize:int=16):    
    super().__init__() # initialises default values from inherited class
    
    self.pos = pos
    self.surf = game.display.get_surface()
    self.face = game.Rect(self.pos, (width, height))
    self.face.center = self.pos
    self.hovering = False
    self.fontsize = fontsize
    self.textColor = (255, 255, 255)
    self.text = Text(self.pos, text, self.fontsize, self.textColor)
    self.caption = text
    self.state = False
    self.hoverSound = 'Implementation/src/resources/sounds/hoverSound.wav'
    self.selectSound = 'Implementation/src/resources/sounds/selectSound.wav'
```

#### Usage

```python
variable = class Btn(text, pos, width, height, fontsize)
```

#### Arguments

- text (str): Text for Button
- pos (list): Position of Button
- width (int): Width of Button
- height (int): Height of Button
- fontsize (int): Size of Text

---

### Methods

#### ChangeState

```python
def ChangeState(self, txt:str, boolean:bool) -> None:
    self.state = boolean # Change Clicked State
    self.text.ChangeText(txt, self.RenderBtn) # Change color of text depending on state
```

##### Usage

```python
variable.ChangeState(txt, bool)
```

##### Arguments

- txt (str): Text to be drawn to screen
- boolean (bool): has button changed state

---

#### isHovering

```python
def isHovering(self, click, effectState:bool, color:tuple=(255, 0, 0), *args) -> None:    
    # If mouse is hovering
    if self.face.collidepoint(game.mouse.get_pos()):
        
        # If the button is not already being hovered
        if not self.hovering:
            self.hovering = True # Sets button being hovered to true
            self.text.ChangeColor(color) # Change Text Color
            
            # Sound Effect Volume
            game.mixer.Channel(0).set_volume(.3) if effectState else game.mixer.Channel(0).set_volume(0)
            game.mixer.Channel(0).play(game.mixer.Sound(self.hoverSound)) if effectState else game.mixer.Channel(0).set_volume(0)
            
            self.RenderBtn() # Redraw Button

        # If the button is already being hovered
        else: self.HasClicked(click, *args) # Check if the button has been clicked
        
    # If mouse is not over the button but the button is still being hovered    
    elif not self.face.collidepoint(game.mouse.get_pos()) and self.hovering:
        self.hovering = False # Make sure when not hovered hover is set to false
        self.text.ChangeColor((255, 255, 255)) # Changes button color to white
        self.RenderBtn() # Redraw Button
```

##### Usage

```python
variable.isHovering(click, effectState, color, *args)
```

##### Arguments

- click (method): Click function
- effectState (bool): Sound effect state
- color (tuple): Color to set text to on hover
- *args: Any other value(s) to be passed into the click method

---

#### HasClicked

```python
def HasClicked(self, click, *args) -> None:
    if game.mouse.get_pressed()[0]: # If button has been pressed with left click
        game.mixer.Channel(0).play(game.mixer.Sound(self.selectSound)) # Play select sound
        click() if not args else click(args) # Run Click Method
        
        from time import sleep
        sleep(.3) # Stop multiple clicks being registered
```

##### Usage

```python
variable.HasClicked(click, *args)
```

##### Arguments

- click (method): Click method
- *args: Any value(s) to send to the click method

---

#### RenderBtn

```python
def RenderBtn(self) -> None:
    '''Render Button to Screen'''
    game.draw.rect(game.display.get_surface(), (0, 0, 0), self.face) # Render button rect
    self.text.RenderText() # Render button text
```

##### Usage

```python
variable.RenderBtn()
```

---

#### __name__

```python
def __name__(): return 'Btn'
```

##### Usage

```python
variable.__name__()
```

##### Returns

- 'Btn' (str)

---

# Game

### Usage

```python
variable = class Game()
```

---

# GridRect

## Init Method

```python
def __init__(self, pos, size): # initialise values
    super().__init__() # initialise default values from inherited class
    self.posX, self.posY = pos
    self.size = size
    self.color = (200, 200, 200)
    self.rect = game.Rect(self.posX, self.posY, self.size, self.size)
    self.image = game.Surface([self.size, self.size])
```

### Usage

```python
variable = class GridRect(pos, size)
```

### Arguments

- pos (tuple): Position of Grid Rectangle
- size (tuple): Size of Grid Rectangle (x, y)

---

## Methods

### drawRect

```python
def drawRect(self, screen):    
    pygame.draw.rect(screen, self.color, self.rect, 1)
```

#### Arguments

- self (Text): Instance of Class
- screen (pygame.Surface): Window to Draw To

---

# Grid

## Init Method

```python
def __init__(self, gridPos:tuple, totalGridSize:tuple=(630, 700)): # initialise values           
    self.posX = gridPos[0]
    self.posY = gridPos[1]
    self.blockSize = 30
    self.gridX = totalGridSize[0]
    self.gridY = totalGridSize[1]
    self.gridGroup = game.sprite.Group()
```

### Usage

```python
variable = class Grid(gridPos, totalGridSize)
```

### Arguments

- gridPos (tuple): Position to start drawing grid from (x, y)
- totalGridSize (tuple): Total Width & Height of the Grid

---

## Methods

### DrawGrid

```python
    def DrawGrid(self, screen) -> None:        
        # for horizontal grid blocks, starting & ending at limits with each step being of size blockSize
        for x in range(self.posX, self.gridX, self.blockSize): 
            # for vertical grid blocks, starting & ending at limits with each step being of size blockSize
            for y in range(self.posY, self.gridY, self.blockSize): 
                # create a GridRect instance, add it to gridGroup & draw it to the screen
                gridBlock = GridRect((x, y), self.blockSize)
                self.gridGroup.add(gridBlock)
                gridBlock.drawRect(screen)
```

#### Arguments

- screen (pygame.Surface): Window to Draw To

---

# Settings

## Init Method

```python
def __init__(self, musicState:bool=True, effectState:bool=True) -> None:
    self.musicState = musicState
    self.effectState = effectState
    self.filePath = 'Implementation/settings.txt'
```

### Usage

```python
variable = class Settings(musicState, effectState)
```

### Arguments

- musicState (bool): Allow Music or not
- effectState (bool): Allow Sound Effects or not

---

## Methods

### init

```python
def init(self) -> None:
    '''Get Settings from File'''
    
    import os.path
    
    if not os.path.isfile(self.filePath): self.WriteSettings(False) # create the settings file if it does not exist

    else: # Otherwise
        with open(self.filePath) as f: # Open the file
            settings = f.read().split(',') # Split values by comma

        self.musicState = True if settings[0] == 'True' else False # Set the music state to true if the settings value is true
        self.effectState = True if settings[1] == 'True' else False # Set the sound effects state to true if the settings value is true  
```

#### Usage
```python
variable.init()
```

---

### WriteSettings

```python
def WriteSettings(self, rem:bool=False) -> None:
    '''Write Settings to Settings file

    Args:
    - rem (bool, optional): remove file if True. Defaults to False
    '''
    
    from os import remove
    if rem: remove(self.filePath) # if we set rem to True, remove settings file
        
    with open(self.filePath, 'w') as f: # open settings file as write
        f.write(f'{str(self.musicState)},') # write new musicState value to file
        f.write(f'{str(self.effectState)}') # write new effectState value to file
        f.close() # close file
        
    self.init() # re-initialise settings
```

#### Usage

```python
variable.WriteSettings(rem)
```

#### Arguments

- rem (bool): Remove current settings file if it exists

---

### ChangeSettings

```python
def ChangeSettings(self, musicBool=None, effectsBool=None) -> None:    
    self.musicState = musicBool if musicBool != None else self.musicState # ternary operation
    self.effectState = effectsBool if effectsBool != None else self.effectState # ternary operation
    self.WriteSettings(True)
```

#### Usage

```python
variable.ChangeSettings(musicBool, effectsBool)
```

#### Arguments

- musicBool (bool): bool to change musicState to
- effectsBool (bool): bool to change effectState to

---

# Highscore

## Init Method

```python
def __init__(self, name='PLA', score=0):    
    self.name = name
    self.score = score
```

### Usage

```python
variable = class Highscore(name, score)
```

### Arguments

- name (str): Name of User
- score (int): Score achieved by User

---

## Methods

### BubbleSortScores

```python
def BubbleSortScores(self, scoreList:list, dev:bool=False) -> list[list]: 
    if self.name != 'PLA' and self.score != 0:
        scoreList.append(Highscore(self.name, self.score))
    
    for i in range(len(scoreList)):
        for j in range (len(scoreList)-i-1):
            if scoreList[j+1].score > scoreList[j].score:
                scoreList[j], scoreList[j+1] = scoreList[j+1], scoreList[j]

    return [[score.name, score.score] for score in scoreList[:5]] if not dev else [[score.name, score.score] for score in scoreList]
```

#### Usage

```python
variableTwo = variable.BubbleSortScores(scoreList, dev)
```

#### Arguments

- scoreList (list): List of Scores to Sort
- dev (bool): Developer Mode, return all scores not just 5

#### Returns

- scores (list[list]): list of scores in the form [name, score]

---

### GetScoresFromFile

```python
@staticmethod
def GetScoresFromFile(filePath:str) -> list:    
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
```

#### Usage

```python
variableTwo = variable.GetScoresFromFile(filePath)
```

#### Arguments

- filePath (str): Path to scores file

#### Returns

- highscores (list): List of Highscore Objects in the form Highscore(name, score)

---

### WriteScoresToFile

```python
@staticmethod
def WriteScoresToFile(filePath:str, scores:list) -> bool:
    '''
        Writes Scores to File Passed in\n
        Return(s):
            - True if Success
            - False if Error
    '''

    from .utils.ClrTerminal import Color
    
    try:
        with open(filePath, 'w') as f:
            for score in scores: f.write(f'{score.name},{score.score},')
            
        Color.prints(f'Successfully written scores to {filePath}')   
        return True

    except Exception as e: 
        Color.printe(f'Unexpected Error occurred whilst writing scores to {filePath}\n{e}')
        return False
```

#### Usage

```python
variable.WriteScoresToFile(filePath, scores)
```

#### Arguments

- filePath (str): File path to scores file to write to
- scores (list): Scores to write to file

#### Returns

- bool: True if successful, False if unsuccessful

---

### CommitToDb

```python
@staticmethod
def CommitToDb(scores:list) -> list[tuple]:
    from .utils.ClrTerminal import Color
    import pyodbc as dbc
    
    topScores = []
    
    scores = scores[0] # Remove from args tuple
    
    try:
        # Connection string for SQL Server
        conn_str = f'''
        DRIVER=SQL SERVER;
        SERVER={SERVERNAME};
        DATABASE={DBNAME};
        Trust_Connection=yes;
        '''

        # Establish Connection & create cursor
        conn = dbc.connect(conn_str)
        cursor = conn.cursor()
        
        cursor.execute('TRUNCATE TABLE highscore;') # Clear out existing data in 'highscore' table
        
        # define insert query
        ins_query = f'''INSERT INTO highscore (name, score) VALUES (?, ?);'''
        
        # iterate over scores list & insert each score into database
        for name, score in scores: cursor.execute(ins_query, (name, score))
            
        # commit changes to db & print success msg
        conn.commit() 
        Color.prints('Committed Data to Database Successfully')
    
        # Attempt to retrieve score data
        try:
            data = cursor.execute('SELECT * FROM highscore;')
        
            # iterate over retrieved data & append each row to topScores
            topScores = [(name, score) for name, score in data]
            
            # print success msg
            Color.prints('Successfully retrieved score data from database')
            
            conn.close() # closes connection to db
            
            Color.prints(f'Data: {topScores}')
            return topScores # return the top scores that were retrieved (if any)
        
        # If there was an error retrieving the data, print an error message
        except Exception as e: Color.printe(f'Error whilst trying to retrieve score data\n{e}')
    
    # If there was an error committing data to the database, print an error message
    except Exception as e: Color.printe(f'Error: There was an unexpected error whilst trying to commit data to the sql database\n{e}')
```

#### Usage

```python
variableTwo = variable.CommitToDb(scores)
```

#### Arguments

- scores (list): Scores to Commit to Database

#### Returns

- list[tuple]: List of tuples containing (name, score) for each entry in database

---

# Subclasses

## Block

## Init Method

```python
def __init__(self, struct, color): # Initialise Values    
    super().__init__()
    self.struct = struct
    self.color = color
    self.realPos = [450, 100]
    self.blockSize = 30
    self.group = game.sprite.Group()
```

### Usage

```python
variable = class Block(struct, color)
```

### Arguments

- struct (tuple): Shape of Block
- color (tuple): Color of Block
- pos (list): Position to Draw Block at

---

## Methods

### GetRandBlock

```python
@staticmethod
def GetRandBlock():    
    from random import choice
    return choice((Game.LBlock, Game.SquareBlock, Game.TBlock, Game.SBlock, Game.ZBlock, Game.LineBlock, Game.JBlock))() # Returns Random Block
```

#### Usage

```python
variableTwo = variable.GetRandBlock()
```

#### Returns

- Type of Block

---

### draw

```python
def draw(self, screen) -> None:
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
```

#### Usage

```python
variable.draw(screen)
```

#### Arguments

- screen (pygame.Surface): Window to Draw to

---

### Move

```python
def Move(self, screen, dir, dirName) -> None:    
    self.UpdateColor((0, 0, 0), screen) # Update color of previous blocks
    self.group.empty() # empty sprite group
    self.group.update(dir) # draw new block at new location (gives impression of movement)
    
    match dirName: # check for direction of travel
        case 'left': self.realPos[0] -= 30
        case 'right': self.realPos[0] += 30
        case 'down': self.realPos[1] += 30
        
    Game.Block.draw(self, screen) # draw new block to screen
```

#### Usage

```python
variable.Move(screen, dir, dirName)
```

#### Arguments

- screen (pygame.Surface): Surface to be Drawn to
- dir (tuple): How far to move block
- dirName (str): Direction of Travel

---

### CheckCollision

```python
def CheckCollision(self, blockGroup) -> bool:
    for i in range(len(blockGroup.sprites())):
        if self == blockGroup.sprites()[i]: continue
        else: 
            for j in range(len(self.group.sprites())):                        
                if Game.Block.WillCollide(self.group.sprites()[j], blockGroup.sprites()[i].group): # still causes issues with collision but it doesn't crash now
                        return True

    for i in range(len(self.group.sprites())): 
        if self.group.sprites()[i].posY == 670: return True

    return False
```

#### Usage

```python
variableTwo = variable.CheckCollision(blockGroup)
```

#### Arguments

- blockGroup (pygame.sprite.Group): Group to check for collisions against

#### Returns

- bool: If Collided

---

### WillCollide

```python
@staticmethod
def WillCollide(sprite, group) -> bool:    
    import copy
    spriteRect = copy.copy(sprite.rect)
    spriteRect.move_ip((0, 30))
    
    for i in range(len(group)):
        if spriteRect.colliderect(group.sprites()[i].rect):
            return True
        
    return False
```

#### Usage

```python
variableTwo = variable.WillCollide(sprite, group)
```

#### Arguments

- sprite (pygame.Sprite): Sprite to check for collisions with
- group (pygame.sprite.Group): Group to check for collisions against

#### Returns

- bool: Whether or not a sprite is about to collide with a group

---

### CheckMovable

```python
def CheckMovable(self, dir:str) -> bool:    
    if dir == 'right':
        for i in range(len(self.group.sprites())):
            if self.group.sprites()[i].posX == 600: return False
        return True
    
    if dir == 'left':
        for i in range(len(self.group.sprites())):
            if self.group.sprites()[i].posX == 360: return False
        return True
```

#### Usage

```python
variableTwo = variable.CheckMovable(dir)
```

#### Arguments

- dir (str): Direction of Travel

#### Returns

- Bool: If the block is movable

---

### UpdateColor

```python
def UpdateColor(self, color, screen) -> None: # Temp fix for screen flashing    
    originalColor = self.color # store original color
    self.color = color # set new color
    self.draw(screen) # draw new colored block to screen
    self.color = originalColor # set color back to original color
```

#### Usage

```python
variable.UpdateColor(color, screen)
```

#### Arguments

- color (tuple): Color to draw sprite with
- screen (pygame.Surface): Surface to be drawn to

---

### Rotate

```python
def Rotate(self, screen, effectState, sound) -> None:    
    if not isinstance(self, Game.SquareBlock): # check if the block is not square, if its not square continue
        if self.CheckMovable('right') and self.CheckMovable('left'): # temp fix for bugging through grid walls
            if effectState: game.mixer.Channel(0).play(sound)
            self.UpdateColor((0, 0, 0), screen) # update color of previous block
            
            from numpy import rot90
            self.struct = rot90(self.struct) # rotate array 90 degrees clockwise
            self.draw(screen) # redraw new block positions
```

#### Usage

```python
variable.Rotate(screen, effectState, sound)
```

#### Arguments

- screen (pygame.Surface): Surface to be drawn to
- effectState (bool): Sound Effects Bool
- sound (str): File Path to Sound File

---

### reachedTop

```python
@staticmethod
def reachedTop(blockGroup) -> bool:    
    for sprite in blockGroup:
        for block in sprite.group:
            if block.posY == 130: return True
    return False
```

#### Usage

```python
variableTwo = variable.reachedTop(blockGroup)
```

#### Arguments

- blockGroup (pygame.sprite.Group): Group of Sprites to Check for Collision With

#### Returns

- bool: Whether or not the group has reached the top

---

## Rectangle

## Init Method

```python
def __init__(self, pos, color, size):    
    super().__init__() # get values from inherited class
    self.posX, self.posY = pos
    self.size = size
    self.color = color
    self.rect = game.Rect(self.posX, self.posY, self.size, self.size)
    self.image = game.Surface([self.size, self.size])
    self.image.fill(self.color) # fill rect with appropriate color
```

### Usage

```python
variable = class Rectangle(pos, color, size)
```

### Arguments

- pos (tuple): Position of the Rectangle
- color (tuple): color of Rectangle
- size (int): size of Rectangle

---

## Methods

### update

```python
def update(self, dir): self.rect.move_ip(dir) # update position of rect
```

#### Usage

```python
variable.update(dir)
```

#### Arguments

- dir (tuple): Direction of Travel (x, y)

---

## LBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0), (1, 0, 0), (1, 1, 1)), (255, 165, 0))
```

### Usage

```python
variable = class LBlock()
```

---

## SquareBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0), (1, 1, 0), (1, 1, 0)), (255, 255, 0))
```

### Usage

```python
variable = class SquareBlock()
```

---

## TBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0), (0, 1, 0), (1, 1, 1)), (128, 0, 128))
```

### Usage

```python
variable = class TBlock()
```

---

## SBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0), (0, 1, 1), (1, 1, 0)), (0, 128, 0))
```

### Usage

```python
variable = class SBlock()
```

---

## ZBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0), (1, 1, 0), (0, 1, 1)), (128, 0, 0))
```

### Usage

```python
variable = class ZBlock()
```

---

## LineBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0)), (0, 255, 255))
```

### Usage

```python
variable = class LineBlock()
```

---

## JBlock

## Init Method

```python
def __init__(self): super().__init__(((0, 0, 0), (0, 0, 1), (1, 1, 1)), (0, 0, 255))
```

### Usage

```python
variable = class JBlock()
```

---
