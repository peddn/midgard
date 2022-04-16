from evennia import CmdSet

from commands.perception.cmds_perception import CmdPerceptionSmell

class CmdsetPerception(CmdSet):
    """
    """

    key = "CmdsetPerception"

    def at_cmdset_creation(self):
        """add the perception commands"""
        self.add(CmdPerceptionSmell())
