contacts = {
    "Police": "911"
}

def showcontacts():
    print(contacts)

def addcontacts(name: str, number: str):
    contacts[name] = number

def removecontacts(name: str):
    try:
        contacts.pop(name)
    except KeyError:
        print("Contact not found, please add a valid contact name.")

def consoletext() -> None:
    while True:
        print("Welcome to the Phone Book!")
        print("1. Add Contact")
        print("2. Remove Contacts")
        print("3. List Contacts")
        print("4. Exit")
        action = int(input("Choose an option: "))
        if action == 1:
            name = input("What is the name of the contact? -> ")
            number = input("What is the number of the contact? -> ")
            addcontacts(name, number)
        elif action == 2:
            name = input("Which contact would you like to remove? -> ")
            removecontacts(name)
        elif action == 3:
            showcontacts()
        elif action == 4:
            print("Exiting...")
            exit()
        else:
            print("Invalid number, try again.")
