import random


class Game:
    def __init__(self):
        self.score = 0

    def play(self):
        # Create a random secret number between 1 and 100 (inclusive)
        secret_number = random.randint(1, 100)


if __name__ == '__main__':
    game = Game()
    game.play()
