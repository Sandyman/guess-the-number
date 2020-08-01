import random


class Game:
    def __init__(self):
        self.score = 1000

    def play(self):
        print("*** Guess the number! ***")

        # Create a random secret number between 1 and 100 (inclusive)
        secret_number = random.randint(1, 100)

        while True:
            guess = input("What's your guess? ")
            if guess[0].lower() == 'q':
                print("Thanks for playing. Bye!")
                exit(0)

            guess = int(guess)

            if guess == secret_number:
                print("You win! Your score is {}.".format(self.score))
                break
            elif guess < secret_number:
                print("Oops. Your guess is too low! You lose!")
            else:
                print("Oops. Your guess is too high! You lose!")

            self.score = self.score // 2  # Only allow integer scores


if __name__ == '__main__':
    game = Game()
    game.play()
