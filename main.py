import pygame
from pygame.examples.moveit import WIDTH, HEIGHT


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

    square_size = 50
    square_one_x = (WIDTH - square_size) // 2
    square_one_y = (HEIGHT - square_size) // 2

    square_two_x = -50
    square_two_y = (HEIGHT - square_size)

    pygame.mixer.music.load("Maze.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square_one_x -= STEP
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RIGHT:
                        square_one_x += STEP
                    elif event.key ==pygame.K_UP:
                        square_one_y -= STEP
                    elif event.key ==pygame.K_DOWN:
                        square_one_y += STEP


        screen.fill("purple")

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

        pygame.draw.rect(screen, BLUE, (square_one_x, square_one_y, square_size, square_size))
        pygame.draw.rect(screen, BLUE, (square_two_x, square_two_y, square_size, square_size))

        if square_two_x > WIDTH + 50:
            square_two_x = -50
        else:
            square_two_x += STEP


        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
