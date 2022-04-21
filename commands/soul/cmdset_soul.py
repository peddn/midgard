from evennia import CmdSet

from commands.soul.cmds_soul import CmdSoulKicher

class CmdsetSoul(CmdSet):
    """
    """

    key = "CmdsetSoul"

    def at_cmdset_creation(self):
        """add the perception commands"""
        self.add(CmdSoulKicher())
