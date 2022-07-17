import axios from 'axios'


export const postMessage = async ( data ) => {
    console.log("Post message called")
    const videoPath = axios({
        method: "post",
        url: "/v1/chatbot/message",
        data: data,
        headers: { "Content-Type": "multipart/form-data" },
    })
    .then(res => {
        console.log(res.data)
        return res.data.video_path
    })
    .catch(err => {
        console.log(err)
    })
    return videoPath
}
