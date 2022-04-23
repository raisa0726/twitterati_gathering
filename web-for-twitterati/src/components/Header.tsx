import { faHouse } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import Link from 'next/link'
import { VFC } from 'react'
import styled from 'styled-components'

const Title = styled.a`
  font-weight: bold;
  font-size: 1.5em;
  color: white;
`
const HeaderWrapper = styled.header`
  display: flex;
  justify-content: space-between;
  padding: 1em;
  align-items: center;
  background: #3c3c3c;
`
const HouseArea = styled.div`
  margin: 0 5%;
  cursor: pointer;
  color: white;
`

const Header: VFC = () => {
  return(
    <HeaderWrapper>
      <Title>オヤの立ち入りにオヤガード</Title>
      <div className='btn-area'>
        <div className="btn btn-flat">
          <Link href="/user/login"><span>Login</span></Link>
        </div>
        <div className="btn btn-flat">
          <Link href="/user/signup"><span>新規登録</span></Link>
        </div>
        <div className="btn btn-flat">
          <Link href="/user/index"><span>ユーザーページ</span></Link>
        </div>
        <div className="btn btn-flat">
          <Link href="/user/logout"><span>ログアウト</span></Link>
        </div>
      </div>
      <HouseArea>
        <Link href="/">
          <FontAwesomeIcon icon={faHouse} />
        </Link>
      </HouseArea>
    </HeaderWrapper>
  )
}

export default Header
