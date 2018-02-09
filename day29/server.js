const express = require('express')
const fs = require('fs')
const app = express()
app.get('/', (req,res) =>{
    fs.readFile('weatherinfo.json', function(err,data)
    res.header("Content-Type",'application/json');
    res.send(JSON.stringify(data));

})
app.listen(3000,()=>console.log('listening on port 3000'))

