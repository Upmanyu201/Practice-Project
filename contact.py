import json

def add():
        try:
            contacts = dict()
            with open('contactbook.json', 'r') as c:
                contacts = json.load(c)
                
            name = input("Enter Name: ").strip()
            number = input("Enter Mobile no. : ").strip()
            
            for savedname, savednumber in contacts.items():
                    if name == savedname:
                            return "Given contact name {} is alredy saved!".format(name)

                    elif number == savednumber:
                            return f"Given contact number{number} is saved with contact name {savedname}!"
        
                    
            if len(number) == 10:
                contacts[name] = number
            else:
                return "Given mobile number is invalid! Provide valid number."
        
            with open("contactbook.json" , 'w' ) as contactbook:
                json.dump(contacts, contactbook, indent=4)
                
            return "\nSuccessfully saved new contact."

        except ValueError:
            return "Error: Invalid input! Only enter digit"
       
def view():
    with open("contactbook.json", "r") as book:
        read = json.load(book)
        contact = ""
        for name, number in read.items():
                contact += f"{name} : {number}\n"
        return contact
        
def search():
        name = input("\nEnter name: ").strip()
        with open("contactbook.json", "rb") as book:
                contact = json.load(book)
                for sname, number in contact.items():
                        if sname == name:
                                return f"{sname} : {number}"
                return "Not Found!"
        
def delete():
    with open('contactbook.json', 'r') as contacts:
            contact = json.load(contacts)
            print(view())

            try:
                user_input = input("\nEnter name of contact to delete: ")
                confirm = input("\nConfirm to delete contact {}? yes or no\n>>> ".format(user_input)).lower()
                if confirm == "yes":
                        contact.pop(user_input)        
                        return f"\nSuccessfuly removed contact details of {user_input}"

                else:
                        return f"\nNot removing {user_input}"
                           
            except KeyError:
                    return f"\nGiven {user_input} is not found in contact list!"
    with open('contactbook.json', 'w') as contactbook:
        json.dump(contact, contactbook, indent= 4)


def menu():
    while True:
        menu = """\n\tContact Book App
0. 'Add' \t |  Add to contact book.
1. 'view \t | Print a list of all contacts.
2. 'search' \t | Show that contact’s number if exists.
3. 'delete' \t | Remove if name exists.
4. 'exit' \t | Close the app\n"""
        print(menu)
        user_input = input(">>> ").lower().strip()
    
        if user_input == "add":
            print(add())

        elif user_input == "view":
            print(view())

        elif user_input == "search":
            print(search())

        elif user_input ==  "delete":
            print(delete())

        elif user_input ==  "exit":
            break

        else:
            print("Invalid Input!")
        
if __name__ == "__main__":
    menu()
    
