import React from 'react'

const SideBar = ({ children }) => {
  return (
    <p className='fixed top-2 left-0 h-screen w-16 bg-green-50'>
      <h1>SideBar:</h1>
      {children}
    </p>
  )
}

export default SideBar