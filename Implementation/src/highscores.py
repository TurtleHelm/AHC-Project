# Import necessary classes and modules
from .classes import Window, Text, Highscore, Btn, Settings
from .game import GameRun
import pygame as game
from pathlib import Path

game.init()
game.event.set_allowed([game.QUIT])

clock, settings = (game.time.Clock(), Settings()) # Games Clock (Frames Per Second)

def InitialiseGUI(name, score) -> list:
    scores = []
    
    GUIObjects = [Text([480, 90], 'Netris', 106),
                  Btn('Main Menu', [720, 600], 300, 48, 32),
                  Btn('New Game', [240, 600], 300, 48, 32)]
    
    userScore = Highscore(name, score)
    scores = userScore.BubbleSortScores(userScore.GetScoresFromFile(f'{str(Path(__file__).parents[1])}\\scores.txt'))
    userScore.WriteScoresToFile(f'{str(Path(__file__).parents[1])}\\scores.txt', scores)
    
    scores = scores[:5] # Limit scores to top 5
    
    height = 140
    
    for i in range(len(scores)):
        height+=60
        GUIObjects.append(Text([480, height], f'{scores[i][0]}: {scores[i][1]}', 36))
    
    GUIObjects.append(Text([480, height+80], 'HIGHSCORE!' if score >= scores[0][1] else '', 36))

    return GUIObjects

def RunHighscore(user=('PLA', 0)):
    """Change to the Highscore Page

    Args:
    - name (str, optional): name of user. Defaults to 'BBB'.
    - score (int, optional): score of user. Defaults to 0.
    """
        
    name, score = user
        
    settings.init()
    GUIObjects = InitialiseGUI(name, score)

    win = Window('Netris - Highscores', (0, 0, 0))
    win.CreateNewWindow()

    win.drawGUIObjs(GUIObjects)

    while 1:
        
        GUIObjects[1].isHovering(win.Leave, settings.effectState) # Check if the exit game button is clicked & exit the game
        GUIObjects[2].isHovering(GameRun, settings.effectState) # Check if the exit game button is clicked & exit the game
        
        # Check for keyboard input
        for event in game.event.get():
            
            # If exit button is clicked (top right of window), exit
            if event.type == game.QUIT: win.ExitWindow()
                    
        game.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS