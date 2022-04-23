import type { NextPage } from 'next'
import styled from 'styled-components'

const Area = styled.div`
  margin: 1em;
`

const Home: NextPage = () => {
  return (
    <Area>
      <h1>Hello! User1</h1>
    </Area>
  )
}

export default Home
