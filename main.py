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
    GREEN = (0, 255, 0)

    pygame.mixer.music.load("ref/Maze.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    green_square_size = 40
    green_square_x = 20
    green_square_y = 590

    maze_paths = ["ref/MAZE.png", 'ref/maze_room2.png', 'ref/maze_room3.png','ref/The_End.png']
    current_maze_index = 0
    maze, mask = load_background_img(maze_paths[current_maze_index])

    square_size = 30
    square_x = 10
    square_y = 10
    start_x, start_y = square_x, square_y

    player_img = pygame.image.load("ref/Slime.png")
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

        if current_maze_index < len(maze_paths) - 1:
            player_rect = pygame.Rect(square_x, square_y, square_size, square_size)
            green_square_rect = pygame.Rect(green_square_x, green_square_y, green_square_size, green_square_size)

            if player_rect.colliderect(green_square_rect):
                current_maze_index += 1
                maze,mask = load_background_img(maze_paths[current_maze_index])
                if current_maze_index == 1:
                    green_square_x = 760
                    green_square_y = 590
                    # pygame.mixer.music.unload("ref/Maze.mp3")
                    # pygame.mixer.music.load("ref/Maze2.mp3")
                    # pygame.mixer.music.set_volume(0.7)
                    # pygame.mixer.music.play(-1)
                elif current_maze_index == 2:
                    green_square_x = 20
                    green_square_y = 590
                    # pygame.mixer.music.unload("ref/Maze2.mp3")
                    # pygame.mixer.music.load("ref/Maze3.mp3")
                    # pygame.mixer.music.set_volume(0.7)
                    # pygame.mixer.music.play(-1)
                elif current_maze_index == 3:
                    # pygame.mixer.music.unload("ref/Maze3.mp3")
                    # pygame.mixer.music.load("ref/Maze4.mp3")
                    # pygame.mixer.music.set_volume(0.7)
                    # pygame.mixer.music.play(-1)

        # if not pygame.mixer.music.get_busy():  # If not playing
        #     pygame.mixer.music.play()


        screen.fill("white")
        screen.blit(maze, (0, 0))
        if current_maze_index < len(maze_paths) - 1:
            pygame.draw.rect(screen, GREEN, (green_square_x, green_square_y, green_square_size, green_square_size))
            screen.blit(player_img, (square_x, square_y))



        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()
