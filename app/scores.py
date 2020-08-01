class Scores:
    def __init__(self, num_high_scores=10):
        self.__high_scores = []

        self.__num_high_scores = num_high_scores

    @property
    def high_scores(self):
        return self.__high_scores

    def is_high_score(self, score):
        """
        See if the score is a high score. We can use this to first check
        that a score is a high score and only if that is the case ask for
        the player's name.
        A score is a high score if we haven't reached the maximum number
        of high scores (see NUM_HIGH_SCORES) or if the reached score is
        larger than OR EQUAL TO the lowest score we have.

        :param score: Score to check against high scores.
        :return: True if the score is a high score, False otherwise.
        """
        return len(self.__high_scores) < self.__num_high_scores \
               or score >= self.__high_scores[-1][1]

    def store_high_score(self, score, name):
        """
        Store this score along with the name of the player as a high score.

        :param score: Score to store as a high score.
        :param name: Name that goes along with the high score.
        """
        insert_at = [i for i, v in enumerate(self.__high_scores) if v[1] <= score]
        if not insert_at:
            self.__high_scores.append((name, score))
        else:
            self.__high_scores.insert(insert_at[0], (name, score))
            self.__high_scores = self.__high_scores[:self.__num_high_scores]
