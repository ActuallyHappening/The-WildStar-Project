export default function wsInit() {
  console.log("wsInit start")
  const ws = new WebSocket("ws://ws.bitstamp.net");
  const __test__ = {
    "event": "bts:subscribe",
    "data": {
      "channel": "live_trades_btcusd"
    }
  }
  ws.onopen = () => {
    console.log("ws.onopen")
    ws.send(JSON.stringify(__test__))
  }
  ws.onmessage = function (event) {
    const json = JSON.parse(event.data);
    console.log(`[message] Data received from server: ${json}`);
    try {
      if ((json.event = "data")) {
        console.log(json.data);
      }
    } catch (err) {
      // whatever you wish to do with the err
    }
  };
  return () => console.log("wsInit finish")
}