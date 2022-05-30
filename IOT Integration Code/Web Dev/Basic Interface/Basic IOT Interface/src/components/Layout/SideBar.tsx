import React from 'react'
import DeviceIcon from '../Device'

const SideBar = ({
  children
}) => {
  return (
    <div className='top-0 left-0 h-screen p-4 m-0 w-auto flex flex-col shadow-lg bg-primary text-secondary'>
      <h1>SideBar:</h1>
      {children}
    </div>
  )
}

export default SideBar