from src.tss.speaker import (
    Speaker,
    SpeakerDirectivity,
    LocationType
)

class Hallway:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getLength(self):
        return self._x
    def getWidth(self):
        return self._y
    def getName(self):
        return "fakeHall"


class Platform:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getLength(self):
        return self._x
    def getWidth(self):
        return self._y
    def getName(self):
        return "fakePlatform"


def test_speaker_platform_init():
    platform = Platform(400, 6)
    speakerConf = {"platform-position": 5.0}
    speaker = Speaker(speakerConf, platform=platform)
    assert speaker.getPosition() == [5.0, 3.0]
    assert speaker._location == LocationType.PLATFORM
    assert str(speaker) == "Speaker(platform(fakePlatform, at 5.0m, 4.0m height, cardioid)"

def test_speaker_hallway_init():
    hallway = Hallway(400, 12)
    speakerConf = {"hallway-position": [5.0, 3.0]}
    speaker = Speaker(speakerConf, hallway=hallway)
    assert speaker.getPosition() == [5.0, 3.0]
    assert speaker._location == LocationType.HALLWAY
    assert speaker._directivity == SpeakerDirectivity.CARDIOID
    assert str(speaker) == "Speaker(hallway(fakeHall, at [5.0, 3.0]m, 4.0m height, cardioid)"    
