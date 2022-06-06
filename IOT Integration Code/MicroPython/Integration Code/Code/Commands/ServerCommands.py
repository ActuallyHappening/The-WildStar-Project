import json
from microdot import Microdot
from microdot_asyncio import Microdot as asio_Microdot
import secrets
from . import Commands
from .command import Command, _timeoutWrapper, timeoutWrapper

app = Microdot()
asio_app = asio_Microdot()

API_CONST = "/api/v1"

_test = json.dumps({"__meta__": {"from": f"<ESP32 id:{secrets.get_esp_id()}",
                   "to": "receiver", "device": "ESP32"}, "payload": {}})


@app.route('/')
@asio_app.route('/')
async def dump(request, methods=["GET"]):
    print("YIPEE!")
    return _test


@app.route(f"{API_CONST}/execute-command/")
@asio_app.route(f'{API_CONST}/execute-command/')
async def request_execute_command(request):
    print("## Command requested ...")
    if "prebuilt" in request.args:
        if request.args["prebuilt"] not in Commands.prebuilt:
            return f"Error Code 50something\nUnknown command {request.args['prebuilt']=}"
        requested_command = Commands.prebuilt[request.args["prebuilt"]]
        _time = 5
        if "time" in request.args:
            _time = int(request.args["time"])
        else:
            print(f"#>\tDefaulting to {_time=}")
        print(f"### Executing task {requested_command.name}")
        try:
            Commands.execute(requested_command, time=_time)
        except Exception as exc:  # Dangerous, will update to use socket.timeout TODO
            print(
                f"#< request_execute_command with {API_CONST=} closed ({exc=})")
        print("### Returning control to ServerCommands ...")
        return f"GOOD executed task! For {_time=}"
    else:
        return "Error Code 40something\nUnknown options, use `.../execute-command/?prebuilt=Blink Builtin`\nWOW this API is COOL AS F**K!"


@app.route(f"{API_CONST}/find-commands/<str:command_name>")
@asio_app.route(f"{API_CONST}/find-commands/<command_name>")
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
async def asio_start_server():
    try:
        print(f"#>\tStarting microdot server --async ...")
        await asio_app.start_server(host='0.0.0.0', port=420, debug=True)
    finally:
        asio_app.shutdown()
        print(f"#>\tShutdown microdot server --async")


@timeoutWrapper
def start_server():
    try:
        print(f"#>\tStarting microdot server --sync ...")
        app.run(host='0.0.0.0', port=420, debug=True)
    finally:
        app.shutdown()
        print(f"#>\tShutdown microdot server --sync ...")


commands = {
    "npm run dev --async": Command(asio_start_server),
    "npm run dev": Command(asio_start_server),
    "npm run dev --sync": Command(start_server),
}
