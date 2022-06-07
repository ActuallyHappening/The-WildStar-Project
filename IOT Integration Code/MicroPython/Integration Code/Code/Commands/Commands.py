import time
import uasyncio as asio

from . import MachineCommands
from . import TimeCommands
from . import ServerCommands
from .command import Command as CommandClass

prebuilt = dict()


def importSet(commands):
    for name, command in commands.items():
        prebuilt[name] = command
        if command.name is None:
            # Set name of command to handle used to call it :)
            command.name = str(name)


importSet(MachineCommands.commands)
importSet(TimeCommands.commands)
importSet(ServerCommands.commands)


async def _execute(commands, *, time=..., **overflow):
    if len(overflow) > 0:
        print(f"OH oh, overflow detected in func _execute: {overflow=}")
    if type(commands) is not list:
        # Executing a single task, just put it in a list for simplicity
        commands = [commands]
    # Execute given list of commands
    print(f"## Executing ({len(commands)} num. tasks) ...")
    for command in commands:
        if type(command) is not CommandClass:
            print("## ERROR: Command is not of type CommandClass")
            return
        print(
            f"#\tMaking Task {str(command.name)+' ' if hasattr(command,'name') else '__'}...")
    if time is ...:
        print(f"#> Note: {time=}, is not set, running until completion")
    print(f"## Holding tasks ({time=} seconds) ...")
    await asio.gather(*[command.asioDo(time=time) for command in commands])
    print("## Released tasks.")


def execute(*args, **kwargs):
    asio.run(_execute(*args, **kwargs))
