# Les fonctions sont un bon moyen de répéter du code
# Ca permet aussi de controller où et quand notre code
# S'éxécute
# Les fonces fonctions acceptent des valeurs en entrée
# Et on peut récuprer leurs sorties sous forme de résultat
# UNE FONCTION - UN BUT ET UN SEUL
# On simplifie et si c'est complexe on split en fonctions plus petites
# test
position = 0
# position est hors de ma fonction
# move_player() # rien ne se passe vu que ma fonction n'est pas encore définie du coup le programme crash
def move_player():
    global position # Je dois donc utiliser global si je veux acceder à position
    position += 1
    print(position)
    # x_position = position
# print(x_position) x_position n'est pas accessible d'ailleur elle n'est pas dispo à la complétion   
# Rien ne se passe tant que j'apelle pas ma fonction
move_player()
# Et je peux l'appeler autant de fois que je veux (Captain Obvious !!!)
move_player()
move_player()
move_player()
move_player()
 