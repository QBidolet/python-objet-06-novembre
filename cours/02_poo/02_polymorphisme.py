class Chat:
    def parler(self):
        return "Miaou !"


class Chien:
    def parler(self):
        return "Waf waf !"


def faire_parler(animal):
    print(animal.parler())


chat = Chat()
chien = Chien()
faire_parler(chat)
faire_parler(chien)

class Animal:
    def parler(self):
        return "..."

class Chat(Animal):
    def parler(self):
        return "Miaou !"

class Chien(Animal):
    def parler(self):
        return "Waf waf !"