import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")


def draw_hangman(incorrect_guesses):
    hangman_images = [
        pygame.image.load("hangman0.png"),
        pygame.image.load("hangman1.png"),
        pygame.image.load("hangman2.png"),
        pygame.image.load("hangman3.png"),
        pygame.image.load("hangman4.png"),
        pygame.image.load("hangman5.png"),
        pygame.image.load("hangman6.png"),
    ]
    screen.blit(hangman_images[incorrect_guesses], (200, 100))


def handle_input(guessed_letters, word, incorrect_guesses):
    keys = pygame.key.get_pressed()
    for key in range(32, 127):
        if keys[key]:
            letter = chr(key)
            if letter not in guessed_letters:
                guessed_letters.append(letter)
                if letter in word:
                    print(f"Correct! '{letter}' is in the word.")
                else:
                    incorrect_guesses += 1
                    print(f"Incorrect! '{letter}' is not in the word.")


def draw_word(guessed_letters, word):
    screen.fill(WHITE)
    for i in range(len(word)):
        letter = word[i]
        if letter in guessed_letters:
            color = BLACK
        else:
            color = WHITE
        pygame.draw.circle(screen, color, (300 + i * 50, 300), 20)
        pygame.draw.circle(screen, BLACK, (300 + i * 50, 300), 20, 2)
        font = pygame.font.Font(None, 36)
        text = font.render(letter, True, BLACK)
        screen.blit(
            text, (300 + i * 50 - text.get_width() //
                   2, 300 - text.get_height() // 2)
        )


def main():
    # Choose a random word
    word = random.choice(["python", "programming", "pygame"])

    # Initialize variables for the hangman and guessed letters
    incorrect_guesses = 0
    guessed_letters = []
    maximum_guesses = len(word)

    # Run the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the hangman and word
        screen.fill(WHITE)
        draw_hangman(incorrect_guesses)
        draw_word(guessed_letters, word)

        # Handle input
        handle_input(guessed_letters, word, incorrect_guesses)

        # Update the display
        pygame.display.flip()

        # Check if the game is over
        if incorrect_guesses >= maximum_guesses:
            running = False
            print("Game over!")
        elif set(word) == set(guessed_letters):
            running = False
            print("You won!")

    # Game over
    pygame.quit()


if __name__ == "__main__":
    main()
