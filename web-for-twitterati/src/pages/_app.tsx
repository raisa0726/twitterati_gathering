import '@/styles/globals.css'
import { AppProps } from 'next/app'
import Layout from '@/components/Layout'
import Footer from '@/components/Footer'
import Header from '@/components/Header'
import { NextPage } from 'next'

const MyApp: NextPage<AppProps> = ({ Component, pageProps }) => {
  return (
    <>
      <Header />
      <Layout>
        <Component {...pageProps} />
      </Layout>
      <Footer />
    </>
  )
}

export default MyApp
