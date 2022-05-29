import { useState } from 'react'
import Device from './components/Device'
import SideBar from './components/Layout/SideBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex">
      <SideBar>
        <Device __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 1" }} />
        <Device __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 2" }} />
        <Device __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 3" }} />
        <Device __meta__={{ from: "discord" }} info={{ deviceName: "ESP32 - 4" }} />
      </SideBar>
    </div >
  )
}

export default App
