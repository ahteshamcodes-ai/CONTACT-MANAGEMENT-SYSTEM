# Contact Management System
contacts = []


def is_valid_phone(phone):
    """Return True if the phone number has exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def find_contact_by_phone(phone):
    """Return the contact with this phone number, or None if not found."""
    for contact in contacts:
        if contact["phone"] == phone:
            return contact
    return None


def add_contact():
    """Add a new contact after checking the inputs."""
    print("\n--- Add Contact ---")
    name = input("Enter name: ").strip()
    if name == "":
        print("Invalid input: name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number! It must contain exactly 10 digits.")
        return

    # Prevent duplicate phone numbers
    if find_contact_by_phone(phone) is not None:
        print("Duplicate phone number! This number already exists.")
        return

    email = input("Enter email: ").strip()

    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)
    print("Contact added successfully.")


def view_contacts():
    """Display all saved contacts."""
    print("\n--- All Contacts ---")
    if len(contacts) == 0:
        print("No contacts found.")
        return

    number = 1
    for contact in contacts:
        print(str(number) + ". Name: " + contact["name"] +
              " | Phone: " + contact["phone"] +
              " | Email: " + contact["email"])
        number += 1


def search_contacts():
    """Search contacts by full or partial name (not case sensitive)."""
    print("\n--- Search Contact ---")
    search_name = input("Enter name to search: ").strip().lower()
    if search_name == "":
        print("Invalid input: search text cannot be empty.")
        return

    found = False
    for contact in contacts:
        # 'in' checks if the search text is part of the name
        if search_name in contact["name"].lower():
            print("Name: " + contact["name"] +
                  " | Phone: " + contact["phone"] +
                  " | Email: " + contact["email"])
            found = True

    if not found:
        print("No contact found with that name.")


def update_contact():
    """Update a contact. The contact is chosen using its phone number."""
    print("\n--- Update Contact ---")
    old_phone = input("Enter phone number of the contact to update: ").strip()
    contact = find_contact_by_phone(old_phone)
    if contact is None:
        print("Contact not found.")
        return

    print("Press Enter to keep the old value.")
    new_name = input("Enter new name (" + contact["name"] + "): ").strip()
    new_phone = input("Enter new phone number (" + contact["phone"] + "): ").strip()
    new_email = input("Enter new email (" + contact["email"] + "): ").strip()

    # Check the new phone number before changing anything
    if new_phone != "":
        if not is_valid_phone(new_phone):
            print("Invalid phone number! It must contain exactly 10 digits.")
            return
        # Duplicate only if another contact already has this number
        existing = find_contact_by_phone(new_phone)
        if existing is not None and existing is not contact:
            print("Duplicate phone number! This number already exists.")
            return
        contact["phone"] = new_phone

    if new_name != "":
        contact["name"] = new_name
    if new_email != "":
        contact["email"] = new_email

    print("Contact updated successfully.")


def delete_contact():
    """Delete a contact using its phone number."""
    print("\n--- Delete Contact ---")
    phone = input("Enter phone number of the contact to delete: ").strip()
    contact = find_contact_by_phone(phone)
    if contact is None:
        print("Contact not found.")
        return

    contacts.remove(contact)
    print("Contact deleted successfully.")


def show_menu():
    """Print the main menu."""
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
    """Run the menu until the user chooses Exit."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using the Contact Management System")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


main()
