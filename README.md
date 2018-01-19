
# Password Locker

This app generates and stores passwords for various accounts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Running the tests

Create a new account including your username and password.
Log In to your account if you have a password already.
Check your login details if they do exist.
Save any website you recently signed up with it's password.
Try to delete any of your user details.

###  end to end tests


  - Will save your newly generated user and account details into the user_list and account_list respectively.
test_save_multiple_user, test_save_multiple_account :
  - Checks whether assorted individuals using the app can save their details.
test_delete_user, test_delete_account :
  - Forsees whether credentials and user information can be deleted.
test_find_by_website
  - This test simplifies work of looking for your numerous details.


```
Given that the app is able to : 1. Store account details.
                                2. Generate random passwords.
                                3. Authenticate users to account.
  when the user logs in,
  Then : 1. He/She should be able to create an account.
         2. LogIn with the provided password.
         3. Save his/her login details.
         4. Retrieve Login details with ease.

```


## Built With

* [Python](https://docs.python.org/3/) - The language used.



## Authors

* **MIlla Tevin**



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Moringa School.
* Stack Exchange Community that helped me to debug my errors.
