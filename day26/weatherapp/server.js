var express = require('express')
var app = express()
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: false })) 
app.use(bodyParser.json());
app.use(express.static(__dirname))

var server = app.listen(3000, ()=>{
    console.log('server is listening on port', server.address().port)
})

app.get('/', (req,res)=>{
    app.sendFile(__dirname + '/index.html')
})

app.post('/register',(req,res)=>{
    var userName = req.body.userName
    var userEmail = req.body.userEmail
    var userCity = req.body.userCity
    console.log(userEmail)
    res.send(userName)
})