import httpx
import random
import json
import time

from ...config.parser import JsonParser
from ...errors.errors import Logging

CONFIG = JsonParser()

def spam_activitys(discord_header: dict, channel_id: str, guild_id: str):
    reverify_data = json.dumps({
        "guild_id": guild_id,
        "session_id": CONFIG.session_token(),
        "timestamps": {
            "end": "2024-04-08"
        },
        "name": "o nooo"
    })
            
    random_apps: list = [
        880218394199220334, 
        1037680572660727838, 
        1078728822972764312, 
        947957217959759964, 
        945737671223947305, 
        832012774040141894, 
        832025144389533716, 
        903769130790969345
    ]

    chosen_app = random.choice(random_apps)
    reverify_url = f"https://discord.com/api/v9/activities/{channel_id}/{chosen_app}"

    discord_header['X-Super-Properties'] = json.dumps({
        "system_locale": "en-US",
        "browser_user_agent": discord_header["User-Agent"],
        "browser_version": "94.0.4606.81",
        "os_version": "10",
        "referrer": "https://discord.com/",
        "referring_domain": "https://discord.com/",
        "referrer_current": "https://discord.com/",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 10666,
        "client_event_source": None
    })

    response = httpx.post(reverify_url, headers=discord_header, data=reverify_data)

    try:
        response.raise_for_status()
        Logging.log_info(f"Sent {chosen_app} to Channel: {channel_id} in Guild: {guild_id}", is_print=True)
    except (httpx.HTTPStatusError, httpx.ReadTimeout):
        Logging.log_warning("Hit discord ratelimit", is_print=False)
        time.sleep(3.5)
