"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.utils import utils

from world.util.grammar import Gender

from typeclasses.objects import Object
from commands.rooms.cmdset_room import CmdsetRoom




class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    def at_object_creation(self):
        "This is only called when the room is first created."
        self.db.desc = "Ein nigelnagelneuer Raum."
        self.db.smell = "Hier riecht es nach absolut gar nichts."
        self.db.details = {}
        self.cmdset.add(CmdsetRoom, permanent=True)
        self.db.gender = Gender.MASKULIN


    def return_smell(self, perceptor):
        """
        The return from this method is what
        perceptor smells when smelling at this object.
        """
        return self.db.smell

    @property
    def x(self):
        """Return the X coordinate or None."""
        x = self.tags.get(category="coordx")
        return int(x) if isinstance(x, str) else None

    @x.setter
    def x(self, x):
        """Change the X coordinate."""
        old = self.tags.get(category="coordx")
        if old is not None:
            self.tags.remove(old, category="coordx")
        if x is not None:
            self.tags.add(str(x), category="coordx")

    @property
    def y(self):
        """Return the Y coordinate or None."""
        y = self.tags.get(category="coordy")
        return int(y) if isinstance(y, str) else None

    @y.setter
    def y(self, y):
        """Change the Y coordinate."""
        old = self.tags.get(category="coordy")
        if old is not None:
            self.tags.remove(old, category="coordy")
        if y is not None:
            self.tags.add(str(y), category="coordy")

    @property
    def z(self):
        """Return the Z coordinate or None."""
        z = self.tags.get(category="coordz")
        return int(z) if isinstance(z, str) else None

    @z.setter
    def z(self, z):
        """Change the Z coordinate."""
        old = self.tags.get(category="coordz")
        if old is not None:
            self.tags.remove(old, category="coordz")
        if z is not None:
            self.tags.add(str(z), category="coordz")


    def return_detail(self, detailkey):
        """
        This looks for an Attribute "obj_details" and possibly
        returns the value of it.
        Args:
            detailkey (str): The detail being looked at. This is
                case-insensitive.
        """
        return self.db.details.get(detailkey.lower(), None)

    def set_detail(self, detailkey, description):
        """
        This sets a new detail.
        Args:
            detailkey (str): The detail identifier to add (for
                aliases you need to add multiple keys to the
                same description). Case-insensitive.
            description (str): The text to return when looking
                at the given detailkey.
        """
        self.db.details[detailkey.lower()] = description

    def at_object_receive(self, new_arrival, source_location):
        """
        When an object enter a room we tell other objects in
        the room about it by trying to call the 'at_new_arrival' on them.
        Args:
            new_arrival (Object): the object that just entered this room.
            source_location (Object): the previous location of new_arrival.
        """
        if new_arrival.has_account and not new_arrival.is_superuser:
            # this is a character
            for obj in self.contents_get(exclude=new_arrival):
                if hasattr(obj, "at_new_arrival"):
                    obj.at_new_arrival(new_arrival)

    def return_appearance(self, looker):
        """
        The return from this method is what
        looker sees when looking at this object.
        """
        #text = super().return_appearance(looker)

        room_name = self.get_display_name(looker) + "\n"
        room_desc = self.db.desc + "\n"

        show_exits = False
        room_exits = "Ausgänge:\n"
        for exit in self.exits:
            room_exits = room_exits + " " + exit.get_display_name(looker)
            show_exits = True
        
        show_chars = False
        room_chars = "Außerdem anwesend sind:\n"
        for content in self.contents_get(exclude=looker):
            if utils.inherits_from(content, 'typeclasses.characters.Character'):
                room_chars += content.get_display_name(looker) + '\n'
                show_chars = True

        text = room_name + room_desc
        
        if(show_exits):
            text = text + room_exits + "\n"
        
        if(show_chars):
            text = text + room_chars

        return text

    def create_vobject(key, aliases):
        return create_object('typeclasses.objects.VirtualObject', key=key, aliases=aliases, home=self, location=self)
