const axios = require('axios');

const getMsg = () => {
  axios.get('https://www.boredapi.com/api/activity')
    .then(res => {
      console.log(res.data.activity);
    })
    .catch(error => {
      if (error) {
        console.log("error")
      }
    })
}

getMsg()