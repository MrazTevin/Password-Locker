import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("elitesingles.com", "Khalid", "hot96%")

    def tearDown(self):
        """will cleanup after running the text cases"""
        User.user_list = []

    def test_init(self):
        """
        will test if we initialized our variables properly
        """
        self.assertEqual(self.new_user.website, "elitesingles.com")
        self.assertEqual(self.new_user.user_name, "Khalid")
        self.assertEqual(self.new_user.password, "hot96%")

    def test_save_user(self):
        """is the text_save_user saved into user_list?"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        """we want to save multiple users to our user_list"""
        self.new_user.save_user()
        test_user = User("googledocs.com", "Nadra", "misru")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """let's see if we can remove a user here"""
        self.new_user.save_user()
        test_user = User("elitesingles.com", "Khalid", "hot96%")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
