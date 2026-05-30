
from src.detector import Detector
def test_detector():
    d=Detector()
    result=False
    for i in range(20):
        result=d.record_change("x")
    assert result is True
