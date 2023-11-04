import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import SidebarComponents from './componets/sidebar'
import Home from './componets/home'
import { AuthProvider } from './context/AuthContext'
import LoginPage from './pages/loginPage'
import DashBoard from './pages/dashboard'


function App() {
 return (
    <>
      
      <Router>
        <AuthProvider>
          <main className='flex max-sm:bg-white'>
            <SidebarComponents/>
            <Routes>
              <Route exact path='/dashboard' element={<DashBoard/>} />
            </Routes>
            <Routes>
              <Route path='/' element={<LoginPage/>}/>
            </Routes>

        
          </main>
          </AuthProvider>  
      </Router>
     

    </>
  )
}

export default App
