from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
table=Table()
console=Console()
import datetime

import pytz
from datetime import datetime

def time_panel():
    # Get current date and time
    content=Text()
    now = datetime.now()

    # Format as "16 July 2026"
    formatted_date = now.strftime("    %d %B %Y")
    formatted_day = now.strftime("%A")
    content.append(f"📅  {formatted_day}",style="bold light_green") 
    content.append(f"\n{formatted_date}",style="bold white") 
    # Set your local time zone
    local_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(local_tz)

    # %I = 12-hour hour, %M = minute, %p = AM/PM
    time_12h = now.strftime("%I:%M %p")
    content.append(f"\n🕓  {time_12h} IST\n",style="bold white")

    return Panel(content, border_style="white", padding=(1, 2))


def last_updated_panel():
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

def title_block():
    content = Text(justify="center")
    content.append("📈 FINPULSE V1.0\n", style="bold bright_green")
    content.append("Personal Macro Intelligence Terminal\n", style="white")
    content.append("Know the markets. Understand the big picture", style="dodger_blue1")
    return content
def header():
    grid = Table.grid(expand=True)
    grid.add_column(ratio=1)
    grid.add_column(ratio=2)
    grid.add_column(ratio=1)
    grid.add_row(time_panel(), title_block(), last_updated_panel())
    return grid

if __name__=="__main__":
    console.print(header())