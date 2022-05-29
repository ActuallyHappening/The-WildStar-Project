import React from 'react'
import { ReactSVG } from 'react-svg'
import BasicBoardDiagram from '../static/images/Basic Board Diagram.svg'

const DeviceConnection = (() => {
  const http = require('http').createServer()
  const io = require('socket.io')(http, {
    cors: { origin: "*" }
  })

  io.on('connection', (socket) => {
    console.log('a user connected')

    socket.on('message', (data) => {
      console.log('Message Received! :: ', data)

      io.emit('message', {
        message: 'Hello World!'
      });
    });

    socket.on('disconnect', () => {
      console.log('user disconnected')
    });
  });

  return (
    <div className='scale-0'>

    </div>
  )
})

const DeviceIcon = ({
  __meta__ = { from: "<from>" },//: { [from: string]: string } | null,
  info = { deviceName: "__" },
  display = { tooltip: undefined, icon: BasicBoardDiagram },
  children
}) => {
  display.tooltip = display.tooltip ?? info.deviceName
  display.icon = display.icon ?? BasicBoardDiagram
  return (
    <div className='sidebar-icon hover:sidebar-icon-hovered group'>
      <h1>
        {info.deviceName}
      </h1>
      <ReactSVG src={display.icon} />
      <span className='sidebar-icon-tooltip group-hover:scale-100'>
        {display.tooltip}
      </span>
    </div>
  )
}




export default DeviceIcon