import React from 'react'
import { ReactSVG } from 'react-svg'
import BasicBoardDiagram from '../static/images/Basic Board Diagram.svg'

const Device = ({
  __meta__,//: { [from: string]: string } | null,
  info,
}) => {
  return (
    <div className='rounded-[50px] p-5 text-white bg-black'>
      <h1>
        {info.deviceName} Device!
      </h1>
      <ReactSVG src={BasicBoardDiagram} />
    </div>
  )
}

export default Device