from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from commands import start, help, admin, filters
from config import TOKEN

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler("start", start.start_command))
    dispatcher.add_handler(CommandHandler("help", help.help_command))
    dispatcher.add_handler(CommandHandler("ban", admin.ban_user))
    dispatcher.add_handler(CommandHandler("mute", admin.mute_user))
    dispatcher.add_handler(CommandHandler("unban", admin.unban_user))
    dispatcher.add_handler(CommandHandler("unmute", admin.unmute_user))
    dispatcher.add_handler(CommandHandler("filter", filters.add_filter))
    dispatcher.add_handler(CommandHandler("deletefilter", filters.delete_filter))
    dispatcher.add_handler(CommandHandler("listfilters", filters.list_filters))

    # Filters handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, filters.handle_filters))

    # Callback Query Handler for inline buttons
    dispatcher.add_handler(CallbackQueryHandler(help.help_callback))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
