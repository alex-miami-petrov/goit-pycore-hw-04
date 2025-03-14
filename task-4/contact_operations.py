def validate_contact_args(args: list) -> str:
    
    if len(args) != 2:
        return "Invalid command. Usage: [command] [ім'я] [номер телефону]"

    try:
        name, phone = args
        if not phone.isdigit():
            return "Invalid phone number. Phone number must contain only digits."

    except ValueError:
        return "Invalid command. Usage: [command] [ім'я] [номер телефону]"

    return None


def add_contact(args: list, contacts: dict) -> str:
    error = validate_contact_args(args)

    if error:
        return error
    
    name, phone = args
    contacts[name] = phone

    return "Contact added."

def change_contact(args: list, contacts: dict) -> str:
    error = validate_contact_args(args)

    if error:
        return error

    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

    else:
        return "Contact not found."
    
def show_phone(args: list, contacts: dict) -> str:

    if len(args) != 1:
        return "Invalid command. Usage: phone [ім'я]"
    
    name = args[0]

    if name in contacts:
        return contacts[name]
    
    else:
        return "Contact not found."
    
def show_all(contacts: dict) -> str:

    if not contacts:
        return "No contacts saved."
    
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"

        return result.strip()



