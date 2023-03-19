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

    # Music Settings
    if settings.effectState:
        pygame.mixer.Channel(0).set_volume(.1)
        pygame.mixer.Channel(2).set_volume(.2)
    else:
        pygame.mixer.Channel(0).set_volume(0)
        pygame.mixer.Channel(2).set_volume(0)
    
    pygame.mixer.Channel(1).set_volume(.2) if settings.musicState else pygame.mixer.Channel(1).set_volume(0)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'{str(Path(__file__).parents[0])}\\resources\\sounds\\tetris.mp3'), -1) # Play music in infinite loop
    
    block = Game.LineBlock() # create initial random block
    block.draw() # draw block to screen
    
    bottomBlocks = pygame.sprite.Group() # initialise block group

    speed, mult, score, limit, delay = [0, 1, 0, 500, 0] # initialise game values (block speed, speed multiplier, score, limit before speed increase, delay for block movement)
    GUIObjects[-1].UpdateText((0, 0, 0), str(score)) # Update Score Count

    grid = Grid(((720 // 2), 100)) # Initialise New Game Grid
    grid.DrawGrid() # draw grid
    
    win.drawGUIObjs(GUIObjects) # Draw the GUI

    while 1: # While the game is running

        keys = pygame.key.get_pressed() # List of Pressed Keys
        grid.DrawGrid() # continually draw grid to screen (stops whole screen flickering) 
        
        # Move Block Automatically for held keys (as long as delay is over)
        if delay >= 5:
            if keys[pygame.K_DOWN]:
                if delay*mult >= 5: # Speeds up as game speeds up
                    block.Move('down', settings.effectState, moveBlockSound)
                    delay = 0
        
            elif keys[pygame.K_RIGHT]:
               if block.CheckMovable('right', bottomBlocks):
                    block.Move('right', settings.effectState, moveBlockSound)
                    delay = 0
                    
            elif keys[pygame.K_LEFT]:
                if block.CheckMovable('left', bottomBlocks):
                    block.Move('left', settings.effectState, moveBlockSound)
                    delay = 0       
        
            elif keys[pygame.K_UP]:
                block.Rotate(settings.effectState, rotateBlockSound, bottomBlocks)               
                delay = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT: win.ExitWindow() # Quit of screen exited
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # Check for Quit event
                pygame.mixer.Channel(1).stop()
                pygame.mouse.set_visible(True)
                win.Leave()

        if speed*mult >= 30 and not keys[pygame.K_DOWN]: # if 1s has passed (30 ticks per second) & down key not held (Stops Phasing through other blocks)
            # block.Move('down', settings.effectState, moveBlockSound) # Move the block down by 1 space on the screen
            speed = 0 # reset timer

        if block.CheckCollision(bottomBlocks, 'down'): # if block collision has been detected or the block has reached the bottom of the grid
            bottomBlocks.add(block.group) # add current rect group to block group
            
            block = Game.Block.GetRandBlock()
            block.draw()
            
            if settings.effectState: pygame.mixer.Channel(2).play(scoreSound)
            
            score += 50 # add to score value
            if score >= limit: # if score is over a specific value, change the value and increase multiplier
                mult += 1 # Increase Speed
                limit += 1000 # Increase Score Limit to 

            # prevents overlap of text
            GUIObjects[-1].UpdateText((0, 0, 0), str(score))
            
            if block.reachedTop(bottomBlocks): # check if the block group is at the top of the screen
                Color.prints('Reached Top of Screen')
                from .scoreInput import InputRun
                pygame.mouse.set_visible(True)
                if settings.effectState: pygame.mixer.Channel(0).play(failSound) # play fail sound
                pygame.mixer.Channel(1).stop() # stop music
                InputRun(score) # exit pygame into highscore menu
            
            complete = block.CheckCompletedRow(bottomBlocks, settings.effectState, lineClearSound)
        
            while complete:
                score += 100
                GUIObjects[-1].UpdateText((0, 0, 0), str(score))
                
                complete = block.CheckCompletedRow(bottomBlocks, settings.effectState, lineClearSound)

        pygame.display.update()
        clock.tick(30)
        speed += 1
        delay += 1