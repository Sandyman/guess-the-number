import pickle


class ListScores:
    def __init__(self, num_high_scores=10, filename="high_scores.dat"):

        # A list to hold the actual high scores as (name, score)-tuples
        self.__high_scores = []

        # Maximum number of high scores to store
        self.__num_high_scores = num_high_scores

        # Filename of high scores file
        self.__high_scores_filename = filename

    def __enter__(self):
        """
        Contextmanager entry point. Try to load the high scores from
        a file, but simply fail silently if this doesn't work.
        """
        try:
            with open(self.__high_scores_filename, 'rb') as f:
                self.__high_scores = pickle.load(f)
        except OSError:
            pass

    def __exit__(self, unused_exc_type, unused_exc_val, unused_exc_tb):
        """
        Context manager exit point. Try to save the high scores to a
        file, but simply fail silently if this doesn't work.
        """
        try:
            with open(self.__high_scores_filename, 'wb') as f:
                pickle.dump(self.__high_scores, f)
        except OSError:
            pass

    @property
    def high_scores(self):
        return self.__high_scores

    def is_high_score(self, score):
        """
        See if the score is a high score. We can use this to first check
        that a score is a high score. If this is indeed the case, the
        program an ask the player for their name.

        A score is a high score if we haven't reached the maximum number
        of high scores (see num_high_scores in the constructor) or if the
        reached score >= the lowest score we have.

        In addition: newer scores will overwrite existing high scores if
        they have the same score.

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

    def print_high_scores(self):
        """
        Convenience method that prints the high scores as a list.
        """
        print("*** HIGH SCORES ***")
        for name, score in self.__high_scores:
            print("{} : {}".format(name, score))
