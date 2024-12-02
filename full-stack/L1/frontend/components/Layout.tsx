import React, { useState } from 'react'
import Container from '@mui/material/Container'
import NavBar from './NavBar'
import Sidebar from './Sidebar'

interface LayoutProps {
  children: React.ReactNode
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen)
  }

  return (
    <div className="min-h-screen flex flex-col">
      <NavBar onMenuClick={toggleSidebar} />
      <Sidebar isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />
      <Container className="flex-grow mt-8">
        {children}
      </Container>
    </div>
  )
}

export default Layout

