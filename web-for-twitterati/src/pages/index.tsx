import type { NextPage } from 'next'
import Link from 'next/link'

const Home: NextPage = () => {
  return (
    <div className='area'>
      <h1>Hello! User1</h1>
      <div className='link-area'>
        <Link href="/group">
          グループ一覧
        </Link>
      </div>
    </div>
  )
}

export default Home
