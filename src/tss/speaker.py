"""
speaker.py - A speaker object.

A Speaker is an object that represents a speaker with the following characteristics:
- its position alongside a platiorm, or its coordinates in a hall
- its height in meters relative to the platform's or hall's ground
- its directivity type (omni, cardiodid, ...)
"""

import enum

import src.constants as constants
import src.gameconfig as gameconfig


class SpeakerDirectivity(enum.StrEnum):
    """represents the speaker directivity"""
    OMNI = "omni",
    CARDIOID = "cardioid",
    HYPER_CARDIOID = "hyper-cardioid"

class LocationType(enum.IntEnum):
    NONE = 0,
    PLATFORM = 1,
    HALLWAY = 2


class Speaker:
    """A Speaker attached to a platform, or a hallway"""
    _directivity: SpeakerDirectivity = SpeakerDirectivity.CARDIOID
    _height: float = constants.DEFAULT_SPEAKER_HEIGHT
    _platformPosition: float = 0.0
    _hallwayPosition: list[float, float] = (0.0, 0.0)
    _owner = None
    _locationType: LocationType = LocationType.NONE
    
    def __init__(self, config, platform=None, hallway=None):
        """Speaker constructor"""
        if platform:
            self._owner = platform
            self._platformPosition = gameconfig.get_value(config, "platform-position", float, {"mandatory": True, "minValue": 0.0, "maxValue": platform.getLength()})
            self._hallPosition = [-1.0, -1.0]
            self._location = LocationType.PLATFORM
        elif hallway:
            self._owner = hallway
            coords = gameconfig.get_value(config, "hallway-position", list, {"elements": 2})
            if coords is None:
                raise RuntimeError(f"Speaker attached to a hallway without a \"hallway-position\" value")
            if isinstance(coords[0], float) is False or isinstance(coords[1], float) is False:
                raise RuntimeError(f"speaker hallway coordinates {coords} has to be of type float")

            # checks that the coordinates are located in the hallway

            if coords[0] >= 0 and coords[0] <= hallway.getLength() \
               and coords[1] >= 0 and coords[1] <= hallway.getWidth():
                self._hallwayPosition = coords
            else:
                raise RuntimeError(f"Coordinates {coords} are outside hallway {hallway}")
            self._location = LocationType.HALLWAY
        else:
            raise RuntimeError("A speaker must be attached either to a hallway or platform")

        self._height = gameconfig.get_value(config, "height", float, {"minValue": 2.0, "maxValue": 8.0, "defaultValue": 4.0})
        self._directivity = gameconfig.get_value(config, "directivity", str, {"oneOf": ["omni", "cardioid", "hyper-cardioid"], "defaultValue": "cardioid"})


    def __str__(self):
        if self._location == LocationType.PLATFORM:
            return f"Speaker(platform({self._owner.getName()}, at {self._platformPosition}m, {self._height}m height, {self._directivity})"
        else:
            return f"Speaker(hallway({self._owner.getName()}, at {self._hallwayPosition}m, {self._height}m height, {self._directivity})"

    def getPosition(self):
        if self._location == LocationType.PLATFORM:
            return [self._platformPosition, self._owner.getWidth() / 2]
        elif self._location == LocationType.HALLWAY:
            return self._hallwayPosition
        else:
            raise ValueError("Unsupported location type {self._location}")
        return [None, None]
    
