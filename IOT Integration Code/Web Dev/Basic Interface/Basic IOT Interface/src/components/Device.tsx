import React from 'react'

const Device = ({
  __meta__,//: { [from: string]: string } | null,
  info,
}) => {
  return (
    <div className='rounded-sm'><h1>
      {info.deviceName}
    </h1></div>
  )
}

export default Device