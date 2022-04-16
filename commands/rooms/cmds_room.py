from evennia import default_cmds, utils


# the system error-handling module is defined in the settings. We load the
# given setting here using utils.object_from_module. This way we can use
# it regardless of if we change settings later.
from django.conf import settings

_SEARCH_AT_RESULT = utils.object_from_module(settings.SEARCH_AT_RESULT)



# for the @detail command we inherit from MuxCommand, since
# we want to make use of MuxCommand's pre-parsing of '=' in the
# argument.
class CmdRoomAddDetail(default_cmds.MuxCommand):
    """
    sets a detail on a room
    Usage:
        @room_add_detail <key> = <description>
        @room_add_detail <key>;<alias>;... = description
    Example:
        @room_add_detail walls = The walls are covered in ...
        @room_add_detail castle;ruin;tower = The distant ruin ...
    This sets a "detail" on the object this command is defined on
    (TutorialRoom for this tutorial). This detail can be accessed with
    the TutorialRoomLook command sitting on TutorialRoom objects (details
    are set as a simple dictionary on the room). This is a Builder command.
    We custom parse the key for the ;-separator in order to create
    multiple aliases to the detail all at once.
    """

    key = "@room_add_detail"
    locks = "cmd:perm(Builder)"
    help_category = "room"

    def func(self):
        """
        All this does is to check if the object has
        the set_detail method and uses it.
        """
        if not self.args or not self.rhs:
            self.caller.msg("Usage: @room_add_detail key = description")
            return
        if not hasattr(self.obj, "set_detail"):
            self.caller.msg("Details cannot be added to %s." % self.obj)
            return
        for key in self.lhs.split(";"):
            # loop over all aliases, if any (if not, this will just be
            # the one key to loop over)
            self.obj.set_detail(key, self.rhs)
        self.caller.msg("Detail added: '%s': '%s'" % (self.lhs, self.rhs))


class CmdRoomLookDetail(default_cmds.CmdLook):
    """
    looks at the room and on details
    Usage:
        look <obj>
        look <room detail>
        look *<account>
    Observes your location, details at your location or objects
    in your vicinity.
    Tutorial: This is a child of the default Look command, that also
    allows us to look at "details" in the room.  These details are
    things to examine and offers some extra description without
    actually having to be actual database objects. It uses the
    return_detail() hook on TutorialRooms for this.
    """

    # we don't need to specify key/locks etc, this is already
    # set by the parent.
    help_category = "TutorialWorld"

    def func(self):
        """
        Handle the looking. This is a copy of the default look
        code except for adding in the details.
        """
        caller = self.caller
        args = self.args
        if args:
            # we use quiet=True to turn off automatic error reporting.
            # This tells search that we want to handle error messages
            # ourself. This also means the search function will always
            # return a list (with 0, 1 or more elements) rather than
            # result/None.
            looking_at_obj = caller.search(
                args,
                # note: excludes room/room aliases
                candidates=caller.location.contents + caller.contents,
                use_nicks=True,
                quiet=True,
            )
            if len(looking_at_obj) != 1:
                # no target found or more than one target found (multimatch)
                # look for a detail that may match
                detail = self.obj.return_detail(args)
                if detail:
                    self.caller.msg(detail)
                    return
                else:
                    # no detail found, delegate our result to the normal
                    # error message handler.
                    _SEARCH_AT_RESULT(looking_at_obj, caller, args)
                    return
            else:
                # we found a match, extract it from the list and carry on
                # normally with the look handling.
                looking_at_obj = looking_at_obj[0]

        else:
            looking_at_obj = caller.location
            if not looking_at_obj:
                caller.msg("You have no location to look at!")
                return

        if not hasattr(looking_at_obj, "return_appearance"):
            # this is likely due to us having an account instead
            looking_at_obj = looking_at_obj.character
        if not looking_at_obj.access(caller, "view"):
            caller.msg("Could not find '%s'." % args)
            return
        # get object's appearance
        caller.msg(looking_at_obj.return_appearance(caller))
        # the object's at_desc() method.
        looking_at_obj.at_desc(looker=caller)
        return