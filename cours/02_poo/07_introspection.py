class Voiture():
    def __init__(self, marque, model):
        self.marque = marque
        self.model = model

    def klaxonner(self):
        return "tut tut !"

ma_voiture = Voiture("Peugeot", "508")

# Introspection
print(type(ma_voiture))
print(isinstance(ma_voiture, Voiture))
print(dir(ma_voiture))
print(getattr(ma_voiture, 'marque'))
print(hasattr(ma_voiture, 'model'))
print(callable(getattr(ma_voiture, 'klaxonner')))