from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


class Contact:
    all_contacts = ContactList()

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


class Friend(Suplier, Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}, +48 {self.phone!r}'


c_1 = Contact("Adam", 'admam@wp.pl')
s = Suplier("Tomasz", "tomasz@wp")
f = Friend("Jarek", "jarek@wp.pl", '563454321')
print(c_1)
print(s)
print(f)
print(c_1.all_contacts)
s.order("kawa")
pprint(c_1.all_contacts)
print([s.name for c in Contact.all_contacts.search('Tomasz')])
# nadpisac słownik, i dopisac metode wyszukujaca najdłuzszy kluczcz

art = LongestKeyDict()
art['tomasz'] = 12
art['Abraham'] = 122
art['zen'] = 1
print(art.longest_key())
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>) - wynik __mro__
