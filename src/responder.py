
import logging
class Responder:
    def handle_detection(self, path):
        logging.warning(f"Detection triggered near {path}")
        print("ALERT: suspicious activity detected")
