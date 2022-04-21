from evennia import Command
from evennia.utils import utils

from world.util.grammar import Case, get_def_art

class CmdSoulKicher(Command):
    """
    """
    key = "kicher"
    aliases = []

    def func(self):
        ""
        caller = self.caller
        location = self.caller.location

        caller.msg('Du kicherst belustigt.')
        location.msg_contents(caller.key + ' kichert belustigt.', exclude=caller)
            