# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings, Highscore, Grid, Game
from .instructions import InstructionsRun
from .highscores import RunHighscore
from .settings import SettingsRun
from .scoreInput import InputRun
from .game import GameRun
from pathlib import Path
import pygame as game

# NOTE: This page is specifically for testing & has NOT been designed prior to creation.
# anything on this page could lead to unexpected errors

game.init() # Initialize Pygame
game.event.set_allowed([game.QUIT]) # limit event checks
clock, settings = (game.time.Clock(), Settings()) # Create the games clock and settings objects

GUIObjects = [ # List of GUI Objects
    Text([480, 60], 'Admin Window <Holy Code Batman!>', 28), # Title
    Btn('New Game', [160, 150], 260, 41, 32), # New Game Btn
    Text([460, 150],'- Game Window', 24), # New Game Btn Desc
    Btn('Instructions', [220, 200], 400, 41, 32), # Instructions Btn
    Text([680, 200], '- Instructions Window', 24), # Instructions Btn Desc
    Btn('Settings', [160, 250], 260, 41, 32), # Settings Btn
    Text([500, 250],'- Settings Window', 24), # Settings Btn Desc
    Btn('Score Input', [205, 300], 320, 41, 32), # Score Input Btn
    Text([650, 300],'- Score Input Window', 24), # Score Input Desc
    Btn('Highscore', [170, 350], 300, 31, 32), # Highscore Btn
    Text([550, 350], '- Highscore Window', 24), # Highscore Btn Desc
    Btn('SimDB', [105, 400], 180, 31, 32), # SimDB Btn
    Text([450, 400], '- Simulate DB Commit', 24), # SimDB Btn Desc
]

def FillHighscore(scores, highscoreWin) -> None:
    '''Fills Miniature Highscore Table with Data
    
    Args:
    - scores (list): List of Highscore Objects
    - highscoreWin (array): Array of Text Objects for the Highscore Table
    '''
    
    height = 450 # Initial Height
    for name, score in scores: # For each name & score in each object
        height += 20 # decrease height
        highscoreWin.append(Text([100, height], f'{name}: {score}', 12)) # Create new Text Object with name & score info, then append to highscore table array

def DevRun():
    """Change to Developer Window"""

    highscoreWin = [] # Highscore Table 

    devUser = Highscore('DEV', 10000) # Create fake user with super high score
    scores = devUser.BubbleSortScores(devUser.GetScoresFromFile(f'{str(Path(__file__).parents[1])}\\scores.txt')) # Get list of highscore objects & sort them
    
    settings.init() # Initialise Settings

    win = Window('Netris - Dev Window', (0, 0, 0)) # Initialise Window Object
    win.CreateNewWindow() # Create New Window
    
    FillHighscore(scores, highscoreWin) # Create Highscore Table from Data
    win.drawGUIObjs(highscoreWin) # Draw Highscore Table to Screen
    win.drawGUIObjs(GUIObjects) # Draw Initial GUI Objects to Screen

    blockTest = Game.Block.GetRandBlock() # Generate Test Block
    blockTest.realPos = [500, 630] # Set Test Block Position
    blockTest.draw() # Draw Test Block

    gridTest = Grid((500, 630)) # Create Test Grid @ a Specific Position
    gridTest.DrawGrid() # Draw Test Grid

    while 1: # Game Loop
        
        # Check Hover Events
        GUIObjects[1].isHovering(GameRun, settings.effectState)
        GUIObjects[3].isHovering(InstructionsRun, settings.effectState)
        GUIObjects[5].isHovering(SettingsRun, settings.effectState)
        GUIObjects[7].isHovering(InputRun, settings.effectState, (255, 0, 0), 0)
        GUIObjects[9].isHovering(RunHighscore, settings.effectState, (255, 0, 0), 'DEV', 1000000)
        GUIObjects[11].isHovering(devUser.CommitToDb, settings.effectState, (255, 0, 0), scores)
        
        for event in game.event.get(): # Check for keyboard input
            if event.type == game.QUIT: win.ExitWindow() # if exit event, quit program
            if event.type == game.KEYDOWN and event.key == game.K_ESCAPE: # if key down & key is escape
                from .home import run 
                run() # Navigate back to home

        game.display.update() # Update screen
        clock.tick(30) # Limit window to 30 FPS