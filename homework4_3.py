def greet():
    return "How can I help you?"

def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added successfully."

def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return "Phone number updated successfully."
    else:
        return "Contact not found."

def get_phone(username, contacts):
    if username in contacts:
        return f"The phone number for {username} is {contacts[username]}."
    else:
        return "Contact not found."

def get_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    contacts = {}
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "hello":
            print(greet())
        elif command.startswith("add"):
            _, username, phone = command.split(" ", 2)
            print(add_contact(username, phone, contacts))
        elif command.startswith("change"):
            _, username, phone = command.split(" ", 2)
            print(change_contact(username, phone, contacts))
        elif command.startswith("phone"):
            _, username = command.split(" ", 1)
            print(get_phone(username, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if name == "__main__":
    main()