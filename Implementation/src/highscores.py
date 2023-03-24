# Import necessary classes and modules
from .classes import Window, Text, Highscore, Btn, Settings
from .game import GameRun
from pathlib import Path
import pygame

pygame.init() # intialise pygame
pygame.event.set_allowed([pygame.QUIT]) # limits event checks, reduces lag
clock, settings = (pygame.time.Clock(), Settings()) # Games Clock (Frames Per Second)

def InitialiseGUI(name:str, score:int) -> list:
    '''Draw Highscore table from Highscore data in ascending order of score
    
    Args:
    -  name (string): Name of User
    - score (int): Users score
    
    Returns:
    - List: List of top 5 highscores
    '''
    
    scores = [] # array for score data
    
    GUIObjects = [ # initial GUI objects
        Text([480, 90], 'Netris', 106), # Title
        Btn('Main Menu', [720, 600], 300, 48, 32), # Main Menu Button
        Btn('New Game', [240, 600], 300, 48, 32) # New Game Button
    ]
    
    userScore = Highscore(name, score) # Set the users score first
    scores = userScore.BubbleSortScores(userScore.GetScoresFromFile(f'{str(Path(__file__).parents[1])}\\scores.txt')) # Sort scores in order of highest to lowest
    userScore.WriteScoresToFile(f'{str(Path(__file__).parents[1])}\\scores.txt', scores) # Write sorted scores to scores file for future use
    
    scores = scores[:5] # Limit scores to top 5
    height = 140 # initial height to begin drawing the table from
    
    for i in range(len(scores)): # for each score in the scores array
        height += 60 # Move Next text object down
        GUIObjects.append(Text([480, height], f'{scores[i][0]}: {scores[i][1]}', 36)) # append new text object to gui list with name & score
    
    GUIObjects.append(Text([480, height+80], 'HIGHSCORE!' if score >= scores[0][1] else '', 36)) # Append Highscore msg to the end of GUI list if users score is highest

    return GUIObjects # Return GUI list to be rendered

def RunHighscore(user=('PLA', 0)):
    """Change to the Highscore Page

    Args:
    - name (str, optional): name of user. Defaults to 'BBB'.
    - score (int, optional): score of user. Defaults to 0.
    """
        
    settings.init() # initialise settings from file
    GUIObjects = InitialiseGUI(user[0], user[1]) # Call Function above to Initialise the Highscores table

    win = Window('Netris - Highscores', (0, 0, 0)) # create new window object
    win.CreateNewWindow() # create new window
    win.drawGUIObjs(GUIObjects) # Draw GUI objects to screen

    while 1: # game loop
        
        GUIObjects[1].isHovering(win.Leave, settings.effectState) # Check if the exit game button is clicked & exit the game
        GUIObjects[2].isHovering(GameRun, settings.effectState) # Check if new game button is clicked & redirect to new game page
        
        if pygame.event.get(pygame.QUIT): win.ExitWindow() # Exit Window if Top Right X clicked
                    
        pygame.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS