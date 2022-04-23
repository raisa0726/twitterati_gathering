import { faHouse } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import Link from 'next/link'
import { VFC } from 'react'
import styled from 'styled-components'

const Title = styled.a`
  font-weight: bold;
  font-size: 1.5em;
`
const HeaderWrapper = styled.header`
  display: flex;
  justify-content: space-between;
  padding: 1em;
  align-items: center;
  background: #e2e7ff;
`

const Header: VFC = () => {
  return(
    <HeaderWrapper>
      <Title>オヤの立ち入りにオヤガード</Title>
      <Link href="/">
        <FontAwesomeIcon icon={faHouse} />
      </Link>
    </HeaderWrapper>
  )
}

export default Header
