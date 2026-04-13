from skills.time_skill import get_time
from skills.app_launcher import open_app

def route_command(text: str):
    text = text.lower()

    # TIME
    if "time" in text:
        return get_time()

    # OPEN APPS
    if "open" in text:
        return open_app(text)

    return "Sorry, I didn't understand that."