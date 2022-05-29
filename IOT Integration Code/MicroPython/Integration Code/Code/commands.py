import time
import machine
import uasyncio as asio


class Command():
    def __init__(self, _project, _action, _input, _task, _cleanUp):
        self.project = _project
        self.action = _action
        self.input = _input
        self.task = _task
        self.cleanUp = _cleanUp


commands = []


async def _execute(commands):
    print("_Executing ...")
    for command in commands:
        print("\t Making Task ...")
        asio.create_task(command.task(command.input))
    print("Holding tasks ...")
    await asio.sleep(10)
    print("Releasing tasks ...")
    for command in commands:
        command.cleanUp()


def execute_command(_project, _action, _input, *, logger=print):
    global commands
    print(f"Handling Command: {_project} {_action} {_input}")
    if _project == "Project Alpha":
        if _action == "flash_builtin":
            try:
                _input = int(_input)
            except ValueError:
                print("$ Input given is not an integer, defaulting to 1")
                _input = 1
            print(f"Executing LED Builtin Flash at {_input} per second ...")
            #logger(f"Executing LED Builtin Flash at {_input} per second ...")

            async def builtin_flash(_input):
                await blink(_input, machine.Pin(2, machine.Pin.OUT))

            def builtin_flash_cleanup():
                pin = machine.Pin(2, machine.Pin.OUT)
                pin.off()
            commands.append(Command(_project, _action, _input,
                            builtin_flash, builtin_flash_cleanup))
            print(f"Commands: {commands}")
            asio.run(_execute(commands))
        elif _action == "pin_live_byte":
            async def pin_live_byte(_input):
                pin = machine.Pin(int(_input), machine.Pin.OUT)
                pin.on()
                await asio.sleep(1)
                pin.off()
                await asio.sleep(1)


async def blink(perSec, led):
    sleep_period = perSec
    #led = machine.Pin(2, machine.Pin.OUT)
    stateCount = 0
    while True:
        stateCount += 1
        print(f"Blinking {led} ({stateCount}) for {sleep_period}...")
        led.on()
        await asio.sleep(sleep_period)
        led.off()
        await asio.sleep(sleep_period)