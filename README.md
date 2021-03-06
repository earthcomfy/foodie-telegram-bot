# Get Random Pictures of Food - A Simple Telegram Bot

This telegram bot is built using the popular python-telegram-bot library. It also uses an [API](https://foodish-api.herokuapp.com/) made by [@surhud004](https://github.com/surhud004). 
I built this project to get an experience in bot development, fetching data from an api, and web scraping using BeautifulSoup. Oh, and because I love food too :laughing:

![Start](https://user-images.githubusercontent.com/66206865/136411889-06bf857a-c668-42d6-ab86-253e07f8b53f.jpg)


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

![Burger](https://user-images.githubusercontent.com/66206865/136411939-1f0c48db-7d17-4b36-9210-a01f19ecb047.jpg)




*Thanks to [@surhud00](https://github.com/surhud004) for providing the API.*
