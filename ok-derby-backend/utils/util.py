import os
import sys
import win32gui


def is_game_running() -> bool:
    h_wnd = win32gui.FindWindow("UnityWndClass", "umamusume")
    if not h_wnd:
        return False
    else:
        return True


def app_path() -> str:
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return os.path.dirname(sys.executable)
    return os.path.join(os.path.dirname(__file__), "..")
