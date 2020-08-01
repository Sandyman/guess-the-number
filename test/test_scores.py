import unittest

from app.scores import Scores


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scores = Scores(num_high_scores=3)

    def test_high_scores_initially_empty(self):
        self.assertEqual(len(self.scores.high_scores), 0)

    def test_high_score_count_after_adding_a_high_score(self):
        name, score = "NAM", 600
        self.scores.store_high_score(score, name)
        self.assertEqual(len(self.scores.high_scores), 1)

    def test_high_score_actually_matches_add_high_score(self):
        name, score = "ABC", 600
        self.scores.store_high_score(score, name)
        _name, _score = self.scores.high_scores[0]
        self.assertEqual(_name, name)
        self.assertEqual(_score, score)

    def test_two_high_scores_must_be_ordered_by_score_descending(self):
        name1, score1 = "DEF", 400
        self.scores.store_high_score(score1, name1)

        name2, score2 = "ABC", 500
        self.scores.store_high_score(score2, name2)

        _name, _score = self.scores.high_scores[0]
        self.assertEqual(_name, name2)
        self.assertEqual(_score, score2)

    def test_multiple_high_scores_must_be_ordered_by_score_descending(self):
        _scores = [
            ("ABC", 500),
            ("DEF", 750),
            ("ZYX", 400),
        ]

        for name, score in _scores:
            self.scores.store_high_score(score, name)

        self.assertEqual(_scores[0], self.scores.high_scores[1])
        self.assertEqual(_scores[1], self.scores.high_scores[0])
        self.assertEqual(_scores[2], self.scores.high_scores[2])

    def test_scores_should_contain_at_most_the_maximum_number_of_high_scores(self):
        _scores = [
            ("ABC", 500),
            ("DEF", 750),
            ("ZYX", 400),
            ("GHI", 500),
        ]

        for name, score in _scores:
            self.scores.store_high_score(score, name)

        self.assertLessEqual(len(self.scores.high_scores), 3)


if __name__ == '__main__':
    unittest.main()
