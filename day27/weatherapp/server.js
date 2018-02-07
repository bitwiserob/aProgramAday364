var express = require('express')
var app = express()
var bodyParser = require('body-parser');
const {Client} = require('pg')
var client = new Client({ 
    user :'draxnol',
    host:'localhost',
    database:'weather',
    password:'',
    port:5432,
})
client.connect()
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
    const values = [req.body.userEmail,req.body.userCity]
    res.send("somethin worked")
    query_setInfo(text,values)
})

function query_setInfo(values){
    const text = 'INSERT INTO users(user_email,user_city) VALUES($1, $2)'
    client.query(text,values)
}

function query_getInfo(){
    const text = 'SELECT * FROM users'
    res = client.query(text)
    console.log(res)
}