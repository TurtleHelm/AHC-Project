class Color:

    # Foreground Colors
    FORE_BLACK = '\x1b[30m'
    FORE_RED = '\x1b[31m'
    FORE_GREEN = '\x1b[32m'
    FORE_YELLOW = '\x1b[33m'
    FORE_BLUE = '\x1b[34m'
    FORE_MAGENTA = '\x1b[35m'
    FORE_CYAN = '\x1b[36m'
    FORE_WHITE = '\x1b[37m'
    FORE_ORANGE = '\x1b[38;5;208m'

    # Background Colors
    BACK_BLACK = '\x1b[40m'
    BACK_RED = '\x1b[41m'
    BACK_GREEN = '\x1b[42m'
    BACK_YELLOW = '\x1b[43m'
    BACK_BLUE = '\x1b[44m'
    BACK_MAGENTA = '\x1b[45m'
    BACK_CYAN = '\x1b[46m'
    BACK_WHITE = '\x1b[47m'

    RESET = '\033[0m'

    def ClrPrint(clr:str='white'.lower(), txt:str='', isBack:bool=False, reset:bool=True) -> None:
        '''Prints Colored Text to the Terminal & Specifies '''
        
        match clr:
            case 'white': print(f'{Color.BACK_WHITE if isBack else Color.FORE_WHITE}{txt}{Color.RESET if reset else ""}')
            case 'black': print(f'{Color.BACK_BLACK if isBack else Color.FORE_BLACK}{txt}{Color.RESET if reset else ""}')
            case 'red': print(f'{Color.BACK_RED if isBack else Color.FORE_RED}{txt}{Color.RESET if reset else ""}')
            case 'green': print(f'{Color.BACK_GREEN if isBack else Color.FORE_GREEN}{txt}{Color.RESET if reset else ""}')
            case 'yellow': print(f'{Color.BACK_YELLOW if isBack else Color.FORE_YELLOW}{txt}{Color.RESET if reset else ""}')
            case 'blue': print(f'{Color.BACK_BLUE if isBack else Color.FORE_BLUE}{txt}{Color.RESET if reset else ""}')
            case 'magenta': print(f'{Color.BACK_MAGENTA if isBack else Color.FORE_MAGENTA}{txt}{Color.RESET if reset else ""}')
            case 'cyan': print(f'{Color.BACK_CYAN if isBack else Color.FORE_CYAN}{txt}{Color.RESET if reset else ""}')
            case 'orange': print(f'{"" if isBack else Color.FORE_ORANGE}{txt}{Color.RESET if reset else ""}')
        
        
        # if not isBack: # If the Back is set as False (Default)
            
        #     match clr: # Checks for the color name    
                
        #         case 'white': print(f'{Color.Fore.WHITE}{txt}{Color.RESET if reset else ""}')
        #         case 'black': print(f'{Color.Fore.BLACK}{txt}{Color.RESET if reset else ""}')
        #         case 'red': print(f'{Color.Fore.RED}{txt}{Color.RESET if reset else ""}')
        #         case 'green': print(f'{Color.Fore.GREEN}{txt}{Color.RESET if reset else ""}')
        #         case 'yellow': print(f'{Color.Fore.YELLOW}{txt}{Color.RESET if reset else ""}')
        #         case 'blue': print(f'{Color.Fore.BLUE}{txt}{Color.RESET if reset else ""}')
        #         case 'magenta': print(f'{Color.Fore.MAGENTA}{txt}{Color.RESET if reset else ""}')
        #         case 'cyan': print(f'{Color.Fore.CYAN}{txt}{Color.RESET if reset else ""}')
        #         case 'orange': print(f'{Color.Fore.ORANGE}{txt}{Color.RESET if reset else ""}')
        #         case _: print(txt)

        # else: # If The Back is set as True
        #     match clr: # Checks for the color name
        #         case 'white': print(f'{Color.Back.WHITE}{txt}{Color.RESET if reset else ""}')
        #         case 'black': print(f'{Color.Back.BLACK}{txt}{Color.RESET if reset else ""}')
        #         case 'red': print(f'{Color.Back.RED}{txt}{Color.RESET if reset else ""}')
        #         case 'green': print(f'{Color.Back.GREEN}{txt}{Color.RESET if reset else ""}')
        #         case 'yellow': print(f'{Color.Back.YELLOW}{txt}{Color.RESET if reset else ""}')
        #         case 'blue': print(f'{Color.Back.BLUE}{txt}{Color.RESET if reset else ""}')
        #         case 'magenta': print(f'{Color.Back.MAGENTA}{txt}{Color.RESET if reset else ""}')
        #         case 'cyan': print(f'{Color.Back.CYAN}{txt}{Color.RESET if reset else ""}')
        #         case _: print(txt)