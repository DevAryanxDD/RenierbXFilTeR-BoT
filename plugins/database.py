# database.py
import pymongo
from datetime import datetime, timedelta
from info import DATABASE_NAME, DATABASE_URI

# Database connection setup
client = pymongo.MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]

# Function to add a user to the premium list with timestamp
def add_user_to_premium(user_id, duration_notation, duration_value):
    expiry_date = calculate_expiry_date(duration_notation, duration_value)
    db.premium_users.insert_one({"user_id": user_id, "expiry_date": expiry_date})

# Function to remove a user from the premium list and update usertype
def remove_user_from_premium(user_id, reason):
    existing_user = db.premium_users.find_one({"user_id": user_id})
    if existing_user:
        original_usertype = existing_user.get("usertype", "Free")
        db.premium_users.delete_one({"user_id": user_id})
        db.premium_users.update_one({"user_id": user_id}, {"$set": {"usertype": "Free"}})
        # Notify the user about the removal...

# Function to calculate expiry date based on duration notation and value
def calculate_expiry_date(duration_notation, duration_value):
    expiry_date = datetime.now()
    if duration_notation == 'M':
        expiry_date += timedelta(minutes=duration_value)
    elif duration_notation == 'h':
        expiry_date += timedelta(hours=duration_value)
    elif duration_notation == 'd':
        expiry_date += timedelta(days=duration_value)
    elif duration_notation == 'w':
        expiry_date += timedelta(weeks=duration_value)
    elif duration_notation == 'm':
        expiry_date += timedelta(weeks=4 * duration_value)  # Approximating a month as 4 weeks
    elif duration_notation == 'y':
        expiry_date += timedelta(weeks=52 * duration_value)  # Approximating a year as 52 weeks
    return expiry_date
