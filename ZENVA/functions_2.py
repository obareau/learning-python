position = 0 

def move_player(position, by_amount):
# si j'ai des paramétres il doivent avoir au moins 1 valeur
# Commome position est une param
# Pas besoin d'appeler la var position grace à global (vf functions.py)
    position += by_amount
    print(position)
    # C'est bien plus propre comme çà (eviter les gobal variables)
    return position
    #  return sans param = break et ne produit pas de valeurs
# je définis mes valeurs ici   
position = move_player (position, 5)
position = move_player (position, 2)
# Fin def valeurs 
print(position)
    