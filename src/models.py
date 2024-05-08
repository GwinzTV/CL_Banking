import sqlite3

class Model:
    db = sqlite3.connect('../data/bank.db')
    cursor = db.cursor()

    def save(self):
        pass

    def update(self):
        pass


class User(Model):
    '''
    User model that inherits the Model class, for the use of its connection
    to the database.
    '''
    def __init__(self, username, password) -> None:
        '''initialising the users attributes
        '''
        self.__username = username
        self.__password = password
        self.__name = ""
        self.__surname = ""

    def get_username(self):
        return self.__username
    
    def check_password(self, password):
        return self.__password == password
    
    def update_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname
    
    def get_user_id(self, username):
        query = "SELECT user_id FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        id = self.cursor.fetchone()
        return id[0]

    def save(self):
        query = "INSERT INTO users (username, password, name, surname) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (self.__username, self.__password, self.__name, self.__surname))
        self.db.commit()

    @staticmethod
    def get_user(username):
        '''returns user entity'''
        cursor = User.db.execute("Select * from Users WHERE username = '{}'".format(username))
        user_data = list(cursor)
        if user_data:
            user_data = user_data[0]
            user = User(user_data[1], user_data[2])
            user.set_name(user_data[3])
            user.set_surname(user_data[4])
            return user
        print("User does not exist!")
        return None
    
    @staticmethod
    def usernames():
        '''method to return all users of bank
        '''
        cursor = User.db.execute("SELECT username FROM Users;")
        usernames = []
        for username in cursor:
            usernames.append(username[0])
        return usernames



class Admin(User):
    '''admin model that inherits from User model
    '''
    def __init__(self, username, password) -> None:
        super().__init__(username, password)

    

class Account(User):
    '''model for depositing money into user account
    '''
    def __init__(self, user_id, amount: int) -> None:
        self.user_id = user_id
        self.username = ""
        self.amount = amount
        self.balance = 0
        self.deposit = False
        self.withdraw = False

    def set_deposit(self):
        self.deposit = True

    def set_withdraw(self):
        self.withdraw = True

    def get_amount(self):
        return self.amount
    
    def get_balance(self):
        query = "SELECT balance FROM account WHERE user_id = ?"
        self.cursor.execute(query, (self.user_id,))
        balance = self.cursor.fetchone()
        return balance[0]
    
    def set_balance(self):
        self.balance = self.get_balance()
    
    def return_balance(self):
        self.set_balance()
        return self.balance

    def save(self):
        # deposit
        if self.deposit:
            query = "UPDATE account SET balance = balance + ? WHERE user_id = ?"
            self.cursor.execute(query, (self.amount, self.user_id))
            self.db.commit()
            return True
        if self.withdraw:
            self.set_balance()
            if self.amount < self.balance:
                query = "UPDATE account SET balance = balance - ? WHERE user_id = ?"
                self.cursor.execute(query, (self.amount, self.user_id))
                self.db.commit()
                return True
            return False
        else:
            query = "INSERT INTO account (user_id, username, balance) VALUES (?, ?, ?)"
            self.cursor.execute(query, (self.user_id, self.username, self.amount))
            self.db.commit()
            return True
