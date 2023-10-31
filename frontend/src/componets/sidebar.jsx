import { Sidebar, Menu, MenuItem} from 'react-pro-sidebar';
import { Link } from 'react-router-dom';
import {sidebarClasses, menuClasses} from 'react-pro-sidebar'
import { Typography, Container } from '@mui/material';
import tickets from '../images/tickets.png'
import overview from '../images/overview.png'
import subscription from '../images/subscription.png'
import MenuOpenIcon from '@mui/icons-material/MenuOpen';
import {useState} from 'react'
import LightbulbIcon from '@mui/icons-material/Lightbulb';
import GroupsIcon from '@mui/icons-material/Groups';
import PersonIcon from '@mui/icons-material/Person';
import ArticleIcon from '@mui/icons-material/Article';
import SettingsIcon from '@mui/icons-material/Settings';
import Home from './home';

function SidebarComponents() {
    const [collapse, setCollapse] = useState(true)

  return (
    <>
        
        <Sidebar
            rootStyles={{
                [`.${sidebarClasses.container}`]: {
                    backgroundColor: '#363740',
                    color: 'gray'
                },
            }}
            className='fixed'
            width='280px'
            toggled = {true}
            collapsed = {collapse}
            collapsedWidth='120px'
            breakPoint='md'
            
        >
            <Menu
                
                rootStyles={{
                    [`.${menuClasses.container}`]: {
                        color: 'white'
                    },
                }}

            className=''>
                
                <Container className='mb-[3rem] mt-[0rem] pt-6 h-fit flex flex-col'>
                    <div className='flex flex-row space-x-6'>
                        <div className='relative '>
                            <div className='w-12 h-12 rounded-3xl bg-[#3751FF]'></div>
                            <Typography 
                            className='text-lg text-white absolute top-[-0.2rem] left-2' 
                            variant='h3'>D</Typography>                     
                        </div>
                        <Typography 
                        className='text-sm pt-3' variant='h5'>
                            {collapse ? null : 'DashBoard Kit'}
                        </Typography>
                    </div>
                </Container>

            
                <Container className='text-gray cursor-pointer hover:text-[#b6c8d9]'>
                    <MenuOpenIcon className='mb-10 ml-6' onClick = {() => setCollapse(!collapse)}/>
                </Container>  
                        
            </Menu>

            
            <Menu
                menuItemStyles={{
                button: {
                    // the active class will be added automatically by react router
                    // so we can use it to style the active menu item
                    [`&.active`]: {
                    backgroundColor: 'black',
                    color: '#b6c8d9',
                    },
                },
                }}
            >
                <MenuItem component='home'>
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <img src={overview} alt='' className='object-contain'/>
                            <Typography variant='h6'>{collapse ? null : 'Overview'}</Typography>
                        </div>
                    </Container>
                    
                </MenuItem>
                <MenuItem component='home'>
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <img src={tickets} alt='' className='object-contain'/>
                            <Typography variant='h6' className='text-lg'>{collapse ? null : 'Tickets'}</Typography>
                        </div>    
                    </Container> 
                </MenuItem>
                <MenuItem component='home'>
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <LightbulbIcon/>
                            <Typography variant='h6' className='text-lg'>
                                {collapse ? null : 'Ideas'}</Typography>
                        </div>    
                    </Container> 
                </MenuItem>
                <MenuItem component='home'>
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <GroupsIcon/>
                            <Typography variant='h6' className='text-lg'>
                                {collapse ? null : 'Contacts'}</Typography>
                        </div>    
                    </Container> 
                </MenuItem>
                <MenuItem component='home'>
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <PersonIcon/>
                            <Typography variant='h6' className='text-lg'>
                                {collapse ? null : 'Agents'}</Typography>
                        </div>    
                    </Container> 
                </MenuItem>
                <MenuItem component='home'>
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <ArticleIcon/>
                            <Typography variant='h6' className='text-lg'>
                                {collapse ? null : 'Article'}</Typography>
                        </div>    
                    </Container> 
                </MenuItem>
            </Menu>
            
            <Menu
                menuItemStyles={{
                button: {
                    // the active class will be added automatically by react router
                    // so we can use it to style the active menu item
                    [`&.active`]: {
                    backgroundColor: 'black',
                    color: '#b6c8d9',
                    },
                },
                }}
                className='mt-[5rem]'
            >
                <MenuItem component='home'>
                        <Container>
                        <div className='flex flex-row space-x-4'>
                            <SettingsIcon/>
                            <Typography variant='h6' className='text-lg'>
                                {collapse ? null : 'Settings'}</Typography>
                        </div>    
                    </Container>
                </MenuItem>

                <MenuItem component='home'>                    
                    <Container>
                        <div className='flex flex-row space-x-4'>
                            <img src={subscription} alt='' className='object-contain'/>
                            <Typography variant='h6' className='text-lg'>{collapse ? null : 'Subscription'}</Typography>
                        </div>    
                    </Container> 
                </MenuItem>
                
            </Menu>
        
        </Sidebar>

    </>
  )
}

export default SidebarComponents
