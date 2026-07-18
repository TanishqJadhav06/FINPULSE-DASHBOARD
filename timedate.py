from rich.console import Console
from rich.table import Table

table=Table()
console=Console()
import datetime

import pytz
from datetime import datetime

def time():
    # Get current date and time
    now = datetime.now()

    # Format as "16 July 2026"
    formatted_date = now.strftime("   %d %B %Y")
    formatted_day = now.strftime("%A")
    console.print(f"\n📅 {formatted_day}",style="bold green") 
    console.print(f"{formatted_date}",style="bold blue") 
    # Set your local time zone
    local_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(local_tz)

    # %I = 12-hour hour, %M = minute, %p = AM/PM
    time_12h = now.strftime("%I:%M %p")
    console.print(f"🕓 {time_12h} IST\n",style="bold purple")
time()