import httpx
import json
import time

from ...config.parser import JsonParser
from ...errors.errors import Logging

CONFIG = JsonParser()

def spam_soundboard(discord_channel: str, discord_header: dict):
    sound = json.dumps(
        {
                    
            "emoji_name": "🤣",
            "sound_id": "2",
                    
        }
    ) # This can be changed to any emoji and sound (Depending on if you have nitro)


    play_sound = httpx.post(f"https://discord.com/api/v9/channels/{discord_channel}/send-soundboard-sound", headers=discord_header, data=sound)

    try:
        if play_sound.json()["code"] == 50168 or play_sound.json()["code"] == 50013:
            Logging.log_warning(f"Failed to send sound to Channel: {discord_channel}", is_print=True)
       
    except (httpx.HTTPStatusError, httpx.ReadTimeout, json.decoder.JSONDecodeError, KeyError) as e:
        if isinstance(e, (httpx.HTTPStatusError, httpx.ReadTimeout)):
            Logging.log_warning("Hit discord ratelimit", is_print=False)
            time.sleep(2.5)
        elif isinstance(e, json.decoder.JSONDecodeError):
            Logging.log_info(f"Sent sound to Channel: {discord_channel}", is_print=True)
       

    

