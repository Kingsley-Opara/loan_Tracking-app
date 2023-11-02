import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import SidebarComponents from './componets/sidebar'
import Home from './componets/home'
import { AuthProvider } from './context/AuthContext'
import LoginPage from './pages/loginPage'


function App() {
 return (
    <>
      
      <Router>
        <AuthProvider>
          <main className='flex max-sm:bg-white'>
            <SidebarComponents/>
            <Routes>
              <Route path='/login' element={<LoginPage/>}/>
            </Routes>
        
          </main>
          </AuthProvider>  
      </Router>
     

    </>
  )
}

export default App
