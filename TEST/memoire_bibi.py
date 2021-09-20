class MaClasse:
    def __init__(self, nombre):
        self.valeur = nombre

    def affiche(self):
        print("Ma valeur à moi est {}".format(self.valeur))

    def adresse_memoire(self):
        return id(self)


truc = MaClasse(5)
bidule = MaClasse(2)

print("Truc est à l'adresse @{} et le self de Truc @{}".format(id(truc), truc.adresse_memoire()))
print("Est-ce que truc et self de truc sont à la même adresse mémoire ? {}".format(id(truc) == truc.adresse_memoire()))
print('------------')
print("Bidule est à l'adresse @{} et le self de Bidule @{}".format(id(bidule), bidule.adresse_memoire()))
print("Est-ce que bidule et self de bidule sont à la même adresse mémoire ? {}".format(id(bidule) == bidule.adresse_memoire()))