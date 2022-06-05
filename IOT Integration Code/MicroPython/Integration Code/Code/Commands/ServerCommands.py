import json
from microdot import Microdot
from microdot_asyncio import Microdot as asio_Microdot
import secrets
from . import Commands
from .command import Command

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
        requested_command = Commands.prebuilt[request.args["prebuilt"]]
        _time = 5
        if "time" in request.args:
            _time = request.args["time"]
        print(f"### Executing task {requested_command.name}")
        Commands.execute(requested_command, time=int(_time))
        print("### Returning control to ServerCommands ...")
        return "GOOD executed task!"
    else:
        return "Error Code 40something\nUnknown options, use `.../execute-command/?prebuilt=Blink Builtin`\nWOW this API is COOL AS F**K!"


async def asio_start_server():
    await asio_app.start_server(host='0.0.0.0', port=420, debug=True)


def start_server():
    app.run(host='0.0.0.0', port=420, debug=True)


commands = {
    "npm run dev --async": Command(asio_start_server, lambda: asio_app.shutdown()),
    "npm run dev": Command(start_server, lambda: app.shutdown()),
    "npm run dev --sync": Command(start_server, lambda: app.shutdown()),
}

if __name__ == "__main__":
    print("Running Server (imported) ...")
    Commands.execute(commands["npm run dev"])
