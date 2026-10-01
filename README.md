# PLP Python Week 7 — Shopping List Manager

`list_warmup.py` — Demonstrates Python list indexes, `.append()`, `.remove()`, and `len()`.

`shopping_list.py` — A menu-based shopping list manager that can add, remove, show, and safely handle missing items.

`list_report.py` — Prints a numbered shopping list, counts item names with more than four letters, and finds the longest item using a loop comparison.

Checking with `in` before calling `.remove()` is safer because `.remove()` causes an error if the item is not in the list. Using `in` first lets the program check whether the item exists and display a message instead of crashing. This makes the shopping list manager more reliable and user-friendly.
