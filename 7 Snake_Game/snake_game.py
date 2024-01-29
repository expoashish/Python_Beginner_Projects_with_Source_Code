import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
display = pygame.display.set_mode((width, height))  # Create a game window
pygame.display.set_caption('Dev Duniya Snake Game')  # Set the window title

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position and size
snake_pos = [100, 50]  # Starting position of the snake's head
snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial segments of the snake's body

# Food position
food_pos = [random.randrange(1, (width//10)) * 10,  # Random position for food
            random.randrange(1, (height//10)) * 10]
food_spawn = True

# Direction
direction = 'RIGHT'  # Initial direction of the snake
change_to = direction

# Speed and clock
snake_speed = 12  # Snake movement speed
clock = pygame.time.Clock()  # Create a clock object to control frame rate

# Game Over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)  # Create a font object
    game_over_surface = my_font.render('Your Score is: ' + str(len(snake_body)), True, red)  # Render the game over text
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    display.blit(game_over_surface, game_over_rect)  # Display the game over text
    pygame.display.flip()
    time.sleep(5)  # Pause for 5 seconds
    pygame.quit()  # Quit Pygame
    quit()  # Quit Python program

# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Arrow keys to control
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validation of direction
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Moving the snake based on the chosen direction
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))  # Add the new head position
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False  # Snake has eaten the food
    else:
        snake_body.pop()  # Remove the tail segment

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10,  # Respawn food in a new random position
                    random.randrange(1, (height//10)) * 10]
    food_spawn = True

    display.fill(black)  # Fill the screen with black color
    
    # Draw Snake
    for pos in snake_body:
        pygame.draw.rect(display, green,pygame.Rect(pos[0], pos[1], 10, 10))  # Draw each segment of the snake's body

    # Draw Food
    pygame.draw.rect(display, white,pygame.Rect(food_pos[0], food_pos[1], 10, 10))  # Draw the food on the screen

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        game_over()  # Call the game over function
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()  # Update the display
    clock.tick(snake_speed)  # Control frame rate