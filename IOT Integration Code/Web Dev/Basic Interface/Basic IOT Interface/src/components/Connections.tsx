import React, { FC, useEffect, useState } from 'react'
import { io } from "socket.io-client"

interface ServerConnectionProps {
  endpoint?: string
}

const ServerConnection: FC<ServerConnectionProps> = (props) => {

  //const [response, setResponse] = useState('')
  const [time, setTime] = useState<string | number>('fetching ...')

  useEffect(() => {
    const socket = io("http://localhost:3001")
    socket.on('connect', () => {
      console.log('connected')
    })
    socket.on('connect', () => console.log(socket.id))
    socket.on('connect_error', () => {
      setTimeout(() => socket.connect(), 5000)
    })
    socket.on('time', (data) => setTime(data))
    socket.on('disconnect', () => setTime('server disconnected'))
  })

  return (
    <div className=''>
      <h1>OH oh, this should never show</h1>
      <h2>{time}</h2>
    </div>
  )
}

export default ServerConnection