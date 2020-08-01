import random
import time
from scores import Scores


class Game:
    def __init__(self):
        self.score = 1000

        self.time = int(time.time())

    @staticmethod
    def __quit():
        print("Thanks for playing. Bye!")
        exit(0)

    def __calculate_round_penalty_and_update_score(self):
        """
        This method calculates the round penalty and updates the score.
        """
        self.score = int(self.score / 1.15)  # Only allow integer scores

    def __calculate_time_penalty_and_update_score(self):
        """
        This method calculates the time penalty and updates the score.
        """
        now = int(time.time())
        self.score -= now - self.time  # Subtract time penalty from score
        self.time = now

    def __handle_high_score(self, scoring):
        print("*** High score! ***")
        name = input("What's your name? ")
        name = name[:3].upper()
        scoring.store_high_score(self.score, name[:3].upper())
        scoring.print_high_scores()

    def play(self, scoring):
        print("*** Guess the number! ***")

        with scoring:
            self.__play_round(scoring)

        print("*** Thanks for playing the game! ***")

    def __play_round(self, scoring):
        # Create a random secret number between 1 and 100 (inclusive)
        secret_number = random.randint(1, 100)

        while True:
            guess = input("What's your guess? ")
            if guess[0].lower() == 'q':
                self.__quit()

            try:
                guess = int(guess)
            except ValueError:
                continue

            self.__calculate_time_penalty_and_update_score()

            if guess == secret_number:
                print("You win! Your score is {}.".format(self.score))
                if scoring.is_high_score(self.score):
                    self.__handle_high_score(scoring)

                break

            self.__calculate_round_penalty_and_update_score()

            print("Oops. Your guess is too {}!".format("low" if guess < secret_number else "high"))


if __name__ == '__main__':
    scores = Scores()

    game = Game()
    game.play(scores)
