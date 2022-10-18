import axios from 'axios'


export const postMessage = async ( data ) => {
    console.log("Post message called")
    const returnVal = axios({
        method: "post",
        url: "/v1/chatbot/message",
        data: data,
        headers: { "Content-Type": "multipart/form-data" },
    })
    .then(res => {
        console.log(`RESULTS data => ${res.data}`)
        return res.data
    })
    .catch(err => {
        console.log(err)
    })
    return returnVal
}



export const postMessageToImage2Vid = async ( data ) => {
    console.log("Post message called")
    const returnVal = axios({
        method: "post",
        url: "/v1/chatbot/message_img2vid",
        data: data,
        headers: { "Content-Type": "multipart/form-data" },
    })
    .then(res => {
        console.log(`RESULTS data => ${res.data}`)
        return res.data
    })
    .catch(err => {
        console.log(err)
    })
    return returnVal
}
