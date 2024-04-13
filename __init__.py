import os
import ctypes
import shutil

from importlib import util
from modules.errors.errors import Logging
from modules.config.parser import JsonParser

__VERSION__ = 1.0
__CONFIG__ = "config.json"

__PATHS__ = [
    "modules",
    "modules/discord",
    "modules/errors",
    "logs"
]

__MODS__ = [
   'httpx',
   'fade'
]

__WHITELIST__ = [
    'random',
    'threading'
]

@lambda _: _()
class _():

    def __init__(self) -> None:
        Logging.log_info("Starting Disdrm tasks")
        for modules in [self.config_check, self.clear_console, self.check_paths, self.remove_pycache, self.mods]:
            run_task: modules = modules()
            if run_task:
                exit(-1)

    def title(self) -> None:
        ctypes.windll.kernel32.SetConsoleTitleW(f'DisRDM | v{__VERSION__}') # type: ignore
        Logging.log_info("Set console title")
    
    def clear_console(self) -> None:
        if os.name != 'nt':
            os.system('clear')
        else:
            self.title()
            os.system('cls')
        Logging.log_info("Cleared console")

    def check_paths(self) -> None:
        Logging.log_info("Checking module paths")
        for path in __PATHS__:
            if not os.path.exists(path):
                os.mkdir(path)

    def mods(self) -> None:
        Logging.log_info("Checking installed pip modules")
        for mod in __MODS__:
            if mod not in __WHITELIST__:
                detected = util.find_spec(mod)
                if detected is None:
                    Logging.log_error(f"Please install pip module '{mod}'", 'PipMod', is_print=True)
                    return True

    def remove_pycache(self) -> None:
        base_directory = os.path.dirname(__file__)
        for root, dirs, files in os.walk(base_directory):
            for name in dirs:
                if name == "__pycache__":
                    pycache_path = os.path.join(root, name)
                    try:
                        shutil.rmtree(pycache_path)
                    except OSError as e:
                        Logging.log_error(f"Failed to remove __pycache__ at {pycache_path}: {e}", '__pycache__', is_print=True)
                        

    def config_check(self) -> None:
        config: bool = os.path.isfile(__CONFIG__)
        if not config:
            Logging.log_error(f"Failed to grab config '{__CONFIG__}'", 'ConfigError')
            return True
    
