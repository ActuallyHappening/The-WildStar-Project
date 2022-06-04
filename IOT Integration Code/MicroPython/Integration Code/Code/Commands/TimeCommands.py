import time
from .command import Command
import uasyncio as asio


async def time_interval(interval, *, callback, logger=print, forever=True, **overflow):
    """
    Every interval seconds, `await callback()`
    If callback is `false` and forever is `false` `return`
    """
    i = 0
    while True:
        asio.sleep(interval)
        i += interval
        if await callback(passage=i) and forever:
            return


async def time_logger(interval, *, logger=print, **kwargs):
    await time_interval(interval=interval, callback=lambda passage: logger(f"Time Logged: {passage}"), forever=True)


async def time_trigger(interval, *, logger=print):
    def callback(passage):
        logger(f"Time Logged: {passage}")
        return False  # Exit since forever=False
    await time_interval(interval=interval, callback=callback, forever=False)

commands = {
    "Seconds Logger": Command(time_logger(1)),
    "Seconds Timer": Command(time_trigger(1)),
}
