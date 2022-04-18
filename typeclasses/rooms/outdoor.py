"""
RoomOutdoor

Rooms are simple containers that has no location of their own.

"""

from typeclasses.rooms.default import Room

class RoomOutdoor(Room):
    """
    """
    def at_object_creation(self):
        super().at_object_creation()
