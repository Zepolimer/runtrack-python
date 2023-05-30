
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


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print("Liste des livres de %s %s:" % (self.prenom, self.nom))
        for livre in self.oeuvre:
            livre.print()

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


auteur1 = Auteur("Hugo", "Victor")
auteur1.SePresenter()

auteur1.ecrireUnLivre("Les Misérables")
auteur1.ecrireUnLivre("Notre-Dame de Paris")

auteur1.listerOeuvre()
