import { faTwitter } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { VFC } from 'react'
import styled from 'styled-components'

const FooterWrapper = styled.div`
  display: flex;
  padding: 1em;
  background: #15202B;
  align-items: center;
  width: 100%;
  @media screen and (max-width: 537px) {
    flex-flow: column;
  }
`
const IconArea = styled.div`
  color: #1D9BF0;
  align-items: center;
  display:flex;
  margin: 0.3rem;
`

const Footer: VFC = () => {
  return (
    <footer>
      <div className='row-line' />
      <FooterWrapper>
        <IconArea>
          <FontAwesomeIcon icon={faTwitter} />
        </IconArea>
        <div className='btn-area'>
          <div className="btn btn-flat">
            <a href='https://twitter.com/kibidango_py'><span>@kibidango_py</span></a>
          </div>
          <div className="btn btn-flat">
            <a href='https://twitter.com/kei_r14'><span>@kei_r14</span></a>
          </div>
          <div className="btn btn-flat">
            <a href='https://twitter.com/yat0i_kit'><span>@yat0i_kit</span></a>
          </div>
          <div className="btn btn-flat">
            <a href='https://twitter.com/SC_Raisa'><span>@SC_Raisa</span></a>
          </div>
        </div>
      </FooterWrapper>
    </footer>
  )
}

export default Footer
