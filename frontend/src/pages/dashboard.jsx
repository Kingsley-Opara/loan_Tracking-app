import logo from '../images/logo.jpg'
// import Container, { Typography } from '@mui/material'
import { Typography, Container } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import notification from "../images/new.png"
import vertical from "../images/vertical.png"
import jones from "../images/jones.png"


function DashBoard() {
  return (
    <>
        <main className = "h-[100vh] mt-8 ml-20 w-[100vw] sm:ml-[10rem]">
            <div className='flex space-x-[44rem] '>
                <div className=''>
                    <Typography variant='h5' className='font-bold'>DashBoard</Typography>
                </div>
                <div className='flex space-x-4 mt-1 place-content-evenly'>
                    <SearchIcon className='cursor-pointer text-[gray] mt-3'/>
                    <img src={notification} alt='' className='object-contain cursor-pointer'/>
                    <img src={vertical} alt='' className='object-contain cursor-pointer'/>
                    <p className='font-light mt-2 pt-2'>Jones Ferdinand</p>
                    <img src={jones} alt='' className='object-contain cursor-pointer'/>
                    
                </div>


            </div>
            

        </main>

    </>
  )
}

export default DashBoard;
