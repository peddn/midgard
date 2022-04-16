from evennia import CmdSet

from commands.rooms.cmds_room import CmdRoomAddDetail, CmdRoomLookDetail

class CmdsetRoom(CmdSet):
    """
    Implements the simple tutorial cmdset. This will overload the look
    command in the default CharacterCmdSet since it has a higher
    priority (ChracterCmdSet has prio 0)
    """

    key = "CmdsetRoom"
    priority = 1

    def at_cmdset_creation(self):
        """add the room commands"""
        self.add(CmdRoomAddDetail())
        self.add(CmdRoomLookDetail())
