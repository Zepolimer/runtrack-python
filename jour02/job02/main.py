
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


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        if len(self.collection) == 0:
            print("Vous n'avez aucun livre.")
        else:
            print("Liste des livres en possession de %s %s:" % (self.prenom, self.nom))
            for livre in self.collection:
                livre.print()


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                self.catalogue[livre] = self.catalogue.get(livre, 0) + quantite
                print("Le livre '%s' a été ajouté au catalogue de la bibliothèque." % titre)
                return
        print("Le livre '%s' n'est pas dans l'œuvre de %s %s." % (titre, auteur.prenom, auteur.nom))

    def inventaire(self):
        if len(self.catalogue) == 0:
            print("La bibliothèque n'a aucun livre.")
        else:
            print("Liste des livres dans la bibliothèque %s:" % self.nom)
            for livre, quantite in self.catalogue.items():
                print("%s (%s exemplaires)" % (livre.titre, quantite))

    def louer(self, client, titre):
        for livre in self.catalogue:
            if livre.titre == titre and self.catalogue[livre] > 0:
                client.collection.append(livre)
                self.catalogue[livre] -= 1
                print("Le livre '%s' a été loué par %s %s."% (titre, client.prenom, client.nom))
                return
        print("Le livre '%s' n'est pas disponible dans la bibliothèque." % titre)

    def rendreLivres(self, client):
        for livre in client.collection:
            self.catalogue[livre] = self.catalogue.get(livre, 0) + 1
        client.collection = []


auteur1 = Auteur("Hugo", "Victor")
auteur1.SePresenter()

auteur1.ecrireUnLivre("Les Misérables")
auteur1.ecrireUnLivre("Notre-Dame de Paris")
auteur1.ecrireUnLivre("Essai")

auteur1.listerOeuvre()

bibliotheque1 = Bibliotheque('Librairie')

bibliotheque1.acheterLivre(
    auteur1,
    'Les Misérables',
    5
)
bibliotheque1.acheterLivre(
    auteur1,
    'Notre-Dame de Paris',
    5
)

print(".\n")
print('***** Livres achetés par la bibliothèque')
bibliotheque1.inventaire()

client1 = Client('Gaspard', 'Does')

bibliotheque1.louer(
    client1,
    'Les Misérables',
)
bibliotheque1.louer(
    client1,
    'Notre-Dame de Paris',
)

print(".\n")
print('***** Inventaire des livres loués à la bibliothèque')
bibliotheque1.inventaire()

bibliotheque1.rendreLivres(client1)

print(".\n")
print('***** Inventaire des livres rendus à la bibliothèque')
bibliotheque1.inventaire()

