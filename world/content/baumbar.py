from typeclasses.rooms.indoor import RoomIndoor

from world.util.grammar import Gender

class BaumbarLounge(RoomIndoor):
    """
    """
    def at_object_creation(self):
        "This is called when object is first created, only."
        self.db.desc = 'Du stehst in der Lounge der Baumbar. Hier gibt es einige sehr gemütlich aussehnde Sofas. In Richtung Stammmitte befindet sich ein Durchgang, aus dessen Richtung es verführerisch nach gegritten Speisen riecht.'
        self.db.smell = 'Aus Richtung der Küche schwebt dir ein verführerischer Geruch nach gegrilltem Fleisch in die Nase'
        self.db.gender = Gender.FEMININ
