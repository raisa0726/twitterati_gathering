import type { NextPage } from 'next'

const SignUp: NextPage = () => {
  return (
    <div className='area'>
      <h1>新規登録</h1>
      <form method="POST">
        <div className="form-group">
          <label htmlFor="user_name" className="form-label">ユーザー名</label>
          <input type="text" name="user_name" className="form-control" />
          <br />
          <label htmlFor="user_password" className="form-label">パスワード</label>
          <input type="password" name="user_password" className="form-control" />
          <br />
          <button type="button" className="btn-submit">
            <input type="submit" value="新規登録" />
          </button>
        </div>
      </form>
    </div>
  )
}

export default SignUp
