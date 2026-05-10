import { useEffect, useState } from 'react';
import './App.css'

function App() {

  const [posts, setPosts] = useState<{title : string, content : string, id : number}[] | null[]>([])

  useEffect(()=>{
    const fetchData = async () =>{
      const response = await fetch("http://127.0.0.1:8000/api/posts")
      const data = await response.json()
      setPosts(data)
    }
    fetchData()
  },[])

  return (
    <div className="bg-gray-300 text-blue-700">
      <h1 className="text-3xl font-bold">Hello world</h1>

      {posts && posts.map((post)=>(
        <div>
          <h2>{post?.title}</h2>
          <p>{post?.content}</p>
        </div>
      ))}
    </div>
  )
}

export default App
