import time
import datetime

class Timer:
    def Countdown(self,seconds=60):
        while seconds > 0:
            timer= datetime.timedelta(seconds)
            time.sleep(1)
            seconds -= 1
            print(seconds)
        print("Game over")