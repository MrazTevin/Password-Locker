import unittest
from user import User


class TestUser(unittest.TestCase):


    def setUp(self):
        self.new_user = User("website", "user_name", "password")
    def test_init(self):
        """
        will test if we initialized our variables properly
        """
        self.assertEqual(self.new_user.website, "website")
        self.assertEqual(self.new_user.user_name, "user_name")
        self.assertEqual(self.new_user.password, "password")
    def test_save_user(self):
        """is the text_save_user saved into user_list?"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    def test_save_multiple_user(self):
        """we want to save multiple users to our user_list"""
        self.new_user.save_user()
        test_user = User("www.dropbox.com", "MrazHashid", "jheineahiko")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if  __name__ ==  '__main__':
    unittest.main()
