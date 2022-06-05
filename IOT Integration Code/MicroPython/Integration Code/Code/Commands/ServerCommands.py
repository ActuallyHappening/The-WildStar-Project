import json
from microdot_asyncio import Microdot
import secrets
from . import Commands
from .command import Command

app = Microdot()

API_CONST = "/api/v1"

_test = json.dumps({"__meta__": {"from": f"<ESP32 id:{secrets.get_esp_id()}",
                   "to": "receiver", "device": "ESP32"}, "payload": {}})


@app.route('/')
async def dump(request, methods=["GET"]):
    print("YIPEE!")
    return _test


@app.route(f'{API_CONST}/execute-command/')
async def request_execute_command(request):
    print("## Command requested ...")
    if "prebuilt" in request.args:
        requested_command = Commands.prebuilt[request.args["prebuilt"]]
        Commands.execute(requested_command)
        print("## Returning control to ServerCommands ...")
    else:
        return "Error Code 40something\nUnknown options, use `.../execute-command/?prebuilt=Blink Builtin`\nWOW this API is COOL AS F**K!"


async def _start_server():
    app.run(host='0.0.0.0', port=420, debug=True)

commands = {
    "npm run dev": Command(_start_server),
}

if __name__ == "__main__":
    print("Running Server (imported) ...")
    Commands.execute(commands["npm run dev"])
