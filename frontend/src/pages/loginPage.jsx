import { useContext } from "react"
import AuthContext from "../context/AuthContext"
function LoginPage() {
    const {login, error} = useContext(AuthContext)
  return (
    <div className="ml-20 mt-8 place-content-center sm:ml-[10rem]">
        <h5>{error ? error : null}</h5>               
        <form onSubmit={login}>
            <div className="mb-6">
                <label htmlFor="email" className="form-label">Your email</label>
                <input type="email" id="email" className="form-input" placeholder="name@flowbite.com" name= 'email' required />
            </div>
            <div className="mb-6">
                <label htmlFor="password" className="form-label">Your password</label>
                <input type="password" id="password" className="form-input" name="password" required />
            </div>
            <div className="flex items-start mb-6">
                <div className="flex items-center h-5">
                    <input id="remember" type="checkbox" value="" className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800" required/>
                </div>
                <label htmlFor="remember" className="ml-2 text-sm font-medium text-gray-900 
                dark:text-gray-300">Remember me</label>
            </div>
            <button type="submit" className="text-white bg-blue-700 hover:bg-blue-800 
            focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium 
            rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 
            dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
        </form>

      
    </div>
  )
}

export default LoginPage

