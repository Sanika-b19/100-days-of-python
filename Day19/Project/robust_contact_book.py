# Project: Robust Contact Book Handling Incorrect Inputs

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if not phone.isdigit():
            print("Error: Phone number must be numeric.")
            return
        self.contacts[name] = phone
        print(f"Contact {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
            return
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")

    def delete_contact(self, name):
        if name not in self.contacts:
            print(f"Error: Contact {name} does not exist.")
            return
        del self.contacts[name]
        print(f"Contact {name} deleted.")

    def save_to_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                for name, phone in self.contacts.items():
                    file.write(f"{name},{phone}\n")
            print("Contacts saved to file.")
        except FileNotFoundError:
            print("Error: Could not save to file.")

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    name, phone = line.strip().split(',')
                    self.contacts[name] = phone
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

 
contact_book = ContactBook()
contact_book.load_from_file("contacts.txt")
 
