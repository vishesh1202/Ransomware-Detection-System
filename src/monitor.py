
import time, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from detector import Detector
from responder import Responder

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.detector = Detector()
        self.responder = Responder()

    def on_modified(self, event):
        if event.is_directory:
            return
        if self.detector.record_change(event.src_path):
            self.responder.handle_detection(event.src_path)

def start_monitor():
    logging.basicConfig(filename="logs/events.log", level=logging.INFO)
    obs = Observer()
    obs.schedule(Handler(), "watched", recursive=True)
    obs.start()
    print("Monitoring started")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        obs.stop()
    obs.join()
