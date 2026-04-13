import subprocess

def open_app(text):
    if "firefox" in text:
        subprocess.Popen(["firefox"])
        return "Opening Firefox"

    if "terminal" in text:
        subprocess.Popen(["gnome-terminal"])
        return "Opening Terminal"

    return "I don't know how to open that yet."