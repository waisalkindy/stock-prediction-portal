import React, { useContext } from 'react'
import Button from './Button'
import { Link } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'

const Header = () => {
  const {isLoggedIn, setIsLoggedIn} = useContext(AuthContext)
  return (
    <>
      <nav className='navbar container pt-3 pb-3 align-items-start'>
        <Link className='navbar-brand text-light' to="/">Stock Prediction Portal</Link>

        <div>
          {isLoggedIn ? (
            <Button text='Logout' className='btn btn-warning'></Button>
          ) : (
            <>
            <Button text='Login' className='btn-outline-info' url="/login" />
            &nbsp;
            <Button text='Register' className='btn-info' url="/register" />
            </>
          )}

        </div>
      </nav>
    </>
  )
}

export default Header
