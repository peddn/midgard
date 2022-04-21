from evennia import CmdSet

from commands.soul.cmds_soul import CmdSoulKicher, CmdSoulDeute

class CmdsetSoul(CmdSet):
    """
    """

    key = "CmdsetSoul"

    def at_cmdset_creation(self):
        """add the soul commands"""
        self.add(CmdSoulKicher())
        self.add(CmdSoulDeute())
