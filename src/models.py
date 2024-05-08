import sqlite3

class Model:
    _connection = sqlite3.connect('data/bank.db')

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
        '''returns username of current user
        '''
        return self.__username
    
    def check_password(self, password):
        '''returns True or False depending on provided password
        '''
        return self.__password == password
    
    def update_password(self, old_password, new_password):
        '''updates password
        '''
        if old_password == self.__password:
            self.__password = new_password
    
    def get_name(self):
        '''returns name of user
        '''
        return self.__name

    def set_name(self, new_name):
        '''sets the name of the user
        '''
        self.__name = new_name

    def get_surname(self):
        '''returns surname of user
        '''
        return self.__surname

    def set_surname(self, new_surname):
        '''sets the surname of the user
        '''
        self.__surname = new_surname

    def get_accNum(self):
        '''returns the user accounut number
        '''
        return self.__accNum

    def set_accNum(self, new_accNum):
        '''sets the user account number
        '''
        self.__accNum = new_accNum

    def save(self):
        '''saves user details into the database
        '''
        query = "INSERT INTO users (username, password, name, surname) VALUES ('{}', '{}', '{}', '{}')".format(self.__username,
                                                                                                               self.__password,
                                                                                                               self.__name,
                                                                                                               self.__surname)
        self._connection.execute(query)
        self._connection.commit()

    def update(self, **values):
        '''updates user details
        '''
        query = "UPDATE Users SET "
        for key, value in values.items():
            if key not in vars(self).keys():
                print(f"{key} is not an attribute of User!")
                return
            query += f"{key} = '{value}',"
        query = query.strip(",")
        query += f" WHERE username = '{self.__username}'"
        self._connection.execute(query)
        self._connection.commit()
    
    @staticmethod
    def get_user(username):
        '''returns user entity'''
        cursor = User._connection.execute("Select * from Users WHERE username = '{}'"
                                            .format(username))
        user_data = list(cursor)
        if user_data:
            user_data = user_data[0]
            user = User(user_data[0], user_data[1])
            user.set_name(user_data[2])
            user.set_surname(user_data[3])
            user.set_accNum(user_data[4])
            return user
        print("User does not exist!")
        return None
    
    @staticmethod
    def usernames():
        '''method to return all users of bank
        '''
        cursor = User._connection.execute("SELECT username FROM Users;")
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
    def __init__(self, user, amount, accNum) -> None:
        self.user = user
        self.amount = amount
        self.accNum = accNum

    def get_user(self):
        return self.user

    def get_amount(self):
        return self.amount

    # def set_amount(self, amount):
    #     self.amount += amount

    def get_accNum(self):
        return self.accNum

    @staticmethod
    def get_transactions():
        cursor = Account._connection.execute("Select * from Transactions")
        transactions = []
        for post in cursor:
            transactions.append(Account(post[0], post[1], post[2]))
        return transactions

    def save(self, deposit=False, withdraw=False):
        # deposit
        if deposit:
            # pull user account balance from db
            cursor = Account._connection.execute("")
        if withdraw:
            pass

        # 
        query = f"INSERT INTO Transactions VALUES ('{self.user}', '{self.amount}', '{self.accNum}')"
        self._connection.execute(query)
        self._connection.commit()

    def __str__(self):
        return f"{self.user} sent £{self.amount} -> {self.accNum}"