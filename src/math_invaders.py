# Import Required Libraries #

import pygame
import random
import math
from pygame import mixer
import sympy as sp
import os

# Find Current Absolute Path #
# TODO: Find a way to remove this entire variable #

cwd = os.path.dirname(os.path.abspath(__file__))

# Initialize PyGame Modules #

pygame.init()

# Load Game Icon #

icon = pygame.image.load(f"{cwd}/img/icon.png")

# Set Title and Icon #

pygame.display.set_icon(icon)
pygame.display.set_caption("Math Invaders")

# Create Window #

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Initialize Fonts #

font = pygame.font.Font(f"{cwd}/fonts/font.ttf", 20)

title_font = pygame.font.Font(f"{cwd}/fonts/font.ttf", 64)
button_font = pygame.font.Font(f"{cwd}/fonts/font.ttf", 32)

game_over_font = pygame.font.Font(f"{cwd}/fonts/font.ttf", 64)

# Draw Title Screen #


def title_screen():
    title_text = title_font.render("Math Invaders", True, (255, 255, 255))
    play_button_text = button_font.render("Play", True, (255, 255, 255))
    quit_button_text = button_font.render("Quit", True, (255, 255, 255))

    screen.blit(title_text, (150, 200))
    pygame.draw.rect(screen, (0, 128, 255), (300, 350, 200, 50))
    pygame.draw.rect(screen, (0, 128, 255), (300, 420, 200, 50))
    screen.blit(play_button_text, (350, 360))
    screen.blit(quit_button_text, (360, 430))

# Display Title Screen Every Frame #


def show_title_screen():
    # Call Drawing Function #

    title_screen()

    # Update Entire Screen #

    pygame.display.update()

    # Define Logic Variable #

    waiting_for_input = True

    # Actual Logic #

    while waiting_for_input:
        # Event Loop #
        for event in pygame.event.get():
            # Detect when the X button is hit, when hit, close game #
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Check for mouse clicks #

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Check if the Play button is clicked
                if 300 <= mouse_x <= 500 and 350 <= mouse_y <= 400:
                    waiting_for_input = False

                # Check if the Quit button is clicked
                elif 300 <= mouse_x <= 500 and 420 <= mouse_y <= 470:
                    pygame.quit()
                    quit()

        # Force game to run at the maximum of 30fps #

        pygame.time.Clock().tick(30)


# Score
score_val = 0
bullet_count = 10
scoreX = 5
scoreY = 5

# Bullet Positions #

bulletX = 650
bulletY = 5

# Symbols and Equations #

x = sp.symbols("x")

equations = [
    (
        sp.Eq(4 * x - 7, 9),
        [4]
    ),
    (
        sp.Eq(2 * (x + 3), 14),
        [4]
    ),
    (
        sp.Eq(5 * x + 2, 27),
        [5]
    ),
    (
        sp.Eq(3 * (x - 4), 15),
        [9]
    ),
    (
        sp.Eq(6 + 2 * x, 14),
        [4]
    ),
    (
        sp.Eq(4 * (x + 2) - 3, 29),
        [6]
    ),
    (
        sp.Eq(2 * x - 5, 15),
        [10]
    ),
    (
        sp.Eq(7 + 2 * (x - 3), 15),
        [7]
    ),
    (
        sp.Eq(9 * x + 5, 41),
        [4]
    ),
    (
        sp.Eq(-3 * x + 2, -10),
        [4]
    ),
    (
        sp.Eq(2 * (x + 4) + 3, 17),
        [3]
    ),
    (
        sp.Eq(5 * (x - 1) - 2, 18),
        [5]
    ),
    (
        sp.Eq(6 - 4 * x, -10),
        [4]
    ),
    (
        sp.Eq(2 * x - 3, x + 5),
        [8]
    ),
    (
        sp.Eq(2 * x + 1, x + 4),
        [3]
    ),
    (
        sp.Eq(3 * x + 2, 8),
        [2]
    ),
    (
        sp.Eq(4 * (x + 1) + 3, 15),
        [2]
    ),
    (
        sp.Eq(5 * (x - 2) - 4, 6),
        [4]
    ),
    (
        sp.Eq(2 * x - 3 * (x + 4), -17),
        [5]
    ),
    (
        sp.Eq(9 - 2 * (x + 1), 3),
        [2]
    ),
    (
        sp.Eq(7 - 3 * x, 16),
        [-3]
    ),
    (
        sp.Eq(4 * x + 1, 9),
        [2]
    ),
    (
        sp.Eq(3 * (x - 1) + 4, 7),
        [2]
    ),
    (
        sp.Eq(8 - 2 * x, 6),
        [1]
    ),
    (
        sp.Eq(4 * x - 5, 11),
        [4]
    ),
    (
        sp.Eq(9 - 3 * (x - 4), 0),
        [7]
    ),
]

# Rendering of score #


def show_score(x, y, bx, by):
    # Initialize text #

    score = font.render(
        f"Your Points: {score_val}",
        True,
        (
            255,
            255,
            255
        )
    )

    # Draw text #

    screen.blit(score, (x, y))

    # Ditto #

    bullet_text = font.render(
        f"Bullets: {bullet_count}",
        True,
        (
            255,
            255,
            255
        )
    )
    screen.blit(bullet_text, (bx, by))

# Game over rendering #


def game_over():
    game_over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(game_over_text, (190, 250))


# Background music
mixer.music.load(f"{cwd}/audio/music.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# loading the player image and location
playerImage = pygame.image.load(f"{cwd}/img/spaceship.png")
player_X = 370
player_Y = 523
player_Xchange = 0

# defining index brackets for the enemy's
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 3

# Generate enemies #

for num in range(no_of_invaders):
    # Add a new instance of the alien image into the array #

    invaderImage.append(pygame.image.load(f"{cwd}/img/alien.png"))

    # Set x and y coords of the alien #

    pos_x = random.randint(64, 737)
    pos_y = random.randint(30, 180)

    # Check if the invaders are stacking. If yes, #
    # regenerate and repeat check steps #

    while pos_x in invader_X and pos_y in invader_Y:
        pos_x = random.randint(64, 737)
        pos_y = random.randint(30, 180)

    # After passing checks, append x, y, and velocity to respective arrays #

    invader_X.append(pos_x)
    invader_Y.append(pos_y)

    invader_Xchange.append(0.6)
    invader_Ychange.append(50)

# pew pew
bulletImage = pygame.image.load(f"{cwd}/img/bullet.png")
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 5
bullet_state = "rest"


# Input box setup
class InputBox:
    def __init__(self, x, y, w, h):
        # Set Rectangle #
        self.rect = pygame.Rect(x, y, w, h)

        # Set initial colour #
        self.color = (173, 216, 230)

        # Set text content #
        self.text = ""

        # Make the text object #
        self.txt_surface = font.render(self.text, True, (0, 0, 0))

        # Set whether or not it's active or not #
        self.active = False

    def handle_event(self, event):
        # Check if has been clicked. Activate and change colour if yes #
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = (173, 216, 230)
            else:
                self.active = False
                self.color = (255, 255, 255)

        # Keypress event #
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # Process the input here (you can use self.text)
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # Re-render text #
                self.txt_surface = font.render(self.text, True, (0, 0, 0))

    def update(self):
        # Set max width #
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Actually draw the InputBox #
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


# Collision detection function #


def isCollision(x1, x2, y1, y2):
    # Calculate distance #
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))

    # Check if it is close enough #
    if distance <= 50:
        return True
    else:
        return False

# Render Player #


def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))

# Invader now #


def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

# Bullet now #


def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"


# Input box setup
input_box = InputBox(100, 550, 140, 32)

# Choose the first equation outside the game loop
equation, correct_answers = random.choice(equations)

# Show title screen #

show_title_screen()

# Once done, set "alive"/running variable and #

running = True

# * MAIN GAME LOOP * #

while running:
    # Clear Screen #

    screen.fill((0, 0, 0))

    # Event Loop #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player_Xchange = -1.7
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
            if event.key == pygame.K_SPACE and bullet_count > 0:
                # Bullet logic #

                if bullet_state == "rest":
                    bullet_X = player_X

                    # Draw bullet #

                    bullet(bullet_X, bullet_Y)

                    # Play song #

                    bullet_sound = mixer.Sound(f"{cwd}/audio/bruh.wav")
                    bullet_sound.play()

                    # Deduct bullets #

                    bullet_count -= 1
        if event.type == pygame.KEYUP:
            player_Xchange = 0

        # Handle events for the input box
        input_box.handle_event(event)

    # Move player and invaders #

    player_X += player_Xchange

    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]

    # bullet movement
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

    # Equation text and positioning #

    equation_text = f"Solve for X: {sp.pretty(equation)}"

    equation_surface = font.render(equation_text, True, (255, 255, 255))

    textRect = equation_surface.get_rect()

    textRect.center = (118, 50)

    # Draw text #

    screen.blit(equation_surface, textRect)

    # Answer checker #

    # Text in box and no focus #

    if not input_box.active and input_box.text:
        # Get answer #

        # Check if answer is valid, if it isn't, remove text om text box #

        try:
            user_answer = sp.sympify(input_box.text)
        except sp.SympifyError:
            input_box.text = ""

        if user_answer not in correct_answers:
            # Set text surface and draw #
            incorrect_text = font.render(
                "Incorrect. Try again.",
                True,
                (
                    255,
                    0,
                    0
                )
            )
            screen.blit(incorrect_text, (50, 100))

            # Update entire screen #
            pygame.display.flip()

            # 1 second delay #

            pygame.time.delay(1000)

            # Reset text #

            input_box.text = ""
        else:
            # Ditto #
            correct_text = font.render("Correct!", True, (0, 255, 0))
            screen.blit(correct_text, (50, 100))
            pygame.display.flip()
            pygame.time.delay(1000)

            # Increase bullets #

            bullet_count += 5

            # Choose new equation #

            equation, correct_answers = random.choice(equations)

            # Reset #

            input_box.text = ""

        # Reset Again #

        input_box.text = ""

    # * WIN CONDITIONS * #

    if score_val >= 50:
        # Make surface and draw #

        win_text = game_over_font.render("You Win!", True, (0, 255, 0))
        screen.blit(win_text, (190, 250))

        # Update entire screen #

        pygame.display.update()

        # Wait 2 seconds #

        pygame.time.delay(2000)

        # Play sound #

        win_sound = mixer.Sound(f"{cwd}/audio/win.mp3")
        win_sound.play()

        # Kill game #

        pygame.quit()
        running = False

    # game over
    for i in range(no_of_invaders):
        # If touching player then die and play sound #

        if invader_Y[i] >= 450:
            if abs(player_X - invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    explosion_sound = mixer.Sound(f"{cwd}/audio/explosion.mp3")
                    explosion_sound.play()
                game_over()
                break

        # If touches other side, bounce back #

        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]

        # Killing aliens #

        collision = isCollision(bullet_X, invader_X[i], bullet_Y, invader_Y[i])

        if collision:
            score_val += 1
            bullet_Y = 600

            # Reset #

            bullet_state = "rest"
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_Xchange[i] *= -1

        # Draw invader #

        invader(invader_X[i], invader_Y[i], i)

    # Add side barriers #

    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750

    # Draw player #

    player(player_X, player_Y)

    # Update the input box
    input_box.update()

    # Display score and bullet count
    show_score(scoreX, scoreY, bulletX, bulletY)

    # Draw the input box
    input_box.draw(screen)

    # Update entire screen #

    pygame.display.update()

# Kill pygame #

pygame.quit()


# Kill Python #
quit()
