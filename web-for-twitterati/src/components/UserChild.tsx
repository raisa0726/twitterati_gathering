import React, { VFC } from 'react'

type Props = {
  id: number
  name: string
}

const UserChild: VFC<Props> = ({ id, name }) => {
  return (
    <>
      <h3>タイトル</h3>
      <div>
        <p>userId: {id}</p>
        <p>username: {name}</p>
      </div>
    </>
  )
}

export default UserChild
