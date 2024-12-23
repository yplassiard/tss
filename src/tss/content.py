"""
content.py - Station content

This contains the base StationContent class that represent a station content:
- a station line (to receive trains)
- a station platform (to allow passenger boarding)
- a station hallway (to allow passengers to enter into the station)

"""

import typing
import enum

class StationContentType(enum.IntEnum):
    HALLWAY = 0,
    LINE = 1,
    PLATFORM = 2

class StationContent:
    """Base class for a station line or platform"""
    _contentType: StationContentType

    def __init__(self, stype: StationContentType):
        self._contentType = stype

    def getContentType(self):
        return self._contentType
