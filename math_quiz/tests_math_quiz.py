import unittest
from math_quiz import get_random_integer, select_random_operation, compute_math_result


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operation(self):
        # Test if random operation are either + - or *
        for _ in range(1000):  # Test a large number of random operations
            rand_op = select_random_operation()
            self.assertTrue(rand_op in ['+', '*', '-'])

    def test_compute_math_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '-', '6 - 3', 3),
                (7, 4, '*', '7 * 4', 28),
                (8, 5, '+', '8 + 5', 13),
                (9, 6, '*', '9 * 6', 54),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                test_problem, test_answer = compute_math_result(num1, num2, operator)
                self.assertTrue(test_answer == expected_answer)
                self.assertTrue(test_problem == expected_problem)


if __name__ == "__main__":
    unittest.main()
