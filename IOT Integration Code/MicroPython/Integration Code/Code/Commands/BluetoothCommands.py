from .command import Command, _timeoutWrapper
from Bluetooth import ble_uart_peripheral as ble_DO


def _bluetoothCallback(msg): return print(
    f"$< BluetoothCommands received: {msg}")


__uart = None


def dualUartPrint(msg, *, defaultPrint=print, shouldDefaultPrint=True, __prefix__=""):
    if shouldDefaultPrint:
        defaultPrint(f"{__prefix__}{msg}")
    if __uart:
        __uart.write(f"{__prefix__}{msg}\n")


__implicitRetry = False


@_timeoutWrapper
async def send(msg, *, logger=dualUartPrint, **kwargs):
    global __implicitRetry
    logger(f"!> BluetoothCommands send: {msg}")
    if __uart:
        __uart.write(f"{kwargs}\n")
    else:
        if __implicitRetry:
            logger("!!> No uart connected: Already retried! FAILED BLUETOOTH")
            __implicitRetry = False
            return
        logger(f"!> No uart connected: Implicitely beginning bluetooth ...")
        await begin(logger=logger)
        __implicitRetry = True
        await send(msg, logger=logger, **kwargs)


@_timeoutWrapper
async def begin(*, logger=dualUartPrint, **kwargs):
    global __uart
    logger("$> BluetoothCommands Beginning ...")

    __uart = ble_DO._begin(callback=_bluetoothCallback)
    __uart.write(
        str("$> Beginning BluetoothCommands.py (begin) bluetooth ...") + '\n')

    logger("$> Finished BluetoothCommands.py (begin) bluetooth")

commands = {
    "Bluetooth Begin": Command(begin),
    "Bluetooth Send": Command(send),
}
