import machine
import uasyncio as asio

from .command import Command
from extensions import constants


async def blink_led(led, *, period=0.5, logger=print, finishState=False, **overflow):
    if len(overflow) > 0:
        logger(f"OH oh, overflow detected in func blink_led: {overflow=}")
    print(
        f"blink_led called with args {led=}, {period=}, {logger=}, {finishState=}")
    logger(f"Blinking LED {led=} every {period=} seconds")
    try:
        while True:
            led.on()
            await asio.sleep(period)
            led.off()
            await asio.sleep(period)
    finally:
        led.value(finishState)
        print(f"#< Closing blink_led with {finishState=}, and {led=}")


async def blink_pin(number, **kwargs):
    print(f"blink_pin called with args {number=}, {kwargs=}")
    led = machine.Pin(number, machine.Pin.OUT)
    await blink_led(led, **kwargs)


async def blink_builtin(**kwargs):
    print(f"blink_builtin called with args {kwargs=}")
    await blink_pin(constants["machine"]["TEST_BUILTIN"], **kwargs)


async def blink_red(**kwargs):
    await blink_pin(constants["machine"]["TEST_RED"], **kwargs)


async def blink_yellow(**kwargs):
    await blink_pin(constants["machine"]["TEST_YELLOW"], **kwargs)


async def blink_green(**kwargs):
    await blink_pin(constants["machine"]["TEST_GREEN"], **kwargs)


async def blink_blue(**kwargs):
    await blink_pin(constants["machine"]["TEST_BLUE"], **kwargs)

commands = {
    "Blink Builtin": Command(blink_builtin),
    "Blink Red": Command(blink_red),
    "Blink Yellow": Command(blink_yellow),
    "Blink Green": Command(blink_green),
    "Blink Blue": Command(blink_blue),
}
