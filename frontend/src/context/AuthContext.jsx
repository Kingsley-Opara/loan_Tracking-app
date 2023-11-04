import { createContext, useState } from "react";
import setCookie from "../utilis/setcookie";
import { jwtDecode } from "jwt-decode";


const endpoint = 'http://localhost:8000/api/user/login/'

const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({children}) =>{
    const [error, setError] = useState(null)
    const fetcher = async (e) =>{
        
        e.preventDefault()
        console.log('heyy')

        const options = {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'email': e.target.email.value, 'password': e.target.password.value})
        }
        const requestLogin = await fetch(endpoint, options)
        const results = await requestLogin.json()
        const data = await results.token
        const decodeToken = data ? jwtDecode(data) : null
        const username = decodeToken && decodeToken.username
        username && setCookie('username', username, 60 )
        console.log(username)
        const errorMsg = await results.detail

        if (errorMsg != null){
            // error = await results.detail
            // console.log(error
            setError(errorMsg)
            console.log(error)
        }
        


    }
    
    const authData = {
        'login': fetcher,
        'error': error,
        
    }
    return(
        <AuthContext.Provider value ={authData}>
            {children}
        </AuthContext.Provider>
    )

}

