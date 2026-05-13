import pygame as pg
import random
from molecule import Molecule

def main():
    pg.init()

    screen_width = 800
    screen_height = 600

    pg.display.set_caption('Броуновское движение')
    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()

    # Create molecules
    molecules = []
    for _ in range(random.randint(10, 30)):
        radius = random.randint(5, 20)
        molecules.append(Molecule(
            random.randint(radius, screen_width - radius),
            random.randint(radius, screen_height - radius),
            radius))
    
    run = True
    while run:
        # Checking the exit event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        screen.fill((0, 0, 0))
        
        # Moving all molecules 
        for m in molecules:
            m.update(screen_width, screen_height, molecules)
            m.display(screen)
        
        # Updating the screen
        pg.display.flip()
        # Limiting screen updates
        clock.tick(60)
    
    pg.quit()

if __name__ == '__main__':
    main()