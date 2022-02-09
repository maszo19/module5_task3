from faker import Faker


class BusinessCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"


def create_contacts(int):
    faker = Faker()
    list = []
    for i in range(int):
        name = faker.name()
        fname, lname = name.split(' ')
        com = faker.company()
        job = faker.job()
        domain = faker.free_email_domain()
        email = f"{fname.lower()}.{lname.lower()}@{domain}"
        contact = BusinessCard(first_name=fname, last_name=lname, company=com, position=job, email=email)
        list.append(contact)
    return list


contacts = create_contacts(5)
sorted_by_name = sorted(contacts, key=lambda contact: contact.first_name)
sorted_by_surname = sorted(contacts, key=lambda contact: contact.last_name)

print("\nMy contacts sorted by first name:")
for card in sorted_by_name:
    print(card)

print("\nMy contacts sorted by last name:")
for card in sorted_by_surname:
    print(card)
