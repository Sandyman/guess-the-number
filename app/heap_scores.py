import heapq
import pickle
import time


class HeapScores:
    def __init__(self, num_high_scores=10, filename="high_scores.dat"):
        self.__high_scores = []

        self.__num_high_scores = num_high_scores

        self.__high_scores_filename = filename

    def __heappush(self, tup):
        heapq.heappush(self.__high_scores, tup)

    def __heappop(self):
        heapq.heappop(self.__high_scores)

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
        return [(score, name) for score, name in heapq.nlargest(10, self.__high_scores)]

    def is_high_score(self, score):
        """
        See if the score is a high score. We can use this to first check
        that a score is a high score. If this is indeed the case, the
        program an ask the player for their name.

        A score is a high score if we haven't reached the maximum number
        of high scores (see num_high_scores in the constructor) or if the
        reached score >= the lowest score we have. Because of the heap
        invariant, we know that the lowest score is in element [0] of the
        __high_scores list.

        In addition: newer scores will overwrite existing high scores if
        they have the same score.

        :param score: Score to check against high scores.
        :return: True if the score is a high score, False otherwise.
        """
        return len(self.__high_scores) < self.__num_high_scores \
               or score > self.__high_scores[0]

    def store_high_score(self, score, name):
        """
        Store this score along with the name of the player as a high score.
        We can simply push the new high score, as the heap will make sure
        the invariant remains valid. All we need to do is check the length
        and pop the first element, which, by definition, has the lowest
        score.

        Question: does this implementation push out entries that have the
        same score but are older? Or does it take into account the name
        field of the tuple in the ordering? Hmm....

        :param score: Score to store as a high score.
        :param name: Name that goes along with the high score.
        """
        self.__heappush((score, name))
        if len(self.__high_scores) > self.__num_high_scores:
            self.__heappop()

    def print_high_scores(self):
        """
        Convenience method that prints the high scores as a list.
        """
        print("*** HIGH SCORES ***")
        for score, name in self.__high_scores:
            print("{} : {}".format(name, score))
