def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "A contact with that name doesn't exist."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]):
    name, phone = args
    _ = contacts[name]  # It will throw KeyError if that contact doesn't exist
    contacts[name] = phone
    return "Contact changed."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]):
    name, = args
    return contacts[name]


def main():
    contacts: dict[str, str] = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print("|{:^20}|{:^20}|".format('Contact name', 'Phone number'))
            for contact_name, phone in contacts.items():
                print("|{:^20}|{:^20}|".format(contact_name, phone))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
