import React, { useEffect } from 'react'
import { ReactSVG } from 'react-svg'
import BasicBoardDiagram from '../static/images/Basic Board Diagram.svg'
import wsInit from './Connections'

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
      {children}
    </div>
  )
}


export default DeviceIcon