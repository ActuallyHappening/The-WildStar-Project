import React from 'react'
import { ReactSVG } from 'react-svg'
import BasicBoardDiagram from '../static/images/Basic Board Diagram.svg'

const Device = ({
  __meta__ = { from: "<from>" },//: { [from: string]: string } | null,
  info = { deviceName: "ESP32 - __" },
  display = { tooltip: "Tooltip :)", icon: BasicBoardDiagram },
}) => {
  display.tooltip = display.tooltip ?? info.deviceName
  display.icon = display.icon ?? BasicBoardDiagram
  return (
    <div className='sidebar-icon hover:sidebar-icon-hovered'>
      <h1>
        {info.deviceName} Device!
      </h1>
      <ReactSVG src={display.icon} />
      <span className='sidebar-icon-tooltip'>
        {display.tooltip}
      </span>
    </div>
  )
}

export default Device