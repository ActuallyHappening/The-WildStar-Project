import React from 'react'

const SideBar = ({ children }) => {
  return (
    <div className='fixed top-2 left-0 h-screen w-16 bg-green-50'>
      {children}
    </div>
  )
}

export default SideBar