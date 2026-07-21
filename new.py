from rich.table import Table
from rich.console import Console

table=Table(title="Today's market signal",title_justify="center",title_style="bold light_green")
console=Console()

console.print("Risk On",style="bold green")
table.add_row("confidence")

console.print(table)