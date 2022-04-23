import type { NextPage } from 'next'
import { Props } from 'next/script'

const UserEdit: NextPage<Props> = ({ families }) => {
  return (
    <div className='area'>
      <h1>編集画面</h1>
      <form method="POST">
        <div className="form-group">
          <label htmlFor="name" className="form-label">名前</label>
          <input type="text" name="name" className="form-control" value={{ families.name }} />
          <br />
          <button type="button" className="btn btn-outline-primary">
            <input type="submit" value="更新" />
          </button>
        </div>
      </form>
    </div>
  )
}

export default UserEdit
