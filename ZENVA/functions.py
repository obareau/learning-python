# Les fonctions sont un bon moyen de répéter du code
# Ca permet aussi de controller où et quand notre code
# S'éxécute
# Les fonces fonctions acceptent des valeurs en entrée
# Et on peut récuprer leurs sorties sous forme de résultat
# UNE FONCTION - UN BUT ET UN SEUL
# On simplifie et si c'est complexe on split en fonctions plus petites

position = 0

def move_player():
    global position
    position += 1
    print(position)

# Rien ne se passe tant que j'apelle pas ma fonction
move_player()
# Et je peux l'appeler autant de fois que je veux (Captain Obvious !!!)
move_player()
move_player()
move_player()
move_player()
