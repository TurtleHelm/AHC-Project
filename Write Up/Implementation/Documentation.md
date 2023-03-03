# Documentation

## Table

| [Classes](#classes)  | Quick Search       |
| :------------------: | :----------------: |
| Window               | [Link](#window)    |
| Btn                  | [Link](#btn)       |
| Text                 | [Link](#text)      |
| Game                 | [Link](#game)      |
| GridRect             | [Link](#gridrect)  |
| Grid                 | [Link](#grid)      |
| Settings             | [Link](#settings)  |
| Highscore            | [Link](#highscore) |

| [Subclasses](#subclasses) | Quick Search         |
| :-----------------------: | :------------------: |
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

# Classes

---

# Window

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/e1bdabbde852ff1835daa4849894cce7a2c3f6c8/Implementation/src/classes.py#L7-L18>

### Usage

```python
variable = class Window(window_title:str='Title', bg_color:tuple=(255, 255, 255))
```

### Arguments

- window_title (string, optional): Window Title
- bg_color (tuple, optional): Background Color of Window

### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L39-L44>

---

## Methods

### CreateNewWindow

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L20-L27>

#### Usage

```python
variable.CreateNewWindow()
```

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L46-L51>

---

### ExitWindow

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L30-L37>

#### Usage

```python
variable.ExitWindow()
```

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L55-L61>

---

### drawGUIObjs

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L39-L60>

#### Usage

```python
variable.drawGUIObjs(GUIObjects)
```

#### Arguments

- GUIObjects (list): List of Objects to be Drawn to Screen

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L63-L75>

---

### Leave

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L62-L65>

#### Usage

```python
variable.Leave()
```

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L77-L80>

---

# Text

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L70-L97>

### Usage

```python
variable = Text(pos, text, fontsize, color)
```

### Arguments

- text (str): Text to be Created
- pos (list): Position of Text on Screen
- fontsize (int): Size of Text
- color (tuple): Color of Text

### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L88-L98>

---

## Methods

### RenderText

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L99-L102>

#### Usage

```python
variable.RenderText()
```

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L100-L103>

---

### ChangeText

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L104-L115>

#### Usage

```python
variable.ChangeText(text, draw)
```

#### Arguments

- text (str): Text to be drawn
- draw (method): Draw method

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L105-L109>

---

### ChangeColor

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L117-L132>

#### Usage

```python
variable.ChangeColor(color)
```

#### Arguments

- color (tuple): Color to Change Text to

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L111-L116>

---

### UpdateText

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L129-L132>

#### Usage

```python
variable.UpdateText(color, text)
```

#### Arguments

- color (tuple): Color to Update Text With
- text (str): Text to Update To

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L118-L122>

### __name__

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L134-L135>

#### Usage

```python
variable.__name__()
```

#### Returns

- 'Text' (str)

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L124-L126>

---

### ReturnText

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L136>

#### Usage

```python
variable.ReturnText()
```

#### Returns

- self.caption (str): Raw Text

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L128-L130>

---

# Btn

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L141-L175>

### Usage

```python
variable = class Btn(text, pos, width, height, fontsize)
```

### Arguments

- text (str): Text for Button
- pos (list): Position of Button
- width (int): Width of Button
- height (int): Height of Button
- fontsize (int): Size of Text

### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L138-L151>

---

## Methods

### ChangeState

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L177-L186>

#### Usage

```python
variable.ChangeState(txt, bool)
```

#### Arguments

- txt (str): Text to be drawn to screen
- boolean (bool): has button changed state

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L154-L157>

---

### isHovering

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L188-L219>

#### Usage

```python
variable.isHovering(click, effectState, color, *args)
```

#### Arguments

- click (method): Click function
- effectState (bool): Sound effect state
- color (tuple): Color to set text to on hover
- *args: Any other value(s) to be passed into the click method

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L159-L172>

---

### HasClicked

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L159-L179>

#### Usage

```python
variable.HasClicked(click, *args)
```

#### Arguments

- click (method): Click method
- *args: Any value(s) to send to the click method

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L180-L187>

---

### RenderBtn

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L231-L234>

#### Usage

```python
variable.RenderBtn()
```

---

### __name__

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L236-L237>

#### Usage

```python
variable.__name__()
```

#### Returns

- 'Btn' (str)

#### Pseudocode

<https://github.com/TurtleHelm/AHC-Project/blob/3c5d017167fc62ba2480bae3befd9893df2d902a/Write%20Up/Design/Pseudocode%20(Extended).txt#L193-L195>

---

# Game

## Usage

```python
variable = class Game()
```

---

# GridRect

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L478-L499>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L501-L508>

#### Arguments

- self (Text): Instance of Class
- screen (pygame.Surface): Window to Draw To

---

# Grid

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L513-L534>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L537-L551>

#### Arguments

- screen (pygame.Surface): Window to Draw To

---

# Settings

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L556-L566>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L568-L580>

#### Usage

```python
variable.init()
```

---

### WriteSettings

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L582-L595>

#### Usage

```python
variable.WriteSettings(rem)
```

#### Arguments

- rem (bool): Remove current settings file if it exists

---

### ChangeSettings

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L599-L609>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L614-L624>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L626-L644>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L646-L676>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L678-L698>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L700-L758>

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

# Block

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L256-L275>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L245-L254>

#### Usage

```python
variableTwo = variable.GetRandBlock()
```

#### Returns

- Type of Block

---

### draw

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L277-L293>

#### Usage

```python
variable.draw(screen)
```

#### Arguments

- screen (pygame.Surface): Window to Draw to

---

### Move

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L295-L313>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L315-L335>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L337-L357>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L359-L377>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L379-L390>

#### Usage

```python
variable.UpdateColor(color, screen)
```

#### Arguments

- color (tuple): Color to draw sprite with
- screen (pygame.Surface): Surface to be drawn to

---

### Rotate

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L392-L408>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L410-L424>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L429-L450>

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

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L452>

#### Usage

```python
variable.update(dir)
```

#### Arguments

- dir (tuple): Direction of Travel (x, y)

---

## LBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L455>

### Usage

```python
variable = class LBlock()
```

---

## SquareBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L458>

### Usage

```python
variable = class SquareBlock()
```

---

## TBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L461>

### Usage

```python
variable = class TBlock()
```

---

## SBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L464>

### Usage

```python
variable = class SBlock()
```

---

## ZBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L467>

### Usage

```python
variable = class ZBlock()
```

---

## LineBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L470>

### Usage

```python
variable = class LineBlock()
```

---

## JBlock

## Init Method

<https://github.com/TurtleHelm/AHC-Project/blob/81b67e66eb018a168a59b07b1ffccb465f446e85/Implementation/src/classes.py#L473>

### Usage

```python
variable = class JBlock()
```

---
