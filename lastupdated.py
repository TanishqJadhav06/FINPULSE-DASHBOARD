from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
table=Table()
console=Console()
import datetime

import pytz
from datetime import datetime

def time():
    # Get current date and time
    content=Text()
    now = datetime.now()

    # Format as "16 July 2026"
    formatted_date = now.strftime("%d %B %Y")

    content.append("Last Updated",style="bold deep_sky_blue1")
    content.append(f"\n{formatted_date}",style="light_green") 
    # Set your local time zone
    local_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(local_tz)

    # %I = 12-hour hour, %M = minute, %p = AM/PM
    time_12h = now.strftime("%I:%M %p")
    content.append(f" | {time_12h} IST\n",style="light_green")
    content.append(f"\nData Auto-Refresh :  ⌛︎",style="light_green")


    return Panel(content, border_style="white", padding=(1, 2))

    