// import React from 'react'
import { useContext } from "react"
import AuthContext from "../context/AuthContext"

function Home() {
  var {name} = useContext(AuthContext)
  return (
    <div>
        hello {name}
    </div>
  )
}

export default Home
