import random
import time
from scores import Scores


class Game:
    def __init__(self):
        self.score = 1000

        self.time = int(time.time())

    def quit(self):
        print("Thanks for playing. Bye!")
        exit(0)

    def calculate_time_penalty(self):
        now = int(time.time())
        self.score -= now - self.time  # Subtract time penalty from score
        self.time = now

    def play(self, scores):
        print("*** Guess the number! ***")

        # Create a random secret number between 1 and 100 (inclusive)
        secret_number = random.randint(1, 100)

        while True:
            guess = input("What's your guess? ")
            if guess[0].lower() == 'q':
                self.quit()

            try:
                guess = int(guess)
            except ValueError:
                continue

            self.calculate_time_penalty()

            if guess == secret_number:
                print("You win! Your score is {}.".format(self.score))
                if scores.is_high_score(self.score):
                    print("*** High score! ***")
                    name = input("What's your name? ")
                    name = name[:3].upper()
                    scores.store_high_score(self.score, name[:3].upper())
                    print("Congratulions, {}!".format(name))
                break
            elif guess < secret_number:
                print("Oops. Your guess is too low! You lose!")
            else:
                print("Oops. Your guess is too high! You lose!")

            self.score = self.score // 2  # Only allow integer scores


if __name__ == '__main__':
    scores = Scores()

    game = Game()
    game.play(scores)
