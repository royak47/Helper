from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from commands import start, help, admin, filters as filter_commands
from config import TOKEN

def main():
    application = Application.builder().token(TOKEN).build()

    # Command Handlers
    application.add_handler(CommandHandler("start", start.start_command))
    application.add_handler(CommandHandler("help", help.help_command))
    application.add_handler(CommandHandler("ban", admin.ban_user))
    application.add_handler(CommandHandler("mute", admin.mute_user))
    application.add_handler(CommandHandler("unban", admin.unban_user))
    application.add_handler(CommandHandler("unmute", admin.unmute_user))
    application.add_handler(CommandHandler("filter", filter_commands.add_filter))
    application.add_handler(CommandHandler("deletefilter", filter_commands.delete_filter))
    application.add_handler(CommandHandler("listfilters", filter_commands.list_filters))

    # Filters handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_commands.handle_filters))

    # Callback Query Handler for inline buttons
    application.add_handler(CallbackQueryHandler(help.help_callback))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
