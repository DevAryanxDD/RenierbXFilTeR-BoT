from info import ADMINS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ForceReply
import schedule
import time
import database

# /addpremium command using the database functionality
@Client.on_message(filters.command("addpremium") & filters.private)
async def add_premium_user(client, message):
    chat_id = message.chat.id

    # Extract the user_id and duration from the command
    text = message.text.split(' ')
    if len(text) == 3:
        user_id = int(text[1])
        duration_notation = text[2][-1]
        duration_value = int(text[2][:-1])

        # Add the user to the premium list using the database function
        database.add_user_to_premium(user_id, duration_notation, duration_value)

        # Send a congratulatory message to the user
        try:
            await client.send_message(user_id, f"Congrats, you are now a premium user! Enjoy your premium subscription.")
        except Exception as e:
            print(f"Failed to send congratulatory message to user {user_id}: {str(e)}")
    else:
        await message.reply_text("Invalid command format.")


# /removepremium command using the database functionality
@Client.on_message(filters.command("removepremium") & filters.private & filters.incoming)
async def remove_premium_user(client, message):
    try:
        if message.from_user.id in ADMINS:  # Ensure that only admins can trigger this command
            if len(message.command) >= 2:
                user_id = int(message.text.split(' ')[1])
                reason = " ".join(message.text.split(' ')[2:]) if len(message.text.split(' ')) > 2 else "No reason specified"

                # Remove the user from the premium list
                database.remove_user_from_premium(user_id, reason)

                await message.reply_text(f"User with ID {user_id} has been removed from the premium user list. Notified the user about the reason.")
            else:
                await message.reply_text("Invalid command format.")
        else:
            await message.reply_text("Sorry, only my Admins can use this command.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Handle the caught exception
        
    
# /clearexpired command using the database functionality
@Client.on_message(filters.command("clearexpired") & filters.private & filters.incoming)
async def clear_expired(client, message):
    if message.from_user.id in ADMINS:
        current_time = datetime.now()
        expired_users = list(db.premium_users.find({"expiry_date": {"$lt": current_time}}))

        removed_user_names = []

        for user in expired_users:
            user_id = user["user_id"]

            # Notify the user about the expiry of their premium plan
            try:
                user_info = await client.get_users(user_id)
                removed_user_names.append(f"[{user_info.first_name}](tg://user?id={user_info.id})")
                await client.send_message(user_id, "Your premium plan has expired. If you want to continue enjoying premium benefits, be sure to upgrade to premium again.",
                           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade to Premium", callback_data="upgrade_premium")]]))
            except Exception as e:
                print(f"Failed to notify user {user_id} about the expiry of their premium plan: {str(e)}")
            
            # Remove the expired user from the premium list
            try:
                database.remove_user_from_premium(user_id, "Premium plan expired")
            except Exception as e:
                print(f"Failed to remove expired user {user_id} from the premium list: {str(e)}")

        removed_users_message = "Expired users have been notified and removed from the premium user list."
        if removed_user_names:
            removed_users_message += "\n\nRemoved users:\n\n" + "\n".join(removed_user_names)

        await message.reply_text(removed_users_message)
    else:
        await message.reply_text("Sorry, only my Admins can use this command.")

