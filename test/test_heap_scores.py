import unittest

from app.heap_scores import HeapScores


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scores = HeapScores(num_high_scores=3)

    def test_high_scores_initially_empty(self):
        self.assertEqual(len(self.scores.high_scores), 0)

    def test_high_score_count_after_adding_a_high_score(self):
        score, name = 600, "NAM"
        self.scores.store_high_score(score, name)
        self.assertEqual(len(self.scores.high_scores), 1)

    def test_high_score_actually_matches_add_high_score(self):
        score, name = 600, "ABC"
        self.scores.store_high_score(score, name)
        _score, _name = self.scores.high_scores[0]
        self.assertEqual(_name, name)
        self.assertEqual(_score, score)

    def test_two_high_scores_must_be_ordered_by_score_descending(self):
        score1, name1 = 400, "DEF"
        self.scores.store_high_score(score1, name1)

        score2, name2 = 500, "ABC"
        self.scores.store_high_score(score2, name2)

        _score, _name = self.scores.high_scores[0]
        self.assertEqual(_name, name2)
        self.assertEqual(_score, score2)

    def test_multiple_high_scores_must_be_ordered_by_score_descending(self):
        _scores = [
            (500, "ABC"),
            (750, "DEF"),
            (400, "ZYX"),
        ]

        for score, name in _scores:
            self.scores.store_high_score(score, name)

        self.assertEqual(_scores[0], self.scores.high_scores[1])
        self.assertEqual(_scores[1], self.scores.high_scores[0])
        self.assertEqual(_scores[2], self.scores.high_scores[2])

    def test_scores_should_contain_at_most_the_maximum_number_of_high_scores(self):
        _scores = [
            (500, "ABC"),
            (750, "DEF"),
            (400, "ZYX"),
            (300, "GHI"),
        ]

        for score, name in _scores:
            self.scores.store_high_score(score, name)

        self.assertLessEqual(len(self.scores.high_scores), 3)

    def test_score_that_is_too_low_should_not_be_stored(self):
        _scores = [
            (500, "ABC"),
            (750, "DEF"),
            (400, "ZYX"),
            (300, "GHI"),
        ]

        for score, name in _scores:
            self.scores.store_high_score(score, name)

        self.assertLessEqual(len(self.scores.high_scores), 3)
        self.assertEqual(_scores[2], self.scores.high_scores[-1])

    def test_new_entry_with_same_score_should_replace_older_entry(self):
        _scores = [
            (550, "ABC"),
            (700, "DEF"),
            (450, "ZYX"),
            (450, "GHI"),  # should overwrite the previous one...
        ]

        for score, name in _scores:
            self.scores.store_high_score(score, name)

        self.assertEqual(_scores[3], self.scores.high_scores[-1])


if __name__ == '__main__':
    unittest.main()
