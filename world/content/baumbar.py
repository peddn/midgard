from evennia import create_object

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

        sofas = self.create_vobject('Sofa', ['Sofas', 'Couch', 'Couches'])
        sofas.db.desc = 'Die Sofas sehen sehr gemütlich aus. Vielleicht solltest du sie mal ausprobieren?'

        durchgang = self.create_vobject('Durchgang', ['Tür'])
        durchgang.db.desc = 'Eine Zarge aus geöltem und poliertem Eichenholz bildet den Durchgang zur Küche'
        durchgang.db.smell = 'Der Durchgang riecht angenehm nach geöltem Eichenholz.'


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
        sefl.db.smell = "Die Luft riecht süßlich frisch nach Blüten. Einfach herrlich."

