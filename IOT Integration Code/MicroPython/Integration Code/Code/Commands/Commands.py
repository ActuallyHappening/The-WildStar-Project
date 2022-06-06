import time
import uasyncio as asio

from . import MachineCommands
from . import TimeCommands
from . import ServerCommands
from .command import Command as CommandClass

prebuilt = dict()


async def _timeoutWrapper(coroutine):
    async def __timeoutWrapper(*_args, time=..., **_kwargs):
        if time is not ...:
            await asio.wait_for(coroutine(*_args, **_kwargs), timeout=time)
        else:
            print(
                f"#>\tRunning __timeoutWrapper with no given time, defaulting to asio.gather(...)")
            await asio.gather(coroutine(*_args, **_kwargs))
    return __timeoutWrapper


def importSet(commands):
    for name, command in commands.items():
        prebuilt[name] = _timeoutWrapper(command)
        if command.name is None:
            command.name = name  # Set name of command to handle used to call it :)


importSet(MachineCommands.commands)
importSet(TimeCommands.commands)
importSet(ServerCommands.commands)


async def _execute(commands, time=..., **overflow):
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
            continue
        print(
            f"#\tMaking Task {str(command.name)+' ' if hasattr(command,'name') else '__'}...")
    if time is ...:
        print(f"#> Note: {time=}, is not set, running until completion")
    print(f"## Holding tasks ({time} seconds) ...")
    await asio.gather(*[task.asioDo(time=time) for task in commands])
    print("## Released tasks.")


def execute(*args, **kwargs):
    asio.run(_execute(*args, **kwargs))
