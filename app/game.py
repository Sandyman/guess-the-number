import random


class Game:
    def __init__(self):
        self.score = 0

    def play(self):
        # Create a random secret number between 1 and 100 (inclusive)
        secret_number = random.randint(1, 100)

        guess = input("What's your guess? ")
        guess = int(guess)

        if guess == secret_number:
            print("You win!")
        elif guess < secret_number:
            print("Oops. Your guess is too low! You lose!")
        else:
            print("Oops. Your guess is too high! You lose!")


if __name__ == '__main__':
    game = Game()
    game.play()
