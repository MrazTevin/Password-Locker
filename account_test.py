import unittest
from account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("Arnold", "@908street")

    def tearDown(self):
        """will do the cleanup after running each test case"""
        Account.account_list = []

    def test_init(self):
        """test if we instanstiated properly"""
        self.assertEqual(self.new_account.user_name, "Arnold")
        self.assertEqual(self.new_account.password, "@908street")

    def test_save_account(self):
        """
        we want to test if our account object is saved
           into the account list
        """
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list), 1)

    def test_save_multiple_account(self):
        """
        to help us save multiple accounts to
        our account_list
        """
        self.new_account.save_account()
        test_account = Account("Hashi", "hashish89")
        test_account.save_account()
        self.assertEqual(len(Account.account_list), 2)

    def test_delete_account(self):
        """we want to be able to delete a login account"""
        self.new_account.save_account()
        test_account = Account("Hashi", "hashish89")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.account_list), 1)

    def test_case_find_account_by_user_name(self):
        """find any account user_name and display it's information"""
        self.new_account.save_account()
        test_account = Account("Hashi", "hashish89")
        test_account.save_account()

        found_account = Account.find_by_user_name("Hashi")

        self.assertEqual(found_account.user_name, test_account.user_name)

    def test_account_exists(self):
        """to return  a boolean if we cannot find the account"""
        self.new_account.save_account()
        test_account = Account("Hashi", "hashish89")
        test_account.save_account()

        account_exists = Account.account_exist("Hashi")

        self.assertTrue(account_exists)


if __name__ == '__main__':
    unittest.main()
