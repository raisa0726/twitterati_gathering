import type { NextPage } from 'next'
import { useEffect, useState } from 'react';

const Group: NextPage = () => {
    // db connect
    const [groups, setGroups] = useState([]);
    useEffect(()=>{
      fetch('http://localhost:3000/group',{
        'methods':'GET',
        headers : {
          'Content-Type':'application/json'
        }
      })
      .then(response => response.json())
      .then(response => setGroups(response))
      .catch(error => console.log(error))

    }, [])

  return (
    <div className='area'>
      <h1>Your Group1</h1>
    </div>
  )
}

export default Group
