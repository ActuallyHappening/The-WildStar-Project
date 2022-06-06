import json
import uasyncio as asio
from microdot import Microdot
from microdot_asyncio import Microdot as asio_Microdot
import secrets
from . import Commands
from .command import Command, _timeoutWrapper, timeoutWrapper

app = asio_Microdot()

API_CONST = "/api/v1.0"


_test = json.dumps({"__meta__": {"from": f"<ESP32 id:{secrets.get_esp_id()}",
                   "to": "receiver", "device": "ESP32"}, "payload": {}})

commandQueue = []
__queuePollPeriod = 5
__queueStop = False


@app.route('/')
async def dump(request, methods=["GET"]):
    print("YIPEE!")
    return _test


async def __commandQueueTask():
    try:
        while True:
            if len(commandQueue) > 0:
                Commands.execute(commandQueue)
                commandQueue.clear()
            await asio.sleep(__queuePollPeriod)
            if __queueStop:
                __queueStop = False
                break
    except Exception as exc:
        print(f"#<\t__commandQueueTask Stopped: {exc}")


@app.route(f'{API_CONST}/execute-command/')
async def request_execute_command(request):
    print("## Command queue request ...")
    if "prebuilt" in request.args:
        if request.args["prebuilt"] not in Commands.prebuilt:
            return f"Error Code 50something\nUnknown command {request.args['prebuilt']=}"
        requested_command = Commands.prebuilt[request.args["prebuilt"]]
        _time = 5
        if "time" in request.args:
            _time = int(request.args["time"])
        else:
            print(f"#>\tDefaulting to {_time=}")
        print(f"### Queueing task {requested_command.name}")
        commandQueue.append(requested_command)
        return f"GOOD queued {requested_command =} for {_time =}"
    else:
        return "Error Code 40something\nUnknown options, use `.../execute-command/?prebuilt=Blink Builtin`\nWOW this API is COOL AS F**K!"


@app.route(f"{API_CONST}/find-commands/<string:command_name>")
async def request_find_commands(request, *, command_name="*"):
    print(f"##! Command requested ...")
    if command_name == "*":
        return json.dumps({"commands": Commands.prebuilt})
    else:
        try:
            return json.dumps({"commands": Commands.prebuilt[command_name]})
        except KeyError:
            return f"Error Code 50something\nUnknown command {command_name=}"


@_timeoutWrapper
async def start_server():
    try:
        print(f"#>\tStarting microdot server --async ...")
        await asio.gather(__commandQueueTask(), app.start_server(host='0.0.0.0', port=420, debug=True))
    finally:
        app.shutdown()
        print(f"#>\tShutdown microdot server --async")


commands = {
    "npm run dev": Command(start_server),
}
