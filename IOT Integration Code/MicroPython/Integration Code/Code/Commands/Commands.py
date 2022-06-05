
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
            command.name = name  # Set name of command to handle used to call it :)


importSet(MachineCommands.commands)
importSet(TimeCommands.commands)
importSet(ServerCommands.commands)


async def _execute(commands, time=10, *, leeWay=1):
    if type(commands) is not list:
        # Executing a single task, just put it in a list for simplicity
        commands = [commands]
    # Execute given list of commands
    print(f"## Executing ({len(commands)} num. tasks) ...")
    for command in commands:
        if type(command) is not CommandClass:
            print("## ERROR: Command is not of type CommandClass")
            continue
        print(
            f"#\t  Making Task {str(command.name)+' ' if hasattr(command,'name') else '__'}...")
        asio.create_task(command.asioDo())
    print(f"## Holding tasks ({time} seconds) ...")
    await asio.sleep(time)
    print(f"## Leeway for {leeWay} ...")
    await asio.sleep(leeWay)
    print("## Releasing tasks ...")
    for command in commands:
        command.cleanup()


def execute(*args, **kwargs):
    asio.run(_execute(*args, **kwargs))
