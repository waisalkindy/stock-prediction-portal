import React from 'react'

const Register = () => {
  return (
    <>
    <div className='container'>
      <div className='row justify-content-center'>
        <div className='col-md-6 bg-light-dark p-5 rounded'>
          <h3 className='text-light text-center mb-4'>Create an account</h3>
          <form>
            <input type="text" className='form-control mb-3' placeholder='Username'/>
            <input type="email" className='form-control mb-3' placeholder='Email address' />
            <input type="password" className='form-control mb-5' placeholder='Set password' />
            <button type='submit' className='btn btn-info d-block mx-auto'>Register</button>
          </form>
        </div>
      </div>
    </div>
    </>
  )
}

export default Register
