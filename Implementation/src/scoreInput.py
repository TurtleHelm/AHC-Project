# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from .utils.ClrTerminal import Color
import pygame

# Initialize Pygame
pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.TEXTINPUT]) # Limit event checks

# Create the games clock and settings objects
clock, settings = (pygame.time.Clock(), Settings())

# create list of illegal characters
disallowedKeys = [chr(key) for key in range(0, 255) if not chr(key).isalpha()]

# List of GUI Objects
GUIObjects = [
    Text([480, 90], 'Netris', 106), # Game Title
    Text([480, 210], 'Enter Name', 48), 
    Text([480, 320], 'PLA', 48), # Name Input Display
    Btn('Enter', [480, 440], 300, 48, 48) # Enter Button
]

def InputRun(score:int=0):
    """Change to Name Input Window"""

    # Initialize settings
    settings.init()

    allowedClick = False

    # Create new window obj & set title & background color
    win = Window('Netris - Score Input', (0, 0, 0))
    # Create the window
    win.CreateNewWindow()

    # Draw the GUI objects on the screen
    win.drawGUIObjs(GUIObjects)

    import time
    time.sleep(.3)

    # While the game is running
    while 1:

        from .highscores import RunHighscore
        if allowedClick: 
            # if clicks are allowed, navigate to the highscore page, passing in the name of the user & the score
            GUIObjects[-1].isHovering(RunHighscore, settings.effectState, (255, 0, 0), GUIObjects[2].caption[:3], score)   
        
        else: 
            try:
                # if clicks are disallowed, navigate back to the input page & grey out Enter button
                GUIObjects[-1].isHovering(InputRun, settings.effectState, (128, 128, 128))
            except RecursionError as e:
                Color.printe(f'Error: Stop Pushing the Button!\n{e}')
                win.ExitWindow()

        if len(GUIObjects[2].caption) == 3: allowedClick = True # Only if name is 3 can you move on
        if len(GUIObjects[2].caption) < 3: allowedClick = False # if name is less than 3 do not allow click 
        
        if len(GUIObjects[2].caption) > 3: # if name is over 3, disallow click & set name to 3
            allowedClick = False # disallow clicks
            Color.printe('Exceeded Character Limit')
            GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption[:3])
        
        # Check for keyboard input
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: # if backspace pressed
                    GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption[:-1]) # Remove char from name
            
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if allowedClick: RunHighscore((GUIObjects[2].caption[:3], score))
            
            if event.type == pygame.TEXTINPUT:
                if event.text not in disallowedKeys: 
                    if GUIObjects[2].caption == 'PLA': GUIObjects[2].UpdateText((0, 0, 0), event.text)
                    else: GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption + event.text) # Add char to name
                
                else: Color.printe(f'Error: Illegal Character "{event.text}"')
                  
        pygame.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS