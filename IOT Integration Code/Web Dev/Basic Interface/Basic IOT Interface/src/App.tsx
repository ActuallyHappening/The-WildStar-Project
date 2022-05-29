import { useState } from 'react'
import ServerConnection from './components/Connections'
import DeviceIcon from './components/Device'
import SideBar from './components/Layout/SideBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex">
      <ServerConnection />
      <SideBar>
        <DeviceIcon __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 1" }} />
        <DeviceIcon __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 2" }} />
        <DeviceIcon __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 3" }} />
        <DeviceIcon __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 4" }} />
      </SideBar>
    </div >
  )
}

export default App
