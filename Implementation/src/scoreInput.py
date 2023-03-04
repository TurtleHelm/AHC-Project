# Import necessary classes and modules
from src.classes import Text, Btn, Window, Settings
from .utils.ClrTerminal import Color
import pygame as game

# Initialize Pygame
game.init()
game.event.set_allowed([game.KEYDOWN, game.TEXTINPUT]) # Limit event checks

# Create the games clock and settings objects
clock, settings = (game.time.Clock(), Settings())

# create list of illegal characters
disallowedKeys = [chr(key) for key in range(0, 255) if not chr(key).isalpha()]

# List of GUI Objects
GUIObjects = [
    Text([480, 90], 'Netris', 106), # Game Title
    Text([480, 210], 'Enter Name', 48), 
    Text([480, 320], 'PLA', 48), # Users name Input
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

    # While the game is running
    while 1:

        from .highscores import RunHighscore
        if allowedClick: 
            # if clicks are allowed, navigate to the highscore page, passing in the name of the user & the score
            GUIObjects[-1].isHovering(RunHighscore, settings.effectState, (255, 0, 0), GUIObjects[2].caption[:3], score)   
        
        else: 
            # if clicks are disallowed, navigate back to the input page & grey out Enter button
            GUIObjects[-1].isHovering(InputRun, settings.effectState, (128, 128, 128))

        if len(GUIObjects[2].caption) == 3: # Only if name is 3 can you move on
            allowedClick = True # allow clicks

        if len(GUIObjects[2].caption) < 3: allowedClick = False # if name is less than 3 do not allow click 
        
        if len(GUIObjects[2].caption) > 3: # if name is over 3, disallow click & set name to 3
            allowedClick = False # disallow clicks
            Color.printe('Exceeded Character Limit')
            GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption[:3])
        
        # Check for keyboard input
        for event in game.event.get():
            
            if event.type == game.KEYDOWN:
                if event.key == game.K_BACKSPACE: # if backspace pressed
                    GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption[:-1]) # Remove char from name
            
                if event.key == game.K_RETURN or event.key == game.K_KP_ENTER:
                    if allowedClick: RunHighscore(GUIObjects[2].caption[:3], score[0])
            
            if event.type == game.TEXTINPUT:
                if event.text not in disallowedKeys: GUIObjects[2].UpdateText((0, 0, 0), GUIObjects[2].caption + event.text) # Add char to name
                else: Color.printe(f'Error: Illegal Character "{event.text}"')
                  
        game.display.update() # Update the display
        clock.tick(30) # Set the game's frame rate to 30 FPS