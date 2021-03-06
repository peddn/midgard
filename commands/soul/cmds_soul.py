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
                caller.msg('Möchtest du eventuell |wauf|n etwas deuten?')
            else:
                if len(self.args) > 1:
                    target = caller.search(self.args[1])
                    if target:
                        if target == caller:
                            caller.msg('Du deutest auf dich.')
                            location.msg_contents('%s deutet auf sich.' % (caller.key), exclude=caller)
                        else:
                            if utils.inherits_from(target, 'typeclasses.characters.Character'):
                                caller.msg('Du deutest auf %s.' % (target.key))
                                location.msg_contents('%s deutet auf %s.' % (caller.key, target.key), exclude=[caller, target])
                                target.msg('%s deutet auf dich.' % (caller.key))
                            else:
                                caller.msg('Du deutest auf %s %s.' % (get_def_art(target, Case.AKK), target.key))
                                location.msg_contents('%s deutet auf %s %s.' % (caller.key, get_def_art(target, Case.AKK), target.key), exclude=[caller, target])
                                target.msg('%s deutet auf dich.' % (caller.key))
                else:
                    caller.msg('Auf was möchtest du denn deuten?')
        else:
            caller.msg('Du deutest vage in der Gegend herum.')
            location.msg_contents(caller.key + ' deutet vage in der gegend herum.', exclude=caller)

