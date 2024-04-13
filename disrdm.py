import fade

from __init__ import __VERSION__, __CONFIG__
from modules.config.parser import JsonParser
from colorama import Fore, init
from modules.messages.help import HELP_MENU, BANNER
from modules.discord.helper import Helper

class DisRDM:
    @staticmethod
    def display_menu():
        helper_instance = Helper()
        menu_options = {
            "help": lambda: print(HELP_MENU),
            "disact": lambda: helper_instance.activitys(),
            "disound": lambda: helper_instance.soundboard()
        }
        print(fade.fire(BANNER))
        while True:
            user_input = input("›› ")
            if user_input in menu_options:
                menu_options[user_input]()

if __name__ == "__main__":
    
    DisRDM.display_menu()
