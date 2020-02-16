import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    """
    Test Case to test functionality of User Model
    """

    def setUp(self):
        """
        setUp method initializes all our objects before tests
        """
        self.my_pass = 'testpass'
        self.new_user = User(username = 'test_user', email = "user@mail.com", password = self.my_pass)

    def test_password_hashing_functions(self):
        """
        test_password_hashing_functions test case to test if password attribute function works
        """
        self.assertIsNotNone(self.new_user.hash_pass)
        self.assertNotEqual(self.new_user.hash_pass, self.my_pass)

    def test_password_access_attribute_error(self):
        """
        test_password_access_attribute_error test case to test if password raises Attribute Error on access
        """
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        """
        test_password_verification test case to test if password verifies password correctly
        """
        self.assertTrue(self.new_user.verify_password(self.my_pass))
        self.assertFalse(self.new_user.verify_password("wrong_password"))
