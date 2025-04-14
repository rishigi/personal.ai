import keyboard  # Python library for detecting key presses

class ActivationListener:
    def is_activated(self):
        # Detect volume button press (simulation for desktop)
        print("Listening for activation...")
        return keyboard.is_pressed("volume up")