from rich.table import Table
from rich.console import Console

table=Table()
console=Console()

console.print("Indian markets",justify="left")
table.add_column("Index")
table.add_column("Value")
table.add_column("Change")
table.add_row("maximus","19836","1.9%")

console.print(table)