
import time
class Detector:
    def __init__(self):
        self.events=[]
    def record_change(self, path):
        now=time.time()
        self.events.append(now)
        self.events=[e for e in self.events if now-e<3]
        return len(self.events)>=20
