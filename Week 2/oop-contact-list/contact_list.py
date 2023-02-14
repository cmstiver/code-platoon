class ContactList:
    def __init__(self):
        self.contacts = []
        pass

    def add_contact(self, name, number):
        self.contacts.append({
            "name": name,
            "number": number
        })
        pass

    def remove_contact(self, name):
        for i in range(len(self.contacts) - 1):
            contact = self.contacts[i]
            print(contact)
            if contact["name"] == name:
                self.contacts.pop(i)
        pass

    def find_shared_contacts(self, ContactList):
        my_list = []
        for x in self.contacts:
            if x in ContactList.contacts:
                my_list.append(x)
        return my_list


my_contacts = ContactList()
work_buddies = ContactList()

my_contacts.add_contact("Jane", "555")
my_contacts.add_contact("Josh", "333")
my_contacts.add_contact("Kyle", "444")

work_buddies.add_contact("Jane", "555")
work_buddies.add_contact("Josh", "333")
work_buddies.add_contact("Chayse", "777")

print(my_contacts.find_shared_contacts(work_buddies))
