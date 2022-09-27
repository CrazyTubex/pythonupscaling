from tests.upscale_test import TestUpScale
import unittest


def main():
    up = TestUpScale(unittest.TestCase)
    up.test_setup()


if __name__ == '__main__': 
    unittest.main()

