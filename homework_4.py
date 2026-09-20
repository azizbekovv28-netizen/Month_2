class Contact:
    def __init__(self, name,phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        return False

print(Contact.validate_phone_number("0707353059"))

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            raise ValueError("Неверный номер!")

ContactList.add_contact("Адиль", "0555443322")
ContactList.add_contact("Марат", "0707333555")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("Бектур", "022244345")
