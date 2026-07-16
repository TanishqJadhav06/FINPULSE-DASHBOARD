import datetime

import pytz
from datetime import datetime

def time():
    # Get current date and time
    now = datetime.now()

    # Format as "16 July 2026"
    formatted_date = now.strftime("%A \n%d %B %Y")
    print(f"📅 {formatted_date}\n") 

    # Set your local time zone
    local_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(local_tz)

    # %I = 12-hour hour, %M = minute, %p = AM/PM
    time_12h = now.strftime("%I:%M %p")
    print(f"🕓 {time_12h} IST\n")

time()