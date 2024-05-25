from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define your Telegram bot token
TOKEN = 'your_telegram_bot_token'

# Define the chat ID where you want to forward messages
FORWARD_CHAT_ID = 'destination_chat_id'

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Welcome to the message forwarder bot!')

# Define a function to forward messages
def forward_message(update, context):
    # Forward the message to the defined chat ID
    context.bot.forward_message(chat_id=FORWARD_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

# Define a function to handle errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')

def main():
    # Create an Updater object
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handler to forward messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # Register an error handler
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
