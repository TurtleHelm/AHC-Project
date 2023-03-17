# Import necessary classes and modules
from .classes import Text, Window, Settings, Game, Grid
from src.utils.ClrTerminal import Color
from pathlib import Path
import pygame

pygame.init() # Initialise Pygame
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
clock, settings = (pygame.time.Clock(), Settings()) # Games Clock (Frames Per Second) & Initialise Settings Object

# GUI Objects
GUIObjects = [Text([495, 60], 'Netris', 40),  # Title Text
              Text([173, 144], 'Controls', 32), # Controls Header
              Text([135, 180], '↑ Rotate', 20),
              Text([164, 212], '← Move Left', 20),
              Text([175, 240], '→ Move Right', 20),
              Text([165, 272], '↓ Move Down', 20),
              Text([165, 300], '[Esc] Exit Game', 20),
              Text([800, 144], 'Score', 40), # Score Header
              Text([800, 200], '0', 36)
]

# Sound Effects
rotateBlockSound, lineClearSound, moveBlockSound, scoreSound, failSound = (
    pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\rotateBlock.wav'), 
    pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\lineClear.wav'), 
    pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\moveBlock.wav'),
    pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\scoreSound.wav'),
    pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\failSound.wav')
)

def GameRun():
    
    pygame.mouse.set_visible(False)
    
    Color.printd('Entering Game...')
    
    win = Window('Netris - Game', (0, 0, 0)) # Instantiate Window Object
    win.CreateNewWindow() # Create New Window

    settings.init() # Initialise Settings with settings from settings file

    pygame.mixer.Channel(0).set_volume(.1)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\tetris.mp3'), -1) # Play music in infinite loop
    pygame.mixer.Channel(1).set_volume(.2) if settings.musicState else pygame.mixer.Channel(1).set_volume(0) # if music settings off, then turn off the music otherwise play the music 
    
    block = Game.Block.GetRandBlock() # create initial random block
    block.draw(win.win) # draw block to screen

    speed, mult, score, limit, delay = [0, 1, 0, 500, 0] # initialise speed value
    # prevents overlap of text
    GUIObjects[-1].UpdateText((0, 0, 0), str(score)) # Update Score Count
    
    bottomBlocks = pygame.sprite.Group() # initialise block group

    # Initialise New Game Grid
    grid = Grid(((720 // 2), 100))
    grid.DrawGrid(win.win) # draw grid
    
    win.drawGUIObjs(GUIObjects) # Draw the GUI

    keys = pygame.key.get_pressed() # List of Pressed Keys

    # While the game is running
    while 1: # 1 & not True due to weirdness with True taking up another operation unlike 1

        grid.DrawGrid(win.win) # continually draw grid to screen (stops screen flickering)
        
        match keys:
            case pygame.K_DOWN:
                if delay*mult >= 5:
                    block.Move(win.win, 'down', settings.effectState, moveBlockSound)
                    delay = 0
                    
            case pygame.K_RIGHT:
                if delay >= 5:
                    block.Move(win.win, 'right', settings.effectState, moveBlockSound)
                    delay = 0
                    
            case pygame.K_LEFT:
                if delay >= 5:
                    block.Move(win.win, 'left', settings.effectState, moveBlockSound)
                    delay = 0

        # Check for keyboard input
        for event in pygame.event.get():
            
            # If exit button is clicked (top right of window), exit
            if event.type == pygame.QUIT: win.ExitWindow()
            
            # all keydown events
            if event.type == pygame.KEYDOWN:
                
                # Check for any matches in the key down events
                match event.key:

                    case pygame.K_ESCAPE: # if esc key, return home
                        pygame.mixer.Channel(1).stop()
                        pygame.mouse.set_visible(True)
                        win.Leave()
                    
                    case pygame.K_UP: # if up arrow, rotate
                        block.Rotate(win.win, settings.effectState, rotateBlockSound, bottomBlocks)
                    
                    # case pygame.K_RIGHT: # if right arrow, move right
                    #     # if block.CheckMovable('right', bottomBlocks):
                    #     #     block.Move(win.win, 'right', settings.effectState, moveBlockSound)

                    # case pygame.K_LEFT: # if left arrow, move left
                    #     if block.CheckMovable('left', bottomBlocks):
                    #         block.Move(win.win, 'left', settings.effectState, moveBlockSound)
                    
                    case _: pass # default case
        
        # TODO: Stop auto block movement when down arrow is pressed
        
        if speed*mult >= 30 and not keys[pygame.K_DOWN]: # if 1s has passed (30 ticks per second)
            block.Move(win.win, 'down', settings.effectState, moveBlockSound) # Move the block down by 1 space on the screen
            speed = 0 # reset timer

        if block.CheckCollision(bottomBlocks, 'down'): # if block collision has been detected or the block has reached the bottom of the grid
            bottomBlocks.add(block.group) # add current rect group to block group
            
            block = Game.Block.GetRandBlock()
            block.draw(win.win)
            if settings.effectState: 
                pygame.mixer.Channel(2).set_volume(.2)
                pygame.mixer.Channel(2).play(scoreSound)
            
            score += 50 # add to score value
            if score >= limit: # if score is over a specific value, change the value and increase multiplier
                mult += 1
                limit += 1000

            # prevents overlap of text
            GUIObjects[-1].UpdateText((0, 0, 0), str(score))
            
            if block.reachedTop(bottomBlocks): # check if the block group is at the top of the screen
                Color.prints('Reached Top of Screen')
                from .scoreInput import InputRun
                pygame.mouse.set_visible(True)
                if settings.effectState: pygame.mixer.Channel(0).play(failSound) # play fail sound
                pygame.mixer.Channel(1).stop() # stop music
                InputRun(score) # exit pygame into highscore menu
            
            complete = block.CheckCompletedRow(bottomBlocks, win.win, settings.effectState, lineClearSound)
        
            while complete:
                score += 100
                GUIObjects[-1].UpdateText((0, 0, 0), str(score))
                
                complete = block.CheckCompletedRow(bottomBlocks, win.win, settings.effectState, lineClearSound)

        pygame.display.update()
        clock.tick(30)
        speed += 1
        delay += 1