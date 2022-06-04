import time
from .command import Command
import uasyncio as asio


async def time_interval(interval, *, callback, logger=print, forever=True, **overflow):
    """
    Every interval seconds, `await callback()`;
    If `False` is returned and forever is `False`, exit / `return` from loop
    """
    i = 0
    while True:
        await asio.sleep(interval)
        i += interval
        c = callback(__passage__=i)
        print("values DEBUG:", i, c, forever)
        exit = await c
        if exit is False and forever is False:
            return


async def time_logger(interval, *, __prefix__="Time Logged", logger=print, **kwargs):
    await time_interval(interval=interval, callback=lambda __passage__: logger(f"{__prefix__}: {__passage__}"), forever=True, logger=logger, **kwargs)


async def time_trigger(interval, *, logger=print):
    def callback(__passage__):
        logger(f"Time Logged: {__passage__}")
        return False  # Exit since forever=False
    await time_interval(interval=interval, callback=callback, forever=False)


async def second_logger(*, __prefix__="Seconds Logged", logger=print, **kwargs):
    await time_logger(interval=1, __prefix__=__prefix__, logger=logger, **kwargs)


async def second_timer(*, __prefix__="Second Triggered", logger=print, **kwargs):
    await time_trigger(interval=1, __prefix__=__prefix__, logger=logger, **kwargs)

commands = {
    "Seconds Logger": Command(second_logger),
    "Seconds Timer": Command(second_timer),
}
