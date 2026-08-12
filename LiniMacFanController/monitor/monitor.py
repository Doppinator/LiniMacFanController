import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def monitor(self, interval: float = 1.0):
        """Monitor the fans and sensors, printing their status to the console."""
        while True:
            self.refresh()
            clear_terminal()
            print(self)
            time.sleep(interval)