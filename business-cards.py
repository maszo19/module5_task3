from faker import Faker


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"

    @property
    def name_len(self):
        return len(self.first_name + " " + self.last_name)

    def contact(self):
        print(f"Dialing {self.phone} to contact {self}")


class BusinessContact(BaseContact):
    def __init__(self, company, business_phone, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.position.lower()} in {self.company}, <{self.email}>"

    def contact(self):
        print(f"Dialing {self.business_phone} to contact {self}")


def create_contacts(class_type, int):
    faker = Faker()
    list = []
    for i in range(int):
        name = faker.name()
        fname, lname = name.split(' ')
        domain = faker.free_email_domain()
        email = f"{fname.lower()}.{lname.lower()}@{domain}"
        phone = faker.phone_number()

        if class_type == "BaseContact":
            contact = BaseContact(first_name=fname, last_name=lname, phone=phone, email=email)
        elif class_type == "BusinessContact":
            com = faker.company()
            job = faker.job()
            b_phone = faker.phone_number()
            contact = BusinessContact(first_name=fname, last_name=lname, phone=phone, email=email, company=com,
                                      position=job, business_phone=b_phone)
        list.append(contact)
    return list


contacts = create_contacts("BaseContact", 3) + create_contacts("BusinessContact", 3)
for card in contacts:
    card.contact()
    print(f"The name is {card.name_len} chars long.")

sorted_by_name = sorted(contacts, key=lambda contact: contact.first_name)
sorted_by_surname = sorted(contacts, key=lambda contact: contact.last_name)

print("\nMy contacts sorted by first name:")
for card in sorted_by_name:
    print(card)

print("\nMy contacts sorted by last name:")
for card in sorted_by_surname:
    print(card)
