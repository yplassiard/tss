"""
TrainStation.py - a scene representing a train station
"""

from scene.scene import Scene

from tss.planner import Planner
from tss.line import StationLine
from tss.platform import StationPlatform

class TrainStationScene(IntervalScene):
    _width: int  # meters
    _length: int  # meters
    _lines: list[StationLine]  # list of station lines
    _platforms: list[StationPlatform]  # each line has to be next to at least one platfor to be considered for commercial service
    _planner: Planner  # route planner
    
