import React, { FC, useEffect, useState } from 'react'
import { io } from "socket.io-client"

interface ServerConnectionProps {
  endpoint?: string
}

const ServerConnection: FC<ServerConnectionProps> = (props) => {

  //const [response, setResponse] = useState('')
  const [connState, setConnState] = useState<string>('Not Started')

  useEffect(() => {
    const socket = io("http://localhost:3001")
    setConnState("Starting ...")
    socket.on('connect', () => {
      console.log('connected')
      setConnState("Connected")
    })
    socket.on('error', (err) => {
      console.log('error', err)
      setConnState("Error")
    })
    socket.on('reconnect', () => {
      console.log('reconnect')
      setConnState("Reconnected")
    })
    socket.on('reconnect_attempt', () => {
      console.log('reconnect_attempt')
      setConnState("Reconnecting ...")
    })
    socket.on('reconnect_error', (err) => {
      console.log('reconnect_error', err)
      setConnState("Reconnect Error!")
    })
    socket.on('reconnect_failed', () => {
      console.log('reconnect_failed')
      setConnState("Reconnect Failed")
    })
    socket.on('ping', () => {
      console.log('ping')
      setConnState("Pinged!")
    })
  }, [props.endpoint])

  return (
    <div className='mg-auto'>
      <h1>OH oh, this should never show</h1>
      <h2>{connState}</h2>
    </div>
  )
}

export default ServerConnection