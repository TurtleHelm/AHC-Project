from .classes import Window, Text, Highscore
import pygame as game

game.init()
game.event.set_allowed([game.QUIT, game.KEYDOWN])

clock = game.time.Clock() # Games Clock (Frames Per Second)

def Leave():
    from .home import run
    run()

def RunHighscore(score=0):
    scores, topScores = [], []
    
    GUIObjects = [Text([480, 90], 'Netris', 106),
                  Text([480, 200], f'Score: {score}', 48)
]
    
    userScore = Highscore('AAA', 9000)
    scores = userScore.BubbleSortScores(userScore.GetScoresFromFile('scores.txt', scores))
    # topScores = userScore.CommitToDb(scores)
    # print(topScores)

    win = Window('Netris - Highscores', (0, 0, 0))
    win.CreateNewWindow()

    win.drawGUIObjs(GUIObjects)

    while True:
        # Check for keyboard input
        for event in game.event.get():
            
            # If exit button is clicked (top right of window), exit
            if event.type == game.QUIT:
                game.quit()
                quit(0)
            
            # if escape key pressed, exit
            if event.type == game.KEYDOWN:
                
                # Check for any matches in the key down events
                match event.key:
                    # If Esc key
                    case game.K_ESCAPE: Leave()
                    case _: pass
                    
        game.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS