# values // Refrences
class GameObject:
    # blueprint est défini ici
    def __init__(self, name, x_pos, y_pos) :
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    #  Faisons bouger notre GameObject
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount
    # Fin du blueprint

       
game_object = GameObject ("Enemy", 1, 2)
# On accéde à la variable name de l'objet game_objet
# print (game_object.name)
# On réassigne name dans le game_object
game_object.name = "Enemy 1"
print ("Enemy Object")

print (game_object.name)
print (game_object.x_pos)
print (game_object.y_pos)
game_object.move (5, 10) #le param self n'est pas nécéssaire
print ("new position")
print (game_object.x_pos)
print (game_object.y_pos)
other_game_object = GameObject("Player", 2, 0)
print("Player Object")
print (other_game_object.name)
print (other_game_object.x_pos)
print (other_game_object.y_pos)

# Values
print ("---------------")
print ("Exaxample Value")
one_int = 10
another_int = one_int
print (one_int)
print (another_int)

another_int = 10
print (one_int)
print (another_int)

print ("---------------")

# References
other_game_object = game_object # les 2 objects sont désormais identiques
print(other_game_object.name)
other_game_object.name = "new name"
print (other_game_object.name)
print ( game_object.name)
