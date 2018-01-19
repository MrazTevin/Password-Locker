class User:
    """Will generate instances of user"""
    account_list = []
      """this is a class variable called account_list"""
    def __init__(self,first_name,last_name,email):
       """Passed in 4 arguements"""
       self.first_name = first_name
       self.last_name  = last_name
       self.email =email
