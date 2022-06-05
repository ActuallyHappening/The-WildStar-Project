import json
from microdot import Microdot
import secrets

app = Microdot()

_test = json.dumps({"__meta__": {"from": f"<ESP32 id:{secrets.get_esp_id()}",
                   "to": "receiver", "device": "ESP32"}, "payload": {}})


@app.route('/')
def dump(request):
    print("YIPEE!")
    return _test


print("Running Server (imported) ...")
app.run(host='0.0.0.0', port=420, debug=True)
