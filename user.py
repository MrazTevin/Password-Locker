class User:
    """Will generate instances of user"""
    user_list = []
    """this is a class variable called account_list"""
    def __init__(self, website, user_name, password):
        """Passed in 4 arguements and create 3 instance variables below"""
        self.website = website
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """saves user objects into user_list"""
        User.user_list.append(self)

    
