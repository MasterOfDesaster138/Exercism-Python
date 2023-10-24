"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    
    def __init__(self, x: int, y: int):
        self.health = 3
        self.x_coordinate = x
        self.y_coordinate = y
        Alien.total_aliens_created += 1
        
    def hit(self) -> int:
        self.health = self.health - 1
        return self.health
    
    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        else:
            return True
        
    def teleport(self, new_x_coordinate: int, new_y_coordinate: int):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
        
    def collision_detection(self, other):
        pass 
    


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(new_aliens_start_positions: list) -> list:
    aliens = list()
    for coordinates in new_aliens_start_positions:
        aliens.append(Alien(coordinates[0], coordinates[1]))
    return aliens