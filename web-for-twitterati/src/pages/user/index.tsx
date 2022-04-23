import type { NextPage } from 'next'
import Link from 'next/link'

const SignUp: NextPage = () => {
  return (
    <div className="area">
      <Link href="./edit">個人情報</Link>
      <h1>あなたの参加しているグループ</h1>
      <br />
      <div className="link-area">
        <Link href="/group/new">グループ作成</Link>
      </div>
    </div>
  )
}

export default SignUp
