import pygame as pg
import random

class Molecule:
    '''
    Represents a moving molecule in a simulation.
    Handles position updates, wall collisions, interactions with other
    molecules, and drawing the instance on the Pygame screen.
    '''
    def __init__(self, x, y, radius):
        '''
        Initialize a new Molecule instance.

        :param x: Initial X-coordinate.
        :param y: Initial Y-coordinate.
        :param radius: The visual radius of the molecule.
        '''
        # Coordinates
        self.x = x
        self.y = y
        # Radius of molecul
        self.radius = radius
        # Motion vectors 
        self.vector_x = random.uniform(-3, 3)
        self.vector_y = random.uniform(-3, 3)
        
    def update(self, screen_width, screen_height, molecules):
        '''
        Update the position and velocity of the molecule.
        Applies random movement, enforces a speed limit, manages wall 
        collisions, and resolves collisions with other molecules.

        :param screen_width: Width of the simulation area.
        :param screen_height: Height of the simulation area.
        :param molecules: A list of all Molecule objects in the simulation.
        '''        
        # Speed limit
        max_speed = 5

        # Random change of motion vectors with speed limit
        self.vector_x = max(-max_speed, 
                            min(max_speed,
                                self.vector_x + random.uniform(-1, 1)))
        self.vector_y = max(-max_speed, 
                            min(max_speed,
                                self.vector_y + random.uniform(-1, 1)))
        
        # Update position of molecule
        self.x += self.vector_x
        self.y += self.vector_y
        
        # Bouncing off the screen walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.vector_x *= -1
            
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.vector_y *= -1
        
        # Collision of molecules
        for other in molecules:
            if other is self:
                continue
                
            d_x = other.x - self.x
            d_y = other.y - self.y
            distance = (d_x ** 2 + d_y ** 2) ** 0.5
            
            # If molecules collide, we exchange speeds
            if distance < self.radius + other.radius:
                self.vector_x, other.vector_x = other.vector_x, self.vector_x
                self.vector_y, other.vector_y = other.vector_y, self.vector_y
        
    def display(self, screen):
        '''
        Draw the molecule on the screen.
        :param screen: The Pygame surface to draw on.
        '''
        pg.draw.circle(screen, 
                       (0, 0, 255), 
                       (int(self.x), int(self.y)), 
                       self.radius)