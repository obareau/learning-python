# inheritance
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