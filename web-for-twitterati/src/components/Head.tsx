import { VFC } from 'react'
import NextHead from 'next/head'

type Props = {
  title?: string
}

const BASE_TITLE = 'Twitteraties'
const EXPLANATION='技育CAMP vol.1 で作成したアプリです。'

const Head: VFC<Props> = (props) => {
  const title = props.title ? `${props.title} | ${BASE_TITLE}` : BASE_TITLE

  return (
    <NextHead>
      <title>{title}</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta name='application-name' content='MyTemplate' />
      <meta name="description" content={ EXPLANATION } />
      <meta property="og:type" content="website" />
      <meta property="og:title" content={title} />
      <link rel="android-touch-icon" sizes="192x192" href="%PUBLIC_URL%/android-chrome-192x192.png"/>
      <link rel="apple-touch-icon" sizes="180x180" href="%PUBLIC_URL%/apple-touch-icon.png"/>
      <link rel="icon" type="image/png" sizes="32x32" href="%PUBLIC_URL%favicon-32x32.png"/>
      <link rel="icon" type="image/png" sizes="16x16" href="%PUBLIC_URL%/favicon-16x16.png"/>
    </NextHead>
  )
}

export default Head
