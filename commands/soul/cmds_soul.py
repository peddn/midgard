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

class CmdSoulDeute(Command):
    """
    """
    key = "deute"
    aliases = []

    def func(self):
        ""
        caller = self.caller
        location = self.caller.location

        self.args = self.args.strip()

        if self.args:
            self.args = self.args.split()
            self.args = [arg.strip() for arg in self.args]
            self.args = [arg.lower() for arg in self.args]
            if self.args[0] != 'auf':
                caller.msg('möchtest du eventulell AUF etwas deuten?\n')
            else:
                if len(self.args) > 1:
                    target = caller.search(self.args[1])
                    if target:
                        caller.msg('Du deutest auf ' + target.key)
                    else:
                        caller.msg('So etwas wie ein %s gibt es hier nicht.' % (self.args[1]))
                else:
                    caller.msg('Auf was möchtest du denn deuten?')
                


        caller.msg('Du deutest vage in der Gegend herum.')
        location.msg_contents(caller.key + ' deutet vage in der gegend herum.', exclude=caller)