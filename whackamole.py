import pygame
import random


def main():
    try:
        pygame.init()
        sq_wid = 32
        grid_wid = 20
        mole_image = pygame.image.load("mole.png")
        mole_x = 0
        mole_y = 0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (mole_x<=event.pos[0]) and (event.pos[0]<=mole_x+32) and (mole_y<=event.pos[1]) and (event.pos[1]<=mole_y+32):
                        mole_x = 32*random.randrange(0, 19)
                        mole_y = 32*random.randrange(0, 15)
            screen.fill("light green")
            for i in range(0,grid_wid):
                pygame.draw.line(screen, (0, 0, 0), (0+i*sq_wid, 0), (0+i*sq_wid, 512))
                pygame.draw.line(screen, (0,0,0), (0, 0+i*sq_wid), (640, 0+i*sq_wid))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
