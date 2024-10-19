#Name: Uzair Ahmed Abdul Samad Ansari
#Contact Manager
class ContactManager:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone): 
        if phone in self.contacts: 
            print(f"Contact '{phone}' already exists.")
        else:
            self.contacts[phone] = name 
            print(f"Contact '{name}' added.")

    def delete_contact(self, name):
        phone_to_delete = None
        for phone, contact_name in self.contacts.items():
            if contact_name.lower() == name.lower():
                phone_to_delete = phone
                break
    
        if phone_to_delete:
            del self.contacts[phone_to_delete]
            print(f"Contact '{contact_name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")
    def search_contact(self, name):
        found = False
        for phone, contact_name in self.contacts.items():
            if contact_name.lower() == name.lower():

                print(f"Contact '{contact_name}': {phone}")
                found = True
            
        if not found:
            print(f"Contact '{name}' not found.")


    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for phone, name in self.contacts.items():
                print(f"{name}: {phone}")
    
def main(): 
    contact_master = ContactManager()

    while True:
        print("\nContact Master Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact_master.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to delete: ")
            contact_master.delete_contact(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_master.search_contact(name)
        elif choice == '4':
            contact_master.display_contacts()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()

