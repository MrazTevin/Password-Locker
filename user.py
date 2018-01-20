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

    def delete_user(self):
        """we want to make our delete user test to pass"""

        User.user_list.remove(self)

    @classmethod
    def find_by_website(cls, website):

        for user in cls.user_list:
            if user.website == website:
                return user

    @classmethod
    def display_users(cls):
        """this method will return the user_list"""
        return cls.user_list
