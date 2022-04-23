import type { NextPage } from 'next'

const Login: NextPage = () => {
  return (
    <div className='area'>
      <h1>Login</h1>
      <form method="POST">
        <div className="form-group">
          <label htmlFor="user_id" className="form-label">ユーザーID</label>
          <input type="text" name="user_id" className="form-control" />
          <br />
          <label htmlFor="user_password" className="form-label">パスワード</label>
          <input type="password" name="user_password" className="form-control" />
          <br />
          <button type="button" className="btn btn-outline-primary">
            <input type="submit" value="ログイン" />
          </button>
        </div>
      </form>
    </div>
  )
}

export default Login
