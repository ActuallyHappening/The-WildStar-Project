import time
from .command import Command
import uasyncio as asio


async def time_interval(interval, *, callback, logger=print, forever=True, **overflow):
    """
    Every interval seconds, `await callback()`;
    If `false` is returned and forever is `false`, exit / `return` from loop
    """
    i = 0
    while True:
        asio.sleep(interval)
        i += interval
        if await callback(__passage__=i) and forever:
            return


async def time_logger(interval, *, __prefix__="Time Logged", logger=print, **kwargs):
    await time_interval(interval=interval, callback=lambda __passage__: logger(f"{__prefix__}: {__passage__}"), forever=True, logger=logger, **kwargs)


async def time_trigger(interval, *, logger=print):
    def callback(__passage__):
        logger(f"Time Logged: {__passage__}")
        return False  # Exit since forever=False
    await time_interval(interval=interval, callback=callback, forever=False)


async def second_logger(*, __prefix__="Seconds Logged", logger=print, **kwargs):
    await time_logger(interval=1, callback=lambda __passage__: logger(f"{__prefix__}: {__passage__}"), logger=logger, **kwargs)


async def second_timer(*, __prefix__="Second Triggered", logger=print, **kwargs):
    await time_trigger(interval=1, callback=lambda __passage__: logger(f"{__prefix__}: {__passage__}"), logger=logger, **kwargs)

commands = {
    "Seconds Logger": Command(second_logger),
    "Seconds Timer": Command(second_timer),
}
