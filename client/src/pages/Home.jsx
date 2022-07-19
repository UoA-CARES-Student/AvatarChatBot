import React, {useState} from 'react'

import { postMessage } from '../api/Api'
import './Home.css';

const Home = ( ) => {
    
    const [videoPath, setVideoPath] = useState("")
    const[message, setMessage] = useState(""); 

    const[response, setResponse] = useState(""); 
    


    const submitMessage = (e) =>{
        const data = new FormData()
        data.append('message', message)
        const fetchData = async () => {
            const receivedData = await postMessage(data);
            // console.log(path)
            setVideoPath(receivedData.video_path)
            setResponse(receivedData.message)
        }          
        fetchData()
    }


    return (
    <div className='centered-div'>
        <div>
            <div>
                <h1>Chat Bot</h1></div>

            <div className='player-wrapper'>
                <video className = 'vid-player' width="600" height="400" autoPlay controls preload src={videoPath} type="video/mp4">
                    Your browser does not support the video tag.
                </video> 
            </div>
            <div className='chat-border'>
                <h3 className='reply-text'>
                    Bot: {response}
                </h3>
            </div>

            <div>
                <input className = 'input-text' name="input" placeholder="Say Hello !" onChange={(e) => {setMessage(e.target.value)}}/>
                <button className = 'submit-button' onClick={submitMessage}>Send</button>
            </div>

        </div>
        
        
        
    </div>
    )
}

export default Home