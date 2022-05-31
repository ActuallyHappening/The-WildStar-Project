import machine
import uasyncio as asio

from .Commands import Command


async def blink_led(led, /, period=0.5, *, logger=print, condition=lambda: True):
    logger(f"Blinking LED {led} every {period} seconds")
    while condition():
        led.on(period)
        await asio.sleep(period)
        led.off(period)
        await asio.sleep(period)


async def blink_pin(number, /, *args, **kwargs):
    led = machine.Pin(number, machine.Pin.OUT)
    await blink_led(led, *args, **kwargs)


async def blink_builtin(*args, **kwargs):
    await blink_pin(machine.c["TEST_BUILTIN"], *args, **kwargs)


async def blink_red(*args, **kwargs):
    await blink_pin(machine.c["TEST_RED"], *args, **kwargs)


async def blink_yellow(*args, **kwargs):
    await blink_pin(machine.c["TEST_YELLOW"], *args, **kwargs)


async def blink_green(*args, **kwargs):
    await blink_pin(machine.c["TEST_GREEN"], *args, **kwargs)


async def blink_blue(*args, **kwargs):
    await blink_pin(machine.c["TEST_BLUE"], *args, **kwargs)

commands = {
    "Blink Builtin": Command(blink_builtin, lambda: None),
    "Blink Red": Command(blink_red, lambda: None, "Blink Red"),
    "Blink Yellow": Command(blink_yellow, lambda: None, "Blink Yellow"),
    "Blink Green": Command(blink_green, lambda: None, "Blink Green"),
    "Blink Blue": Command(blink_blue, lambda: None, "Blink Blue"),
}
