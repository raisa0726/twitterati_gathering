import type { NextPage } from 'next'
import Link from 'next/link'
import styled from 'styled-components'

const Area = styled.div`
  margin: 1em;
`

const Home: NextPage = () => {
  return (
    <Area>
      <h1>Hello! User1</h1>
      <div>
        <Link href="/group">
          グループ一覧
        </Link>
      </div>
    </Area>
  )
}

export default Home
