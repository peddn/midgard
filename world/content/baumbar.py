from typeclasses.rooms.indoor import RoomIndoor
from typeclasses.rooms.outdoor import RoomOutdoor

from world.util.grammar import Gender

class BaumbarLounge(RoomIndoor):
    """
    """
    def at_object_creation(self):
        "This is called when object is first created, only."
        super().at_object_creation()
        self.db.desc = 'Du stehst in der Lounge der Baumbar. Hier gibt es einige sehr gemütlich aussehnde Sofas. In Richtung Stammmitte befindet sich ein Durchgang, aus dessen Richtung es verführerisch nach gegrillten Speisen riecht.'
        self.db.gender = Gender.FEMININ

    def return_smell(self, perceptor):
        smell = 'Aus Richtung der Küche schwebt dir ein verführerischer Geruch nach gegrilltem Fleisch in die Nase'
        return smell

class BaumbarWiese(RoomOutdoor):
    """
    """
    def at_object_creation(self):
        ""
        super().at_object_creation()
        self.db.desc = 'Du stehst in einer wunderschönen Blumenwiese. Im Norden trohnt eine mächtige Eiche mit dem dicksten Stamm, den du jeh gesehen hast. Ein kleiner Pfad führt zur Eiche hin. Im Süden kannst du ein seltsam schimmerndes Portal erkennen.'
        self.db.gender = Gender.FEMININ

    def return_smell(self, perceptor):
        smell = "Die Luft riecht süßlich frisch nach Blüten. Einfach herrlich."
        return smell
