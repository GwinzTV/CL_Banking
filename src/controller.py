from hashlib import sha1
from views import welcome, login_menu, main_menu, get_user_details, get_deposit_info, get_withdrawal_info, display_result
from models import Account, User

class Controller:

    def __init__(self):
        self.__current_user = None

    def start(self):
        welcome()
        while self.__current_user is None:
            user_option = login_menu()
            if user_option == "1":
                self.__login()
            elif user_option == "2":
                self.__create_user()
            elif user_option == "0":
                break
        while self.__current_user:
            self.__main_menu()

    def __login(self):
        username, password = get_user_details()
        user = User.get_user(username)
        if user and user.check_password(sha1(password.encode("utf-8")).hexdigest()):
            self.__current_user = user

    def __create_user(self):
        while True:
            username, password, password_conf = get_user_details(register=True)
            if username in User.usernames():
                print("Username taken!")
                continue
            if password == password_conf:
                break
            print("Passwords don't match. Please Try again.")

        new_user = User(username, sha1(password.encode(encoding="utf-8")).hexdigest())
        new_user.set_name(username)
        new_user.save()
        self.__current_user = new_user
        user_id = new_user.get_user_id(username)
        # creates a new account with opening balance of £1000
        new_account = Account(user_id, 1000)
        new_account.save()
    
    def __main_menu(self):
        option = input(main_menu(self.__current_user))
        if option == "1":
            self.__deposit()
        elif option == "2":
            self.__withdraw() # need implementing
        elif option == "3":
            self.__check_balance() # need implementing
        elif option == "0":
            exit()

    def __deposit(self):
        amount = get_deposit_info()
        username = self.__current_user.get_username()
        new_deposit = Account(self.__current_user.get_user_id(username), amount)
        new_deposit.set_deposit()
        result = new_deposit.save()
        display_result(result)

    def __withdraw(self):
        pass

    def __check_balance(self):
        pass
