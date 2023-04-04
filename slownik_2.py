class MyDict(dict):
    def __missing__(self, key):
        return 'Nie ma takiego klucza'


class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())  # lower() - zmienia na małe
        return None


dictionary = {'name': 'Radek'}
d = MyDict()
d['name'] = 'Radek'
print(d['imie'])
print(d['Name'])

d2 = DefaultDict()
d2['name'] = 'Radek'
print(d2['imie'])
print(d2)

d3 = AutoKeyDict()
d3['name'] = 'Radek'
print(d3['imie'])
print(d3)

d4 = CaseInsensitiveDict()
d4['name'] = 'Radek'
print(d4['Name'])
