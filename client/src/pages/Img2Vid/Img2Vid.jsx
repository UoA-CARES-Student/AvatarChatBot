import React, {useState} from 'react'
import './Img2Vid.css'; 
import { postMessageToImage2Vid } from '../../api/Api'

const Img2Vid = ( ) => {
    
    const [videoPath, setVideoPath] = useState("")
    const[message, setMessage] = useState(""); 
    const[response, setResponse] = useState(""); 

    const getInitialSpeaker = () => {
        const value = "obama";
        return value;
    };

    const getInitialEmotion = () => {
        const value = "happy";
        return value;
    };

    const [speaker, setSpeaker] = useState(getInitialSpeaker);
    const [emotion, setEmotion] = useState(getInitialEmotion);

    const submitMessage = (e) =>{

        const data = new FormData()
        data.append('message', message)
        data.append('speaker', speaker)
        data.append('emotion', emotion)
        const fetchData = async () => {
            const receivedData = await postMessageToImage2Vid(data);
            // console.log(path)
            console.log(`Received data  => ${receivedData}`)

            setVideoPath(`http://10.104.144.222:5000/v1/chatbot/video/${receivedData.video_path}`)
            setResponse(receivedData.message)
        }          
        fetchData()
    }

    const handleChangeSpeaker = (e) => {
        setSpeaker(e.target.value);
    };

    const handleChangeEmotion = (e) => {
        setEmotion(e.target.value);
    };

    return (
    
    <div className='centered-div'>
        <div>
            <div>
                <h1>Image to Video</h1> 
                <h1>Chat Bot</h1> 
            </div>
            

            <select value={speaker} onChange={handleChangeSpeaker}>
                <option value="obama">obama</option>
                <option value="monalisa">monalisa</option>
            </select>

            <select value={emotion} onChange={handleChangeEmotion}>
                <option value="happy">happy</option>
                <option value="sad">sad</option>
                <option value="neutral">neurtral</option>
            </select>

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

export default Img2Vid