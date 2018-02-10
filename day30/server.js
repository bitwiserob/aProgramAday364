var express = require('express');
var bodyParser = require('body-parser');
var nodemailer = require('nodemailer');
const {Client} = require('pg');
var client = new Client({
    user: 'draxnol',
    host: 'localhost',
    database: 'weather',
    password: '',
    port: 5432
});
var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: '',
        pass: ''
    }
});

app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.json());
dataSet =
    {
        userInfo: '',
        userEmail: '',
        userCity: ''
    };

function setMailOptions(toEmail, subject, text) {
    var mailOptions = {
        from: '',
        to: toEmail,
        subject: subject,
        text: text,
    };
    return mailOptions;
}

function add_user_db(user_email, user_city) {
    client.connect()
    var values = [user_email, user_city];
    const text = 'INSERT INTO users(user_email,user_city) VALUES($1, $2)';
    client.query(text, values)
}

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html')
});
app.post('/getstuff', function (req, res) {
    dataSet.userInfo = req.body.user_name;
    dataSet.userEmail = req.body.user_email;
    dataSet.userCity = req.body.user_city;
    transporter.sendMail(setMailOptions(dataSet.userEmail, 'weather for: ' + dataSet.userCity, 'weather goes here'));
    add_user_db(dataSet.userEmail,dataSet.userCity)

    res.send(`<h3>Email sent to:</h3><p> ${dataSet.userInfo} <br> ${dataSet.userEmail} <br> ${dataSet.userCity}</p>`)
});
app.listen(3000);