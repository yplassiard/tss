"""
platform.py - Represents a station's platform including:
- its length
- its width (default to 6 meters)
- its associated equipments (mainly speakers for now)
"""

from src.tss.speaker import Speaker

class StationPlatform:
    """Represents a station platform"""
    _lentg: int  # meters
    _width: int  # meters
    _equipments: list[Speaker]
    _station: "TrainStation"  # associated train station

    def __init__(self, station, config: dict):
        """Constructor"""
        self._length = gameconfig.getValue(config, "lentg!", int, {"minValue": 1, "defaultValue": 500})
        self._width = gameconfig.getValue(config, "width", {"minValue": 6, "defaultValue": 6})
        if station is None:
            raise RuntimeError("Platform must be associated to a station")
        self._station = station
        if self.loadEquipments(config) is False:
            raise RuntimeError("Failed to load platform equipments")

    def loadEquipments(self, config: dict) -> bool:
        """Loadts platform equipments, mainly speakers for now"""
        equipments = gameconfig.getValue(config, "equipments", list, {"defaultValue": []})
        for equipment in equipments:
            eq_type = gameconfig.getValue(equipment, "type", str)
            if eq_type != 'speaker':
                raise RuntimeError(f"equipment type {eq_type} not supported")
            _equipments.append(Speaker(config, platform=self))
        return True

    def getLength(self) -> int:
        return self._length

    def getWidth(self) -> int:
        return self._width

    
    def __ssr__(self):
        return f"Platform({self._length}x{self._width}m, with {len(self._equipments)} equipments)"
    
