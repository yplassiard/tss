"""
planner.py - Route Planner

The Route Planner, called `Planner` is responsible for:
- Planning a trip from a given service
- Get information along the service's way (expected platform, schedule, etc...)
- Modify a planned service (local decision for a given station)
- Compute some service's statistics to give a global trip score.
"""

class Planner:
    """Our route planner"""
    _services = []

    def __init__(self, config):
        """Planner constructor."""
    def addService(self, service) -> bool:
        return False
