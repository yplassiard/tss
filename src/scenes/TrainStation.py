"""
TrainStation.py - a scene representing a train station
"""

from src import constants as constants
from src import gameconfig as gameconfig
from src import logger as logger


from src.scenes.scene import IntervalScene

from src.tss.content import (
    StationContent,
    StationContentType
)

from src.tss.planner import Planner
from src.tss.line import (
    StationLine,
    StationLineType
)

from src.tss.platform import StationPlatform

class Scene(IntervalScene):
    _width: float  # meters
    _length: float  # meters
    _content: list[StationContent] = [] # lines, platforms and hallways
    _planner: Planner  # route planner

    def __init__(self, name, config, *args, **kwargs):
        config["interval"] = constants.SCENE_MINIMUM_INTERVAL
        super().__init__(name, config)
        self._length = gameconfig.get_value(config, "length", float, {"minValue": 100.0, "mandatory": True})
        self._width = gameconfig.get_value(config, "width", float, {"minValue": 50.0, "mandatory": True})
        
        lps = gameconfig.get_value(config, "content", list, {"elements": 2, "mandatory": True})
        self.loadLinesAndPlatforms(lps)
        
    def loadLinesAndPlatforms(self, lps):
        """Load all platforms and associated lines, setting their coordinates in the station's area."""
        cur_pos = 0.0
        try:
            lps.sort(key=lambda x: x["width"])
        except KeyError:
            logger.exception(self, f"Failed to parse station \"content\" array: {ex}", ex)
            raise ex
        errors = False
        if len(lps) == 0:
            raise RuntimeError("No \"content\" data")
        for content in lps:
            ctype = gameconfig.get_value(content, "type", str, {"oneOf": ["line", "platform"], "mandatory": True})
            obj = None
            if ctype == 'line':
                try:
                    obj = StationLine(self, content)
                except Exception as ex:
                    logger.exception(self, f"Failed to instanciate {ctype}: {ex}", ex)
                    raise ex
                    errors = True
            elif ctype == 'platform':
                try:
                    obj = StationPlatform(self, content)
                except Exception as ex:
                    logger.exception(self, f"Failed to instanciate {ctype}: {ex}", ex)
                    raise ex
                    errors = True
                
            if cur_pos + obj.getWidth() > self._width:
                logger.error(self, f"{str(obj)}: outside station area width")
                errors = True
                continue
            obj.setPosition((cur_pos, 0.0))
            cur_pos += obj.getWidth() + constants.DEFAULT_SPACE_BETWEEN_LINE_AND_PLATFORM
            self._content.append(obj)


        if errors:
            raise RuntimeError(f"Error while parsing station content")

        # determine if a line is storage

        for i in range(len(self._content)):
            if self._content[i].getContentType() == StationContentType.LINE:
                if ((i + 1 < len(self._content) and self._content[i + 1].getContentType() == StationContentType.PLATFORM) \
                    or (i > 0 and self._content[i - 1].getContentType() == StationContentType.PLATFORM)):
                    self._content[i].setLineType(StationLineType.COMMERCIAL)
                else:
                    self._content[i].setLineType(StationLineType.STORAGE)

