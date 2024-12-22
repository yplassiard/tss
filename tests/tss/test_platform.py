from src.tss.platform import *
class TrainStation:
    _name = "test"

def test_platform_init():
    pconfig = {"length": 500.0, "width": 6.0}
    station = TrainStation()
    platform = StationPlatform(station, pconfig)
    assert platform.getLength() == 500.0
    assert platform.getWidth() == 6.0
    

def test_platform_init_with_equipment():
    pconfig = {"length": 500.0, "width": 6.0,
               "equipments": [{"type": "speaker", "platform-position": 1.0},
                              {"type": "speaker", "platform-position": 6.0}
                              ]
               }
    station = TrainStation()
    platform = StationPlatform(station, pconfig)
    assert platform.getLength() == 500.0
    assert platform.getWidth() == 6.0
    assert str(platform) == "Platform(500.0x6.0m, with 2 equipments)"
    eqs = platform.getEquipments()
    assert len(eqs) == 2
    assert eqs[0].getPosition() == [1.0, 3.0]
