from rooms.indoor import RoomIndoor

class WorkroomLughaid(RoomIndoor):
    """
    """
    def at_object_creation(self):
        self.db.desc = "Das hier Lughaid's Arbeitsraum. Viel ist hier noch nicht passiert."
