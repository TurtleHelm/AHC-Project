# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings, Highscore, Grid, Game
from .instructions import InstructionsRun
from .highscores import RunHighscore
from .settings import SettingsRun
from .scoreInput import InputRun
from .game import GameRun
import pygame as game

# Initialize Pygame
game.init()
game.event.set_allowed([game.QUIT]) # limit event checks

# Create the games clock and settings objects
clock, settings = (game.time.Clock(), Settings())

# List of GUI Objects
GUIObjects = [
    Text([480, 60], 'Admin Window <Holy Code Batman!>', 28),
    
    Btn('New Game', [160, 150], 260, 41, 32),
    Text([460, 150],'- Game Window', 24),
    
    Btn('Instructions', [220, 200], 400, 41, 32),
    Text([680, 200], '- Instructions Window', 24),
    
    Btn('Settings', [160, 250], 260, 41, 32),
    Text([500, 250],'- Settings Window', 24),
    
    Btn('Score Input', [205, 300], 320, 41, 32),
    Text([650, 300],'- Score Input Window', 24),
    
    Btn('Highscore', [170, 350], 300, 31, 32),
    Text([550, 350], '- Highscore Window', 24),
    
    Btn('SimDB', [105, 400], 180, 31, 32),
    Text([450, 400], '- Simulate DB Commit', 24)
]

def FillHighscore(scores, highscoreWin):
    
    height = 450

    for name, score in scores:
        height += 20
        highscoreWin.append(Text([100, height], f'{name}: {score}', 12))

def DevRun():
    """Change to Developer Window"""

    highscoreWin = []

    devUser = Highscore('DEV', 10000)
    scores = devUser.BubbleSortScores(devUser.GetScoresFromFile('Implementation/scores.txt'))
    
    settings.init()

    win = Window('Netris - Dev Window', (0, 0, 0))
    win.CreateNewWindow()
    
    FillHighscore(scores, highscoreWin)
    win.drawGUIObjs(highscoreWin)
    win.drawGUIObjs(GUIObjects)

    blockTest = Game.Block.GetRandBlock()
    blockTest.realPos = [500, 630]
    blockTest.draw(win.win)

    
    gridTest = Grid((500, 630))
    gridTest.DrawGrid(win.win)    

    while 1:
        
        GUIObjects[1].isHovering(GameRun, settings.effectState)
        GUIObjects[3].isHovering(InstructionsRun, settings.effectState)
        GUIObjects[5].isHovering(SettingsRun, settings.effectState)
        GUIObjects[7].isHovering(InputRun, settings.effectState, (255, 0, 0), 0)
        GUIObjects[9].isHovering(RunHighscore, settings.effectState, (255, 0, 0), 'DEV', 10000)
        GUIObjects[11].isHovering(devUser.CommitToDb, settings.effectState, (255, 0, 0), scores)

        # Check for keyboard input
        for event in game.event.get():
            if event.type == game.QUIT: win.ExitWindow()
            if event.type == game.KEYDOWN and event.key == game.K_ESCAPE:
                from .home import run
                run()

        game.display.update()
        clock.tick(30)