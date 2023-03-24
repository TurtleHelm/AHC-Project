# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from .utils.ClrTerminal import Color
import pygame

pygame.init() # Initialize Pygame
pygame.event.set_allowed([pygame.KEYDOWN, pygame.TEXTINPUT]) # Limit event checks, reduces lag
clock, settings = (pygame.time.Clock(), Settings()) # Create the games clock and settings objects

allowedKeys = [chr(key) for key in range(0, 255) if chr(key).isalpha() and key <= 122] # create list of legal characters

GUIObjects = [ # List of GUI Objects
    Text([480, 90], 'Netris', 106), # Game Title
    Text([480, 210], 'Enter Name', 48), # Subtitle
    Text([480, 320], 'PLA', 48), # Name Input Display
    Btn('Enter', [480, 440], 300, 48, 48) # Enter Button
]

def InputRun(score:int=0):
    """Change to Name Input Window
    
    Args:
    - score (int, optional): Users score, defaults to
    """

    settings.init() # Initialize settings
    allowedClick = False # Dictates whether or not the user has entered a valid name, allowing navigation to the highscores page

    win = Window('Netris - Score Input', (0, 0, 0)) # Create New Window Object
    win.CreateNewWindow() # Create new Window
    win.drawGUIObjs(GUIObjects) # Draw the GUI objects on the screen

    from time import sleep
    sleep(.3) # prevents RecursionError from happening during game loop

    while 1: # game loop
        if allowedClick: # if clicks are allowed
            from .highscores import RunHighscore
            GUIObjects[-1].isHovering(RunHighscore, settings.effectState, (255, 0, 0), GUIObjects[2].caption[:3], score) # navigate to the highscore page, passing in the name of the user & the score
        else: # otherwise
            try: # try to block click
                GUIObjects[-1].isHovering(InputRun, settings.effectState, (128, 128, 128)) # navigate back to the input page & grey out Enter button
            except RecursionError as e: # if recursion error occurs (constantly holding down btn)
                Color.printe(f'Error: Stop Pushing the Button!\n{e}') # error out
                win.ExitWindow() # Exit Program Calmly

        if len(GUIObjects[2].caption) == 3: allowedClick = True # Only if name is 3 can you move on
        if len(GUIObjects[2].caption) < 3: allowedClick = False # if name is less than 3 do not allow click 
        
        if len(GUIObjects[2].caption) > 3: # if name is over 3, disallow click & set name to 3
            allowedClick = False # disallow clicks
            Color.printe('Exceeded Character Limit')
            GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption[:3]) # Set Text to the first 3 characters
        
        for event in pygame.event.get(): # Check for keyboard input
            if event.type == pygame.KEYDOWN: # if key down
                if event.key == pygame.K_BACKSPACE: # if backspace pressed
                    GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption[:-1]) # Remove character from name
            
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # if enter pressed
                    if allowedClick: RunHighscore((GUIObjects[2].caption[:3], score)) # do same function as clicking enter
            
            if event.type == pygame.TEXTINPUT: # check for keyboard input
                if event.text in allowedKeys: # if the character pressed is a legal character
                    if GUIObjects[2].caption == 'PLA': GUIObjects[2].UpdateText((0, 0, 0), event.text) # automatically remove default name on text input
                    else: GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption + event.text) # Add character to name
                
                else: Color.printe(f'Error: Illegal Character "{event.text}"') # print out error
                  
        pygame.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS