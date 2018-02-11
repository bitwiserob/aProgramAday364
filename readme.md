epilogue
=====
After 30 days, I’ve decided to end this little challenge. When I first began, I didn’t know how long I wanted to it for, so I just decided to call the repo aprogramaday364. The intention was never to create a program a day for 364 days. I’ve decided to end now because while doing this challenge did teach me a lot, I haven’t had time to work on bigger projects.

About
---
The purpose of this repository is to create a small program a day for as long as possible.

Rules
---
1. Program must complete atleast one task.
2. Program must be more complicated then a hello world program or something similar.
3. Program must be completed once a day starting from 2018-01-11

Disclaimer:
---
The programs presented here are quick prototypes usually completed within a few hours. Due to the time constraints associated with making a program everyday, each program only has enough testing to ensure basic functionally. There is also no error handling unless it was essential to the base functionally of the program.  sssd

List Of Programs
---

|Day		|Program		|Description|
|-----------|---------------|-----------|
|1			|CopyInputToFile|A small gui program that simply takes some input from a text area and copies it to a file|
|2          |HTML tag text extractor|A gui program that extracts the text content from a selected tag from a URL|
|3			|Paste to pastebin|A gui program that creates a paste on pastebin from entered text and returns the url of the created paste|
|4			|Ping ip		|A simple gui program that pings an address and outputs the ping results to the gui.| 
|5			|Get Current weather| A gui program that outputs information about the current weather in a selected city using an api call.| 
|6			|Email Sender| A gui email client that can be used to send emails.| 
|7			|Explosm comic viewer| Displays a random comic from the popular webcomic hosted on http://explosm.net |
|8			|Current weather email sender| A command line script that takes an gmail address and password as command line arguments, then sends a email containing the current weather and a link to the lastest explosm comic.|
|9			|BBC rss parse| A program that parses the bbc news rss and sends a email to someone containing 10 article titles, date published and a link to the article.|
|10		    |Current Weather webApp| A web application version of the day 05 program which uses flask to display the current weather of a city that the user enters.|
|11			|Email helper class| Not really a program, but a class that was created to make sending emails easier using emailHandler objects.|
|12			|send mutiple emails web app(INCOMPLETE)|A half working web application using flask that will send the weather to mutiple emails that are entered in a web interface.|
|13			|EmailLog| A mockup for a web applcation email registration form using flask. User enters a email, user name and comment that is then inserted into a database using python.| 
|14			|Send Weather Emails| A flask web app that can send the current weather in a city to mutiple emails that are entered in the web interface. The email is a HTML message can be styled in anyway that is supported by clients.(working remake of day 12)|
|15			|Refactored Classes| Due to computer issues, there was only time to clean up the email helper class and the weather helper class.|
|16			|Weather Email Web App| Part 1 of a mockup webapp that allows users to register using their emails and city name. The webapp then stores this infomation in a database. Part 2 will build upon this by having a control panel that can send everyone in the database a email containing the weather.|
|17			|Weather Email Web App| Part 2. Added the ablitiy to send everyone in the database a email using the methods used in day 14.|
|18         |Refactored the Email Web App| Made code about 98% more pep8 compliant and less likely to cause bleeding from eyes.|
|19			|basic postgresql interaction| A small flask app that interacts with a postgresql database and displays items from the database|
|20			|postgresql weather|A small application that gets weather data for the cities in a list and then inserts that data into a database.|
|21			|day 20 + day 16| Moved the weather email app to postgresql and added interaction between the user table and weather table. The webapp gets all the cities from the user table, then gets the weather for those cities and adds the weather data to the weather table.|
|22			|Weather email app(the SQLquel)| Building on day 21, added the ablitiy to send people emails by retrieving their infomation from one database, then retrieving weather data from another database, sticking it together and sending it.|
|23			|Small pyglet not-quite-a-game| Spent time learning pyglet and drawing sprites on a window.|
|24         |pyglet-not-a-game| Spent more time breaking things in pyglet|
|25         |Weather Email App part 1|Set up the front end of a weather email app that is going to be the same as the one from day 22, but made using node.js, express and bootstrap.|
|26         |Weather Email App part 2| Spent most of my programming time editing the wrong file and wondering why the express server wasnt working, so i was only able to get basic form functionally working.|
|27         |Weather Email app 3| User is added to postgresql database when they register.|
|28         |Emailing Using Node| Made a node program that grabs the emails in the database and sends an email to those emails.|
|29          |incomplete fragment|Messed around with json files, node and express.|
|30          |Back 2 weather app| recreated the registration process. A user signs up, is sent an email and is added to a db.|
