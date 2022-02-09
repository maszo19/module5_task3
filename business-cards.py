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
for card in contacts:
    print(card)
