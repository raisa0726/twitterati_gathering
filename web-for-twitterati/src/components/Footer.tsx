import { faTwitter } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { VFC } from 'react'
import styled from 'styled-components'

const FooterWrapper = styled.footer`
  display: flex;
  justify-content: space-between;
  padding: 1em;
  background: #3c3c3c;
  width: 100%;
  @media screen and (max-width: 537px) {
    flex-flow: column;
  }
`
const Developers = styled.div`
  display: flex;

  @media screen and (min-width: 537px) {
    align-items: center;
  }
  @media screen and (max-width: 537px) {
    flex-flow: column;
    justify-content: center;
    align-items: center;
  }

  * {
    margin: 0 1em;
    color: #1D9BF0;
  }
`

const Footer: VFC = () => {
  return (
    <FooterWrapper>
      <Developers>
        <FontAwesomeIcon icon={faTwitter} />
        <a href='https://twitter.com/kibidango_py'>@kibidango_py</a>
        <a href='https://twitter.com/kei_r14'>@kei_r14</a>
        <a href='https://twitter.com/yat0i_kit'>@yat0i_kit</a>
        <a href='https://twitter.com/SC_Raisa'>@SC_Raisa</a>
      </Developers>
    </FooterWrapper>
  )
}

export default Footer
