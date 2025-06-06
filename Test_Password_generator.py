import unittest
from password_generator import generate_password
import string

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        length = 12
        password = generate_password(length, True, True, True)
        self.assertEqual(len(password), length)

    def test_password_uppercase(self):
        password = generate_password(12, True, False, False)
        self.assertTrue(any(char in string.ascii_uppercase for char in password))

    def test_password_numbers(self):
        password = generate_password(12, False, True, False)
        self.assertTrue(any(char in string.digits for char in password))

    def test_password_special_chars(self):
        password = generate_password(12, False, False, True)
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_password_no_uppercase(self):
        password = generate_password(12, False, True, True)
        self.assertFalse(any(char in string.ascii_uppercase for char in password))

    def test_password_no_numbers(self):
        password = generate_password(12, True, False, True)
        self.assertFalse(any(char in string.digits for char in password))

    def test_password_no_special_chars(self):
        password = generate_password(12, True, True, False)
        self.assertFalse(any(char in string.punctuation for char in password))

if __name__ == "__main__":
    unittest.main()
