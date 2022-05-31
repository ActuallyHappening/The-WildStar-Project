import time
import machine
import uasyncio as asio


class Command():
    def __init__(self, aDo, aCleanup):
        self.do = aDo
        self.cleanup = aCleanup


commands = []


async def _execute(commands, time=10):
    print("## Executing ...")
    for command in commands:
        print("\t Making Task ...")
        asio.create_task(command.aDo())
    print("## Holding tasks ...")
    await asio.sleep(time)
    print("## Releasing tasks ...")
    for command in commands:
        command.aCleanup()
