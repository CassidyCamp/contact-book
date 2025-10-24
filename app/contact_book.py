from rich.console import Console
from rich.table import Table

from app.contact import Contact
from app.storage import Storage


console = Console()

class ContactBook:

    def __init__(self):
        self.storage = Storage()
    
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.storage.save(contact)

    def show_all(self):
        get_contacts = self.storage.read_db()
        
        table = Table(title="Contacts", title_style="bold")
        
        table.add_column("№", style="bold")
        table.add_column("Name", style="yellow")
        table.add_column("Phone")
        table.add_column("Eamil", style="blue")
        
        for index, contact in enumerate(get_contacts, start=1):
            table.add_row(f"{index}", contact["name"], f"{contact['phone']}", contact["email"])
        
        console.print(table)
        

    def search_contact(self, contact_name):
        get_contacts = self.storage.read_db()
        
        table = Table(title="Results", title_style="bold")
        
        table.add_column("Name", style="yellow")
        table.add_column("Phone")
        table.add_column("Eamil", style="blue")
        
        for index, contact in enumerate(get_contacts, start=1):
            if contact_name.lower() in contact["name"].lower():
                table.add_row(f"{index}", contact["name"], f"{contact['phone']}", contact["email"])
        
        console.print(table)
        
    
    def update_task(self, contact_num):
        get_contacts = self.storage.read_db()
        contact = get_contacts[contact_num - 1]
        print()
        print(f"1. Update Name ({contact['name']})")
        print(f"2. Update Phone ({contact['phone']})")
        print(f"3. Update Email ({contact['email']})")
        print()
        
        update_type = ["name", "phone", "email"]
        
        choice = int(input("Enter your choice (1-3): "))
        
        new_date = input(f"Enter new {update_type[choice - 1]}: ")
        
        contact[update_type[choice - 1]] = new_date
                
        self.storage.save(contact)
        
        
