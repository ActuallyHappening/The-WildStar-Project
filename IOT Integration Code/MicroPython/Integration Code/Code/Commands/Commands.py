import time
import uasyncio as asio

from . import MachineCommands


class Command():
    def __init__(self, aDo, cleanup, name=None):
        self.do = aDo
        self.cleanup = cleanup


prebuilt = dict()


def importSet(commands):
    for name, command in commands.items():
        prebuilt[name] = command


importSet(MachineCommands.commands)


async def execute(commands, time=10):
    if type(commands) is not list:
        # Executing a single task, just put it in a list for simplicity
        commands = [commands]
    # Execute given list of commands
    print(f"## Executing ({len(commands)} num. tasks) ...")
    for command in commands:
        print(
            f"#\t  Making Task {str(command.name)+' ' if command.name is not None else ''}...")
        asio.create_task(command.aDo())
    print(f"## Holding tasks ({time} seconds) ...")
    await asio.sleep(time)
    print("## Releasing tasks ...")
    for command in commands:
        command.cleanup()
