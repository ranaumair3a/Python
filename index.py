from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ChatAction

# Function to handle the /start command
def start(update, context):
    update.message.reply_text("Welcome to the bot! I will send a welcome message whenever someone joins the chat.")

# Function to handle new chat members
def new_chat_members(update, context):
    for member in update.message.new_chat_members:
        update.message.reply_text(f"Welcome, {member.first_name}!")

# Function to handle all other messages
def echo(update, context):
    update.message.reply_text("I'm a simple bot. I only respond to the /start command and greet new members.")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("6053910794:AAH-osc8S1c1N9q4q_uIgAzxe7JBPLJVXVI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handlers
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_members))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

# The variable `handler` serves as the entry point for the serverless function
handler = main()
