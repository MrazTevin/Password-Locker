class Account:
    """Will generate instances of account"""
    account_list = []
    """this is a class variable called account_list"""
    def __init__(self, user_name, password):
        """Passed in 4 arguements and create 3 instance variables below"""
        self.user_name = user_name
        self.password = password
