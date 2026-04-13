from datetime import datetime

def get_time():
    now = datetime.now().strftime("%I:%M %p")
    return f"The time is {now}"