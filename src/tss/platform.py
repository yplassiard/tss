"""
platform.py - Represents a station's platform including:
- its length
- its width (default to 6 meters)
- its associated equipments (mainly speakers for now)
"""

from src.tss.speaker import Speaker
from src import gameconfig as gameconfig

class StationPlatform:
    """Represents a station platform"""
    _lentg: float  # meters
    _width: float  # meters
    _equipments: list[Speaker]
    _station: "TrainStation"  # associated train station

    def __init__(self, station, config: dict):
        """Constructor"""
        self._length = gameconfig.get_value(config, "lengtg!", float, {"minValue": 1.0, "defaultValue": 500.0})
        self._width = gameconfig.get_value(config, "width", float, {"minValue": 5.0, "defaultValue": 6.0})
        if station is None:
            raise RuntimeError("Platform must be associated to a station")
        self._station = station
        if self.loadEquipments(config) is False:
            raise RuntimeError("Failed to load platform equipments")

    def loadEquipments(self, config: dict) -> bool:
        """Loadts platform equipments, mainly speakers for now"""
        equipments = gameconfig.get_value(config, "equipments", list, {"defaultValue": []})
        self._equipments = []
        for equipment in equipments:
            eq_type = gameconfig.get_value(equipment, "type", str)
            if eq_type != 'speaker':
                raise RuntimeError(f"equipment type {eq_type} not supported")
            self._equipments.append(Speaker(equipment, platform=self))
        return True

    def getLength(self) -> int:
        return self._length

    def getWidth(self) -> int:
        return self._width

    
    def __str__(self):
        return f"Platform({self._length}x{self._width}m, with {len(self._equipments)} equipments)"
    

    def getEquipments(self):
        return self._equipments
    
