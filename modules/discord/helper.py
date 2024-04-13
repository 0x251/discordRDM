from ..config.parser import JsonParser
from .activitys.activity import spam_activitys
from .soundboard.soundboard import spam_soundboard
from ..errors.errors import Logging
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore


class Helper:
    CONFIG = JsonParser()
    DISCORD_HEADER = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
        "Read-Timeout": "5",
        "Authorization": CONFIG.auth_token(),
        "Content-Type": "application/json",
    }

    @classmethod
    def activitys(cls):
        try:
            Logging.log_warning("Please make sure you read the README.md about sessions, as this method requires a session token!", is_print=True)
            discord_guild: str = input(f"[{Fore.LIGHTBLUE_EX}GuildID{Fore.RESET}] ›› ")
            discord_channel: str = input(f"[{Fore.LIGHTBLUE_EX}ChannelID{Fore.RESET}] ›› ")
            repeat_count: str = input(f"[{Fore.LIGHTBLACK_EX}Spam count{Fore.RESET}] ›› ")

            def spam_activities_thread(discord_channel, discord_guild):
                spam_activitys(discord_header=cls.DISCORD_HEADER, channel_id=discord_channel, guild_id=discord_guild)

            with ThreadPoolExecutor(max_workers=cls.CONFIG.threads()) as executor:
                futures = [executor.submit(spam_activities_thread, discord_channel, discord_guild) for _ in range(int(repeat_count))]
                for future in futures:
                    future.result()
        except KeyboardInterrupt:
            return print() # Empty frame
        
    
    @classmethod
    def soundboard(cls):
        try:
            Logging.log_warning("Remember to be in voice channel for this to work", is_print=True)
            discord_channel: str = input(f"[{Fore.LIGHTBLUE_EX}ChannelID{Fore.RESET}] ›› ")
            repeat_count: str = input(f"[{Fore.LIGHTBLACK_EX}Spam count{Fore.RESET}] ›› ")

            def spam_soundboard_thread(discord_channel):
                spam_soundboard(discord_channel=discord_channel, discord_header=cls.DISCORD_HEADER)
            
            with ThreadPoolExecutor(max_workers=cls.CONFIG.threads()) as executor:
                futures = [executor.submit(spam_soundboard_thread, discord_channel) for _ in range(int(repeat_count))]
                for future in futures:
                    future.result()

        except KeyboardInterrupt:
            return print()
