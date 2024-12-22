"""
line.py - Defines a station line:
- used to receive a train into a station
- should be next to a platform to be considered for commercial service, otherwise would be considered storage
- its length should be compatible with the incoming train
- A parameter can indicate that one of the boundaries is an ending.
"""

import typing

class StationLine:
    """Defines a station's line."""
    _name: str
    _length: int  # length of this line
    _is_ending: bool  # if set to False, train can come from both line endings.
    _station: "TrainStation"  # Refers to a train station scene.

    def __init__(self, station: "TrainStation", config: dict):
        """Line constructor"""
        from scenes.TrainStation import TrainStation

        if station is None or isinstance(station, TrainStation) is False:
            raise RuntimeError("Missing station for this train station line")
        self._station = station
        self._length = gameconfig.getValue(config, "length", int, {"minValue": 1, "defaultValue": 450})
        self._is_ending = gameconfig.getValue(config, "ending", bool, {"defaultValue": False})
        self._name = gameconfig.getValue(config, "name", str)
        if self._name == "" or _name == None:
            raise RuntimeError("A station line should always have a name property")

    def getLength(self) -> int:
        return self._length
    def getName(self) -> str:
        return self._name

    def hasEnding(self) -> bool:
        return self._is_ending

    def __str__(self) -> str:
        ending = "with ending" if self._is_ending else "without ending"
        return f"StationLine({self._name}, {self._length}m, {ending})"
