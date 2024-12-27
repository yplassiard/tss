"""
line.py - Defines a station line:
- used to receive a train into a station
- should be next to a platform to be considered for commercial service, otherwise would be considered storage
- its length should be compatible with the incoming train
- A parameter can indicate that one of the boundaries is an ending.
"""

import typing
import enum

from src import gameconfig
from src import logger as logger

from src.tss.content import (
    StationContentType,
    StationContent
)

class StationLineType(enum.IntEnum):
    UNKNOWN = 0,
    COMMERCIAL = 1,
    STORAGE = 2

class StationLine(StationContent):
    """Defines a station's line."""
    _name: str
    _width: float
    _length: int  # length of this line
    _is_ending: bool  # if set to False, train can come from both line endings.
    _station: "Scene"  # Refers to a train station scene.
    _position: list[float, float]  # line's coordinates in a station

    def __init__(self, station: "TrainStation", config: dict):
        super().__init__(StationContentType.LINE)
        """Line constructor"""
        from src.scenes.TrainStation import Scene

        if station is None or isinstance(station, Scene) is False:
            raise RuntimeError("Missing station for this train station line")
        self._station = station
        self._type = StationLineType.UNKNOWN
        self._length = gameconfig.get_value(config, "length", float, {"minValue": 1.0, "defaultValue": 450.0})
        self._width = gameconfig.get_value(config, "width", float, {"minValue": 4.0, "mandatory": True})
        self._is_ending = gameconfig.get_value(config, "ending", bool, {"defaultValue": False})
        self._name = gameconfig.get_value(config, "name", str, {"mandatory": True})
        logger.debug(self, f"{str(self)} initialized")

    def getLength(self) -> int:
        return self._length
    def getName(self) -> str:
        return self._name

    def hasEnding(self) -> bool:
        return self._is_ending

    def getLineType(self) -> StationLineType:
        return self._type
    
    def setLineType(self, stype: StationLineType):
        self._type = stype
        logger.debug(self, f"setType")

    def setPosition(self, position: tuple[float, float]):
        self._position = position
        logger.debug(self, f"setPosition({position}): {str(self)}")

    def getWidth(self):
        return self._width
    
    def getLogName(self):
        return f"StationLine({self._yame})"
    def __str__(self) -> str:
        ending = "with ending" if self._is_ending else "without ending"
        stype = 'Unknown'
        if self._type == StationLineType.STORAGE:
            stype = "storage"
        elif self._type == StationLineType.COMMERCIAL:
            stype = "commercial"
        return f"StationLine({self._name}, {stype}, {self._length}m, {ending})"
