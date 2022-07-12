from Commands import Commands as cmds
from Helper import networking



def ThetaHandler(msg, logger=print, **kwargs):
    logger(f"$< BluetoothCommands Project THETA received: {msg}")
    if msg[:5] == "Blink":
        cmds.execute(cmds.prebuilt["Machine Blink Builtin"], time=int(msg[5:]))

# cmds.execute(cmds.prebuilt["npm run dev"])
cmds.execute(cmds.prebuilt["Bluetooth Project Theta"], __constructor__=ThetaHandler)

