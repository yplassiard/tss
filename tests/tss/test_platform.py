from src.tss.platform import *
class TrainStation:
    _name = "test"

def test_platform_init():
    pconfig = {"length": 500.0, "width": 6.0}
    station = TrainStation()
    platform = StationPlatform(station, pconfig)
    assert platform.getLength() == 500.0
    assert platform.getWidth() == 6.0
    
