import type { NextPage } from 'next'
import Link from 'next/link'
import { useEffect, useState } from 'react';

const SignUp: NextPage = () => {
  // db connect
  const [users, setUsers] = useState([]);
  useEffect(()=>{
    fetch('http://localhost:3000/user',{
      headers : {
        'Content-Type':'application/json'
      }
    })
    .then(response => response.json())
    .then(response => setUsers(response))
    .catch(error => console.log(error))

  }, [])

  return (
    <div className="area">
      <Link href="/user/edit">{users}さんの情報</Link>
      <h1>あなたの参加しているグループ</h1>
      <div className="link-area">
        <Link href="/group/new">グループ作成</Link>
      </div>
    </div>
  )
}

export default SignUp
