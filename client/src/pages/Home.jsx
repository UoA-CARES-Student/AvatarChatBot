import React, {useState} from 'react'

import { postMessage } from '../api/Api'

const Home = ( ) => {
    
    const [videoPath, setVideoPath] = useState("")
    const[message, setMessage] = useState(""); 


    const submitMessage = (e) =>{
        const data = new FormData()
        data.append('message', message)

        const fetchVideoPath = async () => {
            const path = await postMessage(data);
            console.log(path)
            setVideoPath(path)
        }          
        fetchVideoPath()
    }


    return (
    <div>
        <div>Chat Bot</div>
        
        <h2>
            Video path : {videoPath}
        </h2>

        <div className='video-player'>
            <video width="600" height="400" autoplay controls preload>
                <source src="/Users/takahiroi/Desktop/AvatarChatBot/ChatBotApp/media/input_videoKennedy.mp4" type="video/mp4"/>
                Your browser does not support the video tag.
            </video> 
        </div>

        <div className='textfield'>
            <input name="input" placeholder="Say Hello !" onChange={(e) => {setMessage(e.target.value)}}/>
        </div>

        <button onClick={submitMessage}>Send</button>
        
    </div>
    )
}

export default Home