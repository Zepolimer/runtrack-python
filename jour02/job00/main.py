
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Bonjour, je m'appelle %s %s." % (self.prenom, self.nom))

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom


personne1 = Personne("Dupont", "Jean")
personne2 = Personne("Martin", "Lucie")

personne1.SePresenter()
personne2.SePresenter()

personne1.set_nom("Durand")
personne1.set_prenom("Pierre")

print(personne1.get_nom())
print(personne1.get_prenom())
