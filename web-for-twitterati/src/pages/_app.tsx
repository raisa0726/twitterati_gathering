import '@/styles/globals.css'
import { AppProps } from 'next/app'
import Footer from '@/components/Footer'
import Header from '@/components/Header'
import { useEffect, useState } from 'react';

function MyApp({ Component, pageProps }: AppProps) {

  // db connect
  const [users, setUsers] = useState([]);
  useEffect(()=>{
    fetch('http://localhost:3000/articles',{
      'methods':'GET',
      headers : {
        'Content-Type':'application/json'
      }
    })
    .then(response => response.json())
    .then(response => setArticles(response))
    .catch(error => console.log(error))

  }, [])

  return (
    <>
      <Header />
      <main>
        <Component {...pageProps} />
      </main>
      <Footer />
    </>
  )
}

export default MyApp
