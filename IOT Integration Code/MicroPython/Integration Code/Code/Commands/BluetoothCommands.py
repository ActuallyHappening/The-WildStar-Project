from .command import Command, _timeoutWrapper
from Bluetooth import ble_uart_peripheral as ble_DO


def _bluetoothCallback(msg): return print(
    f"$< BluetoothCommands received: {msg}")


__uart = None


def dualUartPrint(msg, *, defaultPrint=print, shouldDefaultPrint=True, __prefix__="$> dualUartPrint"):
    if shouldDefaultPrint:
        defaultPrint(f"{__prefix__}: {msg}")
    if __uart:
        __uart.write(f"{__prefix__}: {msg}\n")


@_timeoutWrapper
async def send(*, logger=print, **kwargs):


@_timeoutWrapper
async def begin(*, logger=print, **kwargs):
    global __uart
    uart = ble_DO._begin(callback=_bluetoothCallback)
    uart.write(str("$> Beginning BluetoothCommands.py bluetooth ...") + '\n')

    __uart = uart
    return uart

commands = {
    "Bluetooth Begin": Command(begin),
    "Bluetooth Send": Command(send),
}
