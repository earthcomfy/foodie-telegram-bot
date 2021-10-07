# Get Random Pictures of Food - A Simple Telegram Bot

This telegram bot is built using the popular python-telegram-bot library. It also uses an [API](https://foodish-api.herokuapp.com/) made by @surhud004. 
I built this project to get an experience in bot development, fetching data from an api, and web scraping using BeautifulSoup. Oh, and because I love food too :laughing:

![start](https://user-images.githubusercontent.com/66206865/136410373-480973ae-ebfd-409a-84cb-9f5542e8872a.jpg)

## Basic features of the bot

- Users can get random images of food based on their choice of category.
- Users can play a game called "guess the food", in which the bot generates a random food from a category, and the user guesses what the food is.

**Note**: In the future I'm hoping to add more features to the bot and deploy it.


## Quick Start
1. Follow this [link](https://core.telegram.org/bots#6-botfather) to create a new telegram bot. Don't forget to keep your authorization token a secret.
2. Set up a python virtual environment
3. Install python-telegram-bot, Beautiful Soup, lxml and requests
```buildoutcfg
pip install python-telegram-bot==13.7
pip install beautifulsoup4==4.9.3
pip install lxml==4.6.3
pip install requests==2.25.1
```
4. Run the module and go to the bot you created in step 1. Hit start and enjoy!

![food](https://user-images.githubusercontent.com/66206865/136410387-f55800c3-1de0-4c08-9de8-213816c1067d.jpg)



*Thanks to @surhud004 for providing the API.*
