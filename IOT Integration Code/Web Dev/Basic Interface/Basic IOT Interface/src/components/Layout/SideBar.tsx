import React from 'react'
import Device from '../Device'

const SideBar = ({
  children
}) => {
  return (
    <div className='fixed top-0 left-0 h-screen p-4 m-0 w-[10%] flex flex-col shadow-lg bg-primary text-secondary'>
      <h1>SideBar:</h1>
      {children}
    </div>
  )
}

export default SideBar