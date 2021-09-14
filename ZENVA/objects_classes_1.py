class GameObject:
    # blueprint est défini ici
    def __init__(self, name, x_pos, y_pos) :
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    # Fin du blueprint
    
game_object = GameObject ("Enemy", 1, 2)
# On accéde à la variable name de l'objet game_objet
print (game_object.name)
# On réassigne name dans le game_object
game_object.name = "Ennemy 1"
print (game_object.name)