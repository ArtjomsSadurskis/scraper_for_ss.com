Project by Artyom Sadursky (211REC086) on the subject Lietojumprogrammatūras automatizēšanas rīki(1) (DIP225)
1.course RDBF0 Automātika un datortehnika, semestris 1 23/24-R

# Web scraping script using Selenium and integration with Telegram


The purpose of the project I like electronics: audio, phones, computer parts, etc.
In Latvia the biggest marketplace for buying and selling electronics is ss.com, the second is facebook/marketplace (I tried to scrap it until I understood the page structure).
Let's get back to ss.com, I've been in the habit of watching interesting ads in different sections for 3-4 years, both rare electronics and just good offers.
I decided that I need to automate this task, increasing efficiency and freeing up for myself about 2-3 hours of time a day, at this time I can code or do sports. I hope the reason for choosing this site and work with it I have explained.


About the code
This script uses Selenium to perform web scraping on a specific ss.com website and sends the extracted information to Telegram chat using the Telegram Bot API.





Python libraries I've used:

selenium: Used to automate the web browser. In your code, this is used to interact with the web page, opening the page, clicking on elements, retrieving data, etc.

time: Used to create time delays to give the browser and page time to load and process.

asyncio: Used to process tasks asynchronously. Your code contains an asynchronous main() function and uses the asyncio event loop to execute it.

telegram: This is supposed to be a custom library for working with the Telegram API. You use it to send messages to the Telegram bot.

schedule: This is used to create and manage a schedule for tasks. In your code, this is used to run job() every 6 minutes.

webdriver.Chrome and webdriver.ChromeOptions: Part of the Selenium library, this allows you to manage the Chrome web browser and define options to run it.



## Pre-requisites

- Python 3.x
- Install the required packages by running the following command:
  ```bash
  pip install selenium python-telegram-bot schedule


Download the ChromeDriver executable and make sure it is in your system's PATH variable.


1.STEP.

Setup

To create a bot, I use the bot https://t.me/BotFather

1.Start the bot by seeing the /start command.
2.Select /newbot
3.The bot will prompt you to create a name for your bot (assistant) In my case it is https://t.me/scraper_market_bot.
4.After creation you will be sent this message:


Done! Congratulations on your new bot. You will find it at t.me/scraper_market_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
6393465137:AAHN7u7UWD5yjyiik9COgwV9QbfTsJVtoU8      <-------------------- это и есть токен вашего телеграмм бота

Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

5.In order for messages to reach you install the library, if it does not exist, using the command:

1.pip install python-telegram-bot
2.telegram-send --configure

P.S in the console you will need to enter your token that https://t.me/BotFather sent you.
3.6393465137:AAHN7u7UWD5yjyiik9COgwV9QbfTsJVtoU8 
4.In the console will be given a password that must be sent to your bot to start working.
5.Write the bot the command /start and type in your password. (Example password:01617)


P.S If my instructions did not help you, you can use this video: https://www.youtube.com/watch?v=-73hRicngD8&ab_channel=TheLookin.


2.STEP

To find out chat_id:

1.Find the telegram bot https://t.me/userinfobot
2.Start a chat with the command /start
3.It will send you a message with all your details:
@Urnickname
Id: 626358089 <----------- is your Id
First: Name
Last: Surname
Lang: Eng



3.STEP Working with the code
In all the code I tried to leave comments to make it clear that it can be adapted to other servers, other categories, etc.

1.Insert your Telegram Bot token and chat ID into the script:

bot_token = 'your_token_bot'
chat_id = 'your_chat_id'


2.Customise the script according to your web scraping requirements.


Usage
Run the script using the following command:

python scrapska.py


The script will run periodically (every 6 minutes, according to the schedule) and send the extracted information to the specified Telegram chat.



Script Overview

The script initialises Chrome WebDriver using Selenium to interact with a website.
It navigates through the website to a specific page and extracts information.
If an element with a specific XPath is found, the script clicks on it.
The extracted information is then sent to Telegram chat.




!!!!Make sure you have the necessary packages installed and Telegram Bot API credentials configured before running the script!!!!