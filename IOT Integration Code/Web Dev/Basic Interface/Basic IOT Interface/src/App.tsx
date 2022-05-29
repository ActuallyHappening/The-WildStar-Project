import { useState } from 'react'
import Device from './components/Device'
import SideBar from './components/Layout/SideBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex">
      App:

      <SideBar>
        <Device __meta__={{ from: "discord" }}></Device>
      </SideBar>
    </div>
  )
}

export default App
