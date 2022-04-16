from typeclasses.rooms.indoor import RoomIndoor

class BaumbarLounge(RoomIndoor):
    """
    """
    def at_object_creation(self):
        "This is called when object is first created, only."
        self.db.desc = 'Du stehst in der Lounge der Baumbar. Hier gibt es einige sehr gemütlich aussehnde Sofas. In Richtung Stammmitte befindet sich ein Durchgang, aus dessen Richtung es verführerisch nach gegritten Speisen riecht.'
