class Scores:
    NUM_HIGH_SCORES = 10

    def __init__(self):
        self.__high_scores = []

    def is_high_score(self, score):
        """
        See if the score is a high score. We can use this to first check
        that a score is a high score and only if that is the case ask for
        the player's name.

        :param score: Score to check against high scores.
        :return: True if the score is a high score, False otherwise.
        """
        return True

    def store_high_score(self, score, name):
        """
        Store this score as a high score along with the name of the player.

        :param score: Score to store as a high score.
        :param name: Name that goes along with the high score.
        """
        pass
