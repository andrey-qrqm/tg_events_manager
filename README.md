# Telegram events manager
This is my university study project. I was focused on producing a working version
of the product with further availability of scaling and improvement. The version today
can be viewed as a MVP and example of implemented functions, strategies and dependencies.


## Overall description

The events manager is an application designed to share and publish information of
future social events in the city to the broad auditory. The publications are made in
the Telegram App. Telegram is a cloud-based instant messaging app that allows users to send text messages, multimedia files, and make voice and video calls.
Also Telegram has their own API system, which I used in this project.
This bot can be added in different chats or be connected directly.

When Bot receives a command out of the list, it will produce an output message.
Output message is a set of all events available for visiting on the specified dates.

Commands available are:

event - Events for today and tonight

event 3 - Events that will be in the next 3 days

event 7 - Events during a week

## Event creation

Information about events is done manually by the creator of the event.
To publish an event, creator fill in the special designed Google Form 
that is in open access.

Link to the Google Form: https://docs.google.com/forms/d/e/1FAIpQLSe199v8MLmNrSUt6rFs3S_VWjvCNlDqoUMOP2d1KcvuDCVN-A/viewform

After submitting, data from Forms is transfered to the GoogleSheets.

I have set up dependencies which are taking the data from GoogleSheets and
transfer it to the Bot script. Inside the script data is filtered and sorted.
Then other script generate the output message and send it to Telegram service,
and the response appears in the chat.

During the work on a project I have used Google Cloud API service and Telebot.


# How to run the code
If you would like to use this example for your own purposes, you should do following:

Install required libraries from requirements.txt

Create your Telegram Bot for responses. There are lots of guides in the internet, so it should not be a problem
When you create a Bot, for example through BotFather. You should find and save the access key.
To run the code use command 

py tele_main.py YOUR_KEY

** py could be changed to python or python3 depending on the system

To use Google Cloud API you should create a Google account and create a project.
After creating a project you should install the credentials.json file in your system, in the
root folder of the project. 

You should also update the "service email" account and give to this account access
to your Google Sheets. 

After this the code should run without any problems.
