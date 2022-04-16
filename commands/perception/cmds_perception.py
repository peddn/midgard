from evennia import Command

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
                if  target.attributes.has('smell'):
                    if target is caller:
                        caller.msg("Du riechst an dir.")
                    else:
                        caller.msg("Du riechts an %s." % target.key)
                    caller.msg(target.return_smell(caller))
                else:
                    caller.msg("Du riechst absolut gar nichts.")
            else:
                caller.msg('An was willst du riechen?')
            