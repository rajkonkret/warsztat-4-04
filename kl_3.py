from pprint import pprint


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


# Adam, admam@wp.pl
# Tomasz, tomasz@wp
# z !r
# 'Adam', 'admam@wp.pl'
# 'Tomasz', 'tomasz@wp'


class Suplier(Contact):  # klasa dziedziczy po klasie Contact
    # pass  # słowko wypełnia cialo klasy ale nic nie robi
    def order(self, order: "Order"):
        print(f"{order} zamówiono od {self.name}")


c_1 = Contact("Adam", 'admam@wp.pl')
s = Suplier("Tomasz", "tomasz@wp")

print(c_1)
print(s)
print(c_1.all_contacts)
s.order("kawa")
pprint(c_1.all_contacts)

