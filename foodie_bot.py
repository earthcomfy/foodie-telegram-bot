from bs4 import BeautifulSoup
import requests
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# Returns a random image from a specified category of food
def get_random_image(category):
    api_end_point = f'https://foodish-api.herokuapp.com/images/{category}/'
    source = requests.get(api_end_point).text

    soup = BeautifulSoup(source, 'lxml')

    name_of_image = soup.find('div', class_='col').img['src'].split('/')[3]

    random_image = f'{api_end_point}/{name_of_image}'
    return random_image


# Returns a random image and its name from a random category
def get_random_food():
    api_end_point = "https://foodish-api.herokuapp.com/api/"
    random_food = requests.get(api_end_point).json()['image']

    name_of_food = random_food.split('/')[4]

    return random_food, name_of_food


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use one of the following commands: \n\n"
                              "/start to get started\n"
                              "/game to play guess the food game\n"
                              "/food to choose a food category and get random image from it.")


def start(update: Update, context: CallbackContext) -> None:

    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    update.message.reply_text(f"Hello {user.first_name} Welcome")


# Shows a category of foods in the form of inline keyboard buttons
def food(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Biryani", callback_data='1'),
            InlineKeyboardButton("Burger", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Butter-Chicken", callback_data='3'),
            InlineKeyboardButton("Dessert", callback_data='4'),
        ],
        [
            InlineKeyboardButton("Dosa", callback_data='5'),
            InlineKeyboardButton("Idly", callback_data='6'),
        ],
        [
            InlineKeyboardButton("Pasta", callback_data='7'),
            InlineKeyboardButton("Pizza", callback_data='8'),
        ],
        [
            InlineKeyboardButton("Rice", callback_data='9'),
            InlineKeyboardButton("Samosa", callback_data='10')
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Get random pictures of foods by choosing '
                              'one of the following category of foods', reply_markup=reply_markup)


# Sends different image based on the user's choice of category
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Depending on which button the user clicked, it displays different random images
    if query.data == '1':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("biryani"),
                             caption="Biryani")
    elif query.data == '2':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("burger"),
                             caption="Burger")
    elif query.data == '3':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("butter-chicken"),
                             caption="Butter-Chicken")
    elif query.data == '4':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("dessert"),
                             caption="Dessert")
    elif query.data == '5':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("dosa"),
                             caption="Dosa")
    elif query.data == '6':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("idly"),
                             caption="Idly")
    elif query.data == '7':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("pasta"),
                             caption="Pasta")
    elif query.data == '8':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("pizza"),
                             caption="Pizza")
    elif query.data == '9':
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("rice"),
                             caption="Rice")
    else:
        query.bot.send_photo(chat_id=query.message.chat_id,
                             photo=get_random_image("samosa"),
                             caption="Samosa")


# This is a command to start a quiz game
def game(update: Update, context: CallbackContext):
    user = update.message.from_user['first_name']
    list_of_categories = ('biryani', 'burger', 'butter-chicken', 'dessert', 'dosa',
                          'idly', 'pasta', 'pizza', 'rice', 'samosa')
    message = f"Hello {user} Welcome to Food Quiz Game.\n\n" \
              f"I've a random food image generated from one of the following categories.\n\n" \
              f"{'    |    '.join(list_of_categories[:2])} \n\n" \
              f"{'    |    '.join(list_of_categories[2:4])} \n\n" \
              f"{'    |    '.join(list_of_categories[4:6])} \n\n" \
              f"{'    |    '.join(list_of_categories[6:8])} \n\n" \
              f"{'    |    '.join(list_of_categories[8:10])} \n\n" \
              f"Guess what it is?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# Game logic
def start_game(update: Update, context: CallbackContext):

    # Generate a random food
    random_food = get_random_food()
    name_of_random_food = str(random_food[1])

    # Get the user's guess
    guess = str(update.message.text).lower()

    if guess != name_of_random_food:
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=random_food[0],
                               caption=f"Sorry you are wrong! Better luck next time. The food was {name_of_random_food}")

    else:
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=random_food[0],
                               caption=f"Congrats, You are right. it is {name_of_random_food}")


def main() -> None:
    updater = Updater(token='1899388930:AAGXbbNV-wBqfdMJZvMcKZtmhzvXPLYHVSI', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('game', game))

    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), start_game))

    dispatcher.add_handler(CommandHandler('food', food))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
