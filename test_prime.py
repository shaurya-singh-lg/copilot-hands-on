# FILE: /workspaces/copilot-hands-on/test_prime.py
import unittest
from prime import prime

class TestPrime(unittest.TestCase):
    def test_prime_1(self):
        self.assertFalse(prime(1))

    def test_prime_2(self):
        self.assertTrue(prime(2))

    def test_prime_3(self):
        self.assertTrue(prime(3))

    def test_prime_4(self):
        self.assertFalse(prime(4))

    def test_prime_5(self):
        self.assertTrue(prime(5))

    def test_prime_10(self):
        self.assertFalse(prime(10))

    def test_prime_11(self):
        self.assertTrue(prime(11))

    def test_prime_13(self):
        self.assertTrue(prime(13))

    def test_prime_17(self):
        self.assertTrue(prime(17))

    def test_prime_19(self):
        self.assertTrue(prime(19))

if __name__ == '__main__':
    unittest.main()