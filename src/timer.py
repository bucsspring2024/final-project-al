import time
from datetime import datetime

class Timer:
    def __init__(self,seconds=30):
        '''
        Initializes the timer of the game
        The game will be 30 seconds unless programmed otherwise
        '''
        self.seconds = seconds
        self.current= datetime.now()
        time.sleep(1)
        seconds -= 1
    def timesup(self):
        now= datetime.now()
        diff = now-self.current
        if diff.total_seconds() >= self.seconds:
            return True
        else:
            return False