import { useState } from 'react'
import Device from './components/Device'
import SideBar from './components/Layout/SideBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="flex">
      <SideBar><Device></Device></SideBar>

    </div>
  )
}

export default App
