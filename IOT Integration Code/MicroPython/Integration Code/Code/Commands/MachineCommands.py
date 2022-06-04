import machine
import uasyncio as asio

from .command import Command
from extensions import constants


async def blink_led(led, *, period=0.5, logger=print, condition=lambda: True, **overflow):
    if len(overflow) > 0:
      logger(f"OH oh, overflow detected in func blink_led: {overflow=}")
    print(f"blink_led called with args {led}, {period}, {logger}, {condition}")
    logger(f"Blinking LED {led} every {period} seconds")
    while condition():
        led.on()
        await asio.sleep(period)
        led.off()
        await asio.sleep(period)


async def blink_pin(number, **kwargs):
    print(f"blink_pin called with args {number}, {kwargs}")
    led = machine.Pin(number, machine.Pin.OUT)
    await blink_led(led, **kwargs)


async def blink_builtin(**kwargs):
    print(f"blink_builtin called with args {kwargs}")
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
    "Blink Builtin": Command(blink_builtin, lambda: None, "Blink Builtin"),
    "Blink Red": Command(blink_red, lambda: None, "Blink Red"),
    "Blink Yellow": Command(blink_yellow, lambda: None, "Blink Yellow"),
    "Blink Green": Command(blink_green, lambda: None, "Blink Green"),
    "Blink Blue": Command(blink_blue, lambda: None, "Blink Blue"),
}
