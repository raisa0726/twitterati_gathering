import type { NextPage } from 'next'
import { useEffect } from 'react';
import { useState } from 'react';

const [users, setUsers] = useState([]);

useEffect(()=>{
  fetch('http://localhost:3000/login',{
    'methods':'POST',
    headers : {
      'Content-Type':'application/json'
    }
  })
  .then(response => response.json())
  .then(response => setUsers(response))
  .catch(error => console.log(error))

}, [])

const Login: NextPage = (props) => {
  return(
    props.users && props.users.map(users => {
      return (
        <div className='area'>
          <h1>Login</h1>
          <form method="POST">
            <div className="form-group">
              <div className='form-child'>
                <label htmlFor="user_id" className="form-label">ユーザーID</label>
                <input type="text" name="user_id" className="form-control" />
              </div>
              <div className='form-child'>
                <label htmlFor="user_password" className="form-label">パスワード</label>
                <input type="password" name="user_password" className="form-control" />
              </div>
              <div className='form-child'>
                <button type="button" className="btn-submit">
                  <input type="submit" value="ログイン" />
                </button>
              </div>
            </div>
          </form>
        </div>
      )
    }
  )
}

export default Login
