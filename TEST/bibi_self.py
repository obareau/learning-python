class MaClasse:
    def __init__(self, nombre, nom):
        self.valeur = nombre
        self.nom = nom
    def affiche(self):
        print(self.valeur)
        print(self.nom)

truc = MaClasse(5,"olivier")
bidule = MaClasse(2, "alex")

truc.affiche()         # --> ?
bidule.affiche() 