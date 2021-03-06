from evennia import Command
from evennia.utils import utils

from world.util.grammar import Case, get_def_art

class CmdPerceptionSmell(Command):
    """
    """
    key = "smell"
    aliases = ["rieche"]

    def func(self):
        ""
        caller = self.caller
        location = self.caller.location

        if self.args:
            target = caller.search(self.args.strip())
            if target:
                if hasattr(target, "return_smell"):
                    if target is caller:
                        caller.msg('Du riechst an dir.')
                        location.msg_contents('%s riecht an sich.' % (caller.key), exclude=caller)
                    else:
                        if utils.inherits_from(target, 'typeclasses.characters.Character'):
                            caller.msg('Du riechst an %s.' % (target.key))
                        else:
                            caller.msg('Du riechst an %s %s.' % (get_def_art(target, Case.DAT), target.key))
                        target.msg('%s riecht an dir.' % (caller.key))
                        if utils.inherits_from(target, 'typeclasses.characters.Character'):
                            location.msg_contents("%s riecht an %s." % (caller.key, target.key), exclude=[ caller, target ])
                        else:
                            location.msg_contents("%s riecht an %s %s." % (caller.key, get_def_art(target, Case.DAT), target.key), exclude=[ caller, target ])
                    caller.msg(target.return_smell(caller))
                else:
                    caller.msg('Du riechst absolut gar nichts.')
            else:
                caller.msg('An was willst du riechen?')
            