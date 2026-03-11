
"""
Rimjhim
Persistent Shopping List Application.
"""

import os
import sys

class ShoppingList:
    FILE_NAME = "shopping_list.txt"

    def __init__(self):
        """Initialize state and load items from file."""
        self.items = []
        self.load_items()

    # ---------- persistence ----------
    def load_items(self):
        """Read items from the file into memory."""
        if not os.path.isfile(self.FILE_NAME):
            # No file yet; start with empty list
            self.items = []
            return
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as f:
                # read lines, strip whitespace/newlines
                lines = [line.strip() for line in f.readlines()]
            # Filter out any blank lines
            self.items = [line for line in lines if line]
        except Exception as e:
            print(f"Warning: could not load items from {self.FILE_NAME}: {e}")

    def save_items(self):
        """Write the list to the file."""
        try:
            with open(self.FILE_NAME, 'w', encoding='utf-8') as f:
                for item in self.items:
                    f.write(item + '\n')
        except Exception as e:
            print(f"Error: could not save items to {self.FILE_NAME}: {e}")

    # ---------- operations ----------
    def start_menu(self):
        """Print the menu / instructions."""
        print()
        print("What do you want to add to your shopping list?")
        print("Enter 'DONE' to stop and save.")
        print("Enter 'HELP' for additional info.")
        print("Enter 'SHOW' to see your shopping list.")
        print("Enter 'REMOVE' to remove an item from your shopping list.")
        print("Enter 'CLEAR' to delete all items.")
        print("Enter 'SEARCH' to search items by keyword.")
        print("-" * 55)

    def add_to_list(self, item):
        """Add a single item (case normalized) if not already present."""
        norm = self._normalize(item)
        if norm in self.items:
            print(f"{norm} is already on your shopping list.")
        else:
            self.items.append(norm)
            print(f"{norm} was added to your shopping list.")
        self._show_count()

    def remove_item(self, item):
        """Remove a single item if present."""
        norm = self._normalize(item)
        if norm in self.items:
            self.items.remove(norm)
            print(f"{norm} was removed from your shopping list.")
        else:
            print(f"{norm} was not found on your shopping list.")
        self._show_count()

    def show_shopping_list(self):
        """Print the current list, alphabetically."""
        if not self.items:
            print("My Shopping List is empty.")
            return
        print("My Shopping List:")
        for item in sorted(self.items):
            print(f"- {item}")

    # ---------- helpers ----------
    def _normalize(self, item):
        """Capitalize first letter, rest lowercase; strip whitespace."""
        item = item.strip()
        if not item:
            return item
        return item[0].upper() + item[1:].lower()

    def _show_count(self):
        count = len(self.items)
        plural = "items" if count != 1 else "item"
        print(f"You have {count} {plural} on your list.")

    def run(self):
        """Command loop until DONE or EOF."""
        self.start_menu()
        try:
            while True:
                try:
                    raw = input("> ")
                except EOFError:
                    # Handle Ctrl+D / Ctrl+Z
                    print()
                    print("EOF detected. Saving and exiting.")
                    self.save_items()
                    self.show_shopping_list()
                    print("See you soon!")
                    break

                cmd = raw.strip()
                if not cmd:
                    continue

                cmd_upper = cmd.upper()

                if cmd_upper == "DONE":
                    # Finish loop
                    self.save_items()
                    print("See you soon!")
                    print("Your shopping list has been saved.")
                    self.show_shopping_list()
                    break
                elif cmd_upper == "HELP":
                    self.start_menu()
                elif cmd_upper == "SHOW":
                    self.show_shopping_list()
                elif cmd_upper == "REMOVE":
                    # Prompt for item to remove
                    self.show_shopping_list()
                    to_remove = input("What do you want to remove?: ")
                    if to_remove.strip():
                        self.remove_item(to_remove)
                    else:
                        print("No item entered.")
                elif cmd_upper == "CLEAR":
                    # Confirm then clear
                    confirm = input("Are you sure you want to clear the entire list? (yes/no): ")
                    if confirm.strip().lower() in ("y", "yes"):
                        self.items = []
                        print("All items cleared.")
                        self._show_count()
                    else:
                        print("Clear canceled.")
                elif cmd_upper == "SEARCH":
                    keyword = input("Enter keyword to search: ").strip()
                    if not keyword:
                        print("No keyword entered.")
                    else:
                        self._search_items(keyword)
                else:
                    # Treat as item to add
                    self.add_to_list(cmd)
        except KeyboardInterrupt:
            # Optional: handle Ctrl+C gracefully
            print()
            print("Interrupted. Saving and exiting.")
            self.save_items()
            self.show_shopping_list()
            print("See you soon!")

    def _search_items(self, keyword):
        """Search for items containing substring, case-insensitive."""
        keyword_lower = keyword.lower()
        matches = [item for item in self.items if keyword_lower in item.lower()]
        if not matches:
            print(f"No items match '{keyword}'.")
        else:
            print(f"Items matching '{keyword}':")
            for item in sorted(matches):
                print(f"- {item}")

def main():
    app = ShoppingList()
    app.run()

if __name__ == "__main__":
    main()
