from enum import Enum
from datetime import datetime

class Logging(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    INFO = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def _log_to_file(cls, log_type, message):
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        log_filename = f"logs/disdrm_log_{current_time.strftime('%Y-%m-%d')}.txt"
        log_message = f"{timestamp} [{log_type}] {message}\n"
        with open(log_filename, "a") as log_file:
            log_file.write(log_message)

    @classmethod
    def log_error(cls, message: str, error_type: str,
                   is_print: bool):
        cls._log_to_file('FAIL', message)
        if is_print:
            print(f"{cls.FAIL.value}[ERROR]{cls.ENDC.value} {message}")

    @classmethod
    def log_warning(cls, message: str, is_print: bool):
        cls._log_to_file('WARNING', message)
        if is_print:
            print(f"{cls.WARNING.value}[WARNING]{cls.ENDC.value} {message}")

    @classmethod
    def log_info(cls, message: str, is_print: bool = False):
        cls._log_to_file('INFO', message)
        if is_print:
            print(f"{cls.INFO.value}[INFO]{cls.ENDC.value} {message}")
    

