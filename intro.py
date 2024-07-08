from colorama import init, Fore, Style
import time

# Initialize colorama for cross-platform ANSI color support
init(autoreset=True)


def show_splash_screen():
    # ASCII art banner
    print(Fore.RED + r"""
     ██▀███   ▄▄▄      ▓█████▄  ▄▄▄       ██░ ██  ███▄    █ 
▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒████▄    ▓██░ ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██  ▀█▄  ▒██▀▀██░▓██  ▀█ ██▒
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌░██▄▄▄▄██ ░▓█ ░██ ▓██▒  ▐▌██▒
░██▓ ▒██▒ ▓█   ▓██▒░▒████▓  ▓█   ▓██▒░▓█▒░██▓▒██░   ▓██░
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ▒   ▒▒ ░ ▒ ░▒░ ░░ ░░   ░ ▒░
  ░░   ░   ░   ▒    ░ ░  ░   ░   ▒    ░  ░░ ░   ░   ░ ░ 
   ░           ░  ░   ░          ░  ░ ░  ░  ░         ░ 
                    ░                                   
    """ + Style.RESET_ALL)

    print("Version 1.0\n")
    print("Loading...")
    time.sleep(2)  # Simulate initialization delay


# Example usage
if __name__ == "__main__":
    show_splash_screen()
    # Your main program logic follows here
