"""
TrainStation.py - a scene representing a train station
"""

from src.scenes.scene import IntervalScene

from src.tss.planner import Planner
from src.tss.line import StationLine
from src.tss.platform import StationPlatform

class Scene(IntervalScene):
    _width: int  # meters
    _length: int  # meters
    _lines: list[StationLine]  # list of station lines
    _platforms: list[StationPlatform]  # each line has to be next to at least one platfor to be considered for commercial service
    _planner: Planner  # route planner

    def __init__(self, config, *args, **kwargs):
        super().__init__(config, *args, **kwargs)

