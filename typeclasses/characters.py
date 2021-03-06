"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

from world.util.grammar import Gender

from typeclasses.objects import Object
from commands.perception.cmdset_perception import CmdsetPerception
from commands.soul.cmdset_soul import CmdsetSoul

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def at_object_creation(self):
        self.db.gender = Gender.MASKULIN
        self.db.smell = '%s riecht nach absolut gar nichts.' % (self.key)
    
    def return_smell(self, perceptor):
        """
        The return from this method is what
        perceptor smells when smelling at this object.
        """
        return self.db.smell
    
    def at_init(self):
        """
        Called just after puppeting has been completed and all
        Account<->Object links have been established.

        Args:
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        Note:
            You can use `self.account` and `self.sessions.get()` to get
            account and sessions at this point; the last entry in the
            list from `self.sessions.get()` is the latest Session
            puppeting this Object.

        """
        #self.msg('DEBUG: at_init')
        super().at_init()
        self.cmdset.add(CmdsetPerception)
        self.cmdset.add(CmdsetSoul)

    
    def at_post_puppet(self):
        super().at_post_puppet()


