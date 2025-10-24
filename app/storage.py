import json
import os

from app.contact import Contact


class Storage:

    def __init__(self):
        self.filename = "database/contacts.json"

    def read_db(self) -> str:
        if not os.path.exists("database"):
            os.mkdir("database")
            with open(self.filename, "w") as f:
                json.dump([], f)
                
        if os.path.getsize(self.filename) == 0:
            with open(self.filename, "w") as f:
                json.dump([], f)
            
        with open(self.filename, "r") as f:
            return json.load(f)
    
    
    def save(self, contact: Contact):
        contact_dict = contact.to_dict()
        
        get_contact_dict = self.read_db()
        get_contact_dict.append(contact_dict)

        if os.path.exists("database"):
            with open(self.filename, "w") as f:
                json.dump(get_contact_dict, f, indent=4)
        else:
            os.mkdir("database")
            with open(self.filename, "w") as f:
                json.dump(get_contact_dict, f, indent=4)
                
        
        
