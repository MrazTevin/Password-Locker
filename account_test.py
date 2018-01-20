import unittest
from account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("Arnold", "@908street")

    def test_init(self):
        """test if we instanstiated properly"""
        self.assertEqual(self.new_account.user_name, "Arnold")
        self.assertEqual(self.new_account.password, "@908street")

    
if __name__ == '__main__':
    unittest.main()
