from telegram import Update
from telegram.ext import CallbackContext

filters_dict = {}

def add_filter(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("Usage: /filter <keyword> <response>")
        update.message.delete()
        return

    keyword = context.args[0].lower()
    response = " ".join(context.args[1:])
    filters_dict[keyword] = response
    update.message.reply_text(f"Filter added for keyword: {keyword}")
    update.message.delete()

def delete_filter(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        update.message.reply_text("Usage: /deletefilter <keyword>")
        update.message.delete()
        return

    keyword = context.args[0].lower()
    if keyword in filters_dict:
        del filters_dict[keyword]
        update.message.reply_text(f"Filter for '{keyword}' deleted.")
    else:
        update.message.reply_text(f"No filter found for '{keyword}'.")
    update.message.delete()

def list_filters(update: Update, context: CallbackContext):
    if filters_dict:
        filters_list = "\n".join(filters_dict.keys())
        update.message.reply_text(f"Active filters:\n{filters_list}")
    else:
        update.message.reply_text("No filters are set.")
    update.message.delete()

def handle_filters(update: Update, context: CallbackContext):
    for keyword, response in filters_dict.items():
        if keyword in update.message.text.lower():
            update.message.reply_text(response)
