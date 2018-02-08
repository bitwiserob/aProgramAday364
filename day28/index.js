var nodemailer = require('nodemailer')
const {Client} = require('pg')

var client = new Client({ 
    user :'draxnol',
    host:'localhost',
    database:'weather',
    password:'',
    port:5432,
})
var transporter = nodemailer.createTransport({
    service:'gmail',
    auth:{
        user:'',
        pass:'',
    }
})

function setMailOptions(toEmail,subject,text){
    var mailOptions ={
        from:'kaczurr@gmail.com',
        to:toEmail,
        subject:subject,
        text:text,
    }
    return mailOptions;
}

client.connect()
var Query = ('select user_email FROM users')
client.query(Query, function (err, result) {
    if (err) {
      console.log(err)
    }
    
    for (var i = result.rows.length - 1; i >= 0; i--) {
        console.log(result.rows[i]['user_email'])
        transporter.sendMail(setMailOptions(result.rows[i]['user_email'],'hi','hi'))
        

    }
    
})




console.log('waka')