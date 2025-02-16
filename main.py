import pygame
from pygame.examples.moveit import WIDTH, HEIGHT
def load_background_img(url):
    maze = pygame.image.load(url).convert()
    mask = pygame.mask.from_threshold(maze, (0, 0, 0, 255), (1, 1, 1, 255))
    return maze, mask

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Super Labyrinth Game")
    clock = pygame.time.Clock()
    running = True

    STEP = 10

    WHITE = (255, 255, 255)
    RED = (255,0,0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    green = (0, 255, 0)

    maze, mask = load_background_img("maze.png")

    square_size = 30
    square_x = 10
    square_y = 10
    start_x, start_y = square_x, square_y

    player_img = pygame.image.load("Slime.png")
    player_img = pygame.transform.scale(player_img, (square_size, square_size))

    square_two_x = -50
    square_two_y = (HEIGHT - square_size)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square_x -= STEP
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RIGHT:
                        square_x += STEP
                    elif event.key ==pygame.K_UP:
                        square_y -= STEP
                    elif event.key ==pygame.K_DOWN:
                        square_y += STEP

        square_mask = pygame.Mask((square_size, square_size), fill=True)

        if mask.overlap(square_mask, (square_x, square_y)) is not None:
            square_x, square_y = start_x, start_y
        screen.fill("white")
        screen.blit(maze, (0, 0))
        screen.blit(player_img, (square_x, square_y))



        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
