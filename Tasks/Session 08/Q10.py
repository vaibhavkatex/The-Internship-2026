
# Unique Item Collector Program using Sets

# Empty set to store unique items
items = set()

while True:
    # Display Menu
    print("\nUnique Item Collector ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show All Unique Items")
    print("4. Check if an Item Exists")
    print("5. Clear All Items")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Option 1: Add Item
    if choice == "1":
        item = input("Enter item to add: ")
        items.add(item)
        print(f"'{item}' added successfully!")

    # Option 2: Remove Item
    elif choice == "2":
        item = input("Enter item to remove: ")
        items.discard(item)  # Safe removal, no error if item doesn't exist
        print(f"'{item}' removed (if it existed).")

    # Option 3: Show All Unique Items
    elif choice == "3":
        if len(items) == 0:
            print("No items available.")
        else:
            print("Unique Items:", items)

    # Option 4: Check if an Item Exists
    elif choice == "4":
        item = input("Enter item to check: ")
        if item in items:
            print(f"'{item}' exists in the set.")
        else:
            print(f"'{item}' does not exist in the set.")

    # Option 5: Clear AllItems
    elif choice == "5":
        items.clear()
        print("All items have been cleared.")

    # Option 6: Exit Program
    elif choice == "6":
        print("Exiting program.Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")