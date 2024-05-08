from utils import draw_line, intro, success, fail

def welcome():
    print(intro())


def login_menu():
    while True:
        user_input = input("""Please choose an option below: 
        [1] Login
        [2] Create New User
        [0] Quit
        Enter Choice: """)
        if user_input in ["0", "1", "2"]:
            return user_input


def get_user_details(register=False):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if register:
        password_conf = input("Please confirm your password: ")
        return (username, password, password_conf)
    return (username, password)

def get_deposit_info():
    while True:
        amount = int(input("Deposit amount (max £50):\n£"))
        if amount < 51:
            return amount

def get_withdrawal_info():
    while True:
        amount = int(input("Withdrawal amount (max £50):\n£"))
        if amount < 51:
            return amount
        
def display_result(result):
    if result:
        success()
    else:
        fail()

def main_menu(user):
    menu = f"Welcome {user.get_name()}\n"
    menu += "Please select a service below:\n\n"
    menu += "[1] Deposit\n"
    menu += "[2] Withdraw\n"
    menu += "[3] Check Balance\n"
    menu += "[0] Quit\n:"
    return menu