
gol_pct=1.512

def fmt_pct(pct):
    color = "green" if pct >= 0 else "red"
    arrow = "▲" if pct >= 0 else "▼"
    return f"[{color}]{arrow} {pct:+.2f}%[/{color}]"


print("GOld","$12099",fmt_pct(gol_pct))