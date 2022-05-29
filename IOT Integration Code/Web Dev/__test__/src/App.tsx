import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='TopLevel bg-green-50 text-center'><p>Yay!</p></div>
  )
}

export default App
