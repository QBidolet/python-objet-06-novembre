mon_dict = {
    "nom": "BIDOLET",
    "prenom": "Quentin",
    "age": 29
}

print(type(mon_dict))
print(mon_dict)

# accéder à un élément
print(mon_dict["prenom"])

users = {
    "1": {
        "nom": "BIDOLET",
        "prenom": "Quentin",
        "age": 29
    },
    "2": {
        "nom": "DUPONT",
        "prenom": "Jean",
        "age": 42,
        "competences": ["HTML", "CSS", "Javascript", "Python"]
    }
}

# assigner une valeur
users["1"]["age"] = 55
print(users)

print('#' * 25)

# for
for element in users.keys():
    print(element)

for element in users.values():
    print(element)

print('#' * 25)
for cle, valeur in users.items():
    print(cle, valeur)