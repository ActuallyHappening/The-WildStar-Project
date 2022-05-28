import time
import machine
import uasyncio as asio


class Command():
    def __init__(self, _project, _action, _input):
        self.project = _project
        self.action = _action
        self.input = _input


commands = []


async def _execute(commands):
    print("_Executing ...")
    tasks = []
    for command in commands:
        tasks += asio.create_task(blink(command.input,
                                  machine.Pin(2, machine.Pin.OUT)))
    for task in tasks:
        print(f"Running task: {task}")
        asio.run(task)


def execute_command(_project, _action, _input, *, logger=print):
    global commands
    if _project == "Project Alpha":
        if _action == "flash_builtin":
            try:
                _input = int(_input)
            except ValueError:
                print("$ Input given is not an integer, defaulting to 1")
                _input = 1
            print("Executing LED Builtin Flash at {_input} per second ...")
            logger("Executing LED Builtin Flash at {_input} per second ...")
            commands += Command(_project, _action, _input)
            _execute(commands)


async def blink(perSec, led):
    sleep_period = (perSec // 2)
    #led = machine.Pin(2, machine.Pin.OUT)
    while True:
        print("Blinking {led} ...")
        led.value(1)
        await asio.sleep(sleep_period)
        led.value(0)
        await asio.sleep(sleep_period)
