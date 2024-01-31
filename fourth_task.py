def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return (cmd, *args)

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "That name already exists."
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]} "
    else:
        return("contact does not exist")

def show_all(contacts):
    all = []
    for contact in contacts:
        all.append(contact + ":\t" + contacts[contact])
    return (all)
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you? add name phone \n change name phone \n phone name \n all ")
        elif command == "help":
            print("Enter a command: \n hello \n add name phone \n change name phone \n phone name \n all \n exit, close")
        elif command == "all":
            if not contacts:
                print ("contact list is empty.")
            for contact in show_all(contacts):
                print(contact)
        elif len(args) == 1 and command == "phone":
            print(show_phone(args, contacts)) 
        elif len(args) == 2:      
            if command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts)) 
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
