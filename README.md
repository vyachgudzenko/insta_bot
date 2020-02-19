# insta_bot

Insta bot - a small bot that can subscribe to profiles that are specified in the file. 
To do this, he uses the Selenium tool to automate the browser.

To work correctly, you must have the latest version of the Selenium driver for your browser downloaded. 
You can do this on the official page https://selenium.dev/downloads/

By files:

bot.py - the bot class itself is located here and you can specify the current name of your files 
with the database of profiles and account information for login

chromedriver.exe - Selenium driver that I used

following.txt - file with a list of profiles that you want to subscribe to. You can add data with or without @

login.json - json file. Your login details are stored here.
