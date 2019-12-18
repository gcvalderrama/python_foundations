import unittest


# The area   of    a   circle is defined as πr ^ 2.
# Estimate  π to  3  decimal  places  using   a  Monte    Carlo   method.
# Hint: The basic equation of a circle is x2 + y2 = r2.
# we will use a basic case with r = 1 , means area = π ^ 2 and x2 + y2 <=1
# pi = The ratio of a circle's circumference to its diameter
# https://www.youtube.com/watch?v=PLURfYr-rdU
import random


def get_rand_number(min_value, max_value):
    """
    This function gets a random number from a uniform distribution between
    the two input values [min_value, max_value] inclusively
    Args:
    - min_value (float)
    - max_value (float)
    Return:
    - Random number between this range (float)
    """
    range = max_value - min_value
    choice = random.uniform(0, 1)
    return min_value + range * choice


def estimate():
    square_points = 0
    circle_points = 0
    for i in range(1000000):
        x = get_rand_number(0, 1)
        y = get_rand_number(0, 1)
        dist = x ** 2 + y ** 2
        if dist <= 1:
            circle_points += 1
        square_points += 1

    pi = 4 * (circle_points / square_points)
    return pi


class Test(unittest.TestCase):

    def test_monte_carlo(self):
        print(estimate())



if __name__ == "__main__":
    unittest.main()


