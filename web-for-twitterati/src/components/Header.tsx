import { faCircleUser, faHouse, faRightToBracket, faUserPlus, faRightFromBracket } from '@fortawesome/free-solid-svg-icons'
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
  @media screen and (max-width: 537px) {
    flex-flow: column;
  }
`

const IconArea = styled.div`
  display: flex;
  margin: 0 5%;
  color: white;
  align-items: center;
  *{
    cursor: pointer;
  }
`

const Header: VFC = () => {
  return (
    <>
      <HeaderWrapper>
        <Title>オヤの立ち入りにオヤガード</Title>
        <div className='btn-area'>
          <IconArea>
            <Link href="/user/login">
              <FontAwesomeIcon icon={faRightToBracket} />
            </Link>
          </IconArea>
          <IconArea>
            <Link href="/user/signup">
              <FontAwesomeIcon icon={faUserPlus} />
            </Link>
          </IconArea>
          <IconArea>
            <Link href="/user/index">
              <FontAwesomeIcon icon={faCircleUser} />
            </Link>
          </IconArea>
          <IconArea>
            <Link href="/user/logout">
            <FontAwesomeIcon icon={faRightFromBracket} />
            </Link>
          </IconArea>
          <IconArea>
            <Link href="/">
              <FontAwesomeIcon icon={faHouse} />
            </Link>
          </IconArea>
        </div>
      </HeaderWrapper>
      <div className='row-line' />
    </>
  )
}

export default Header
