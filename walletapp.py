

class BankAccount:
    starting_rn = 1_000
    def __init__(self, funds=10_000, trusted_users = []):

        self.funds = funds
        BankAccount.starting_rn += 1
        self.routing_number = BankAccount.starting_rn
        self.trustedUsers = trusted_users



    def check_balance(self):
        print(self.funds)
        print(self.routing_number)



    def withdraw(self, amount):
        if self.funds - amount >= 0:
            self.funds = self.funds - amount
            print(self.funds)
            return amount
        else:
            print("Error: can't withdraw that amount")

    def deposit(self, amount):
        self.funds = self.funds + amount
        print(self.funds)

    def transfer_to(self, account_2, amount):
        if self.funds - amount >= 0:
            self.funds = self.funds - amount
            account_2.deposit(amount)
            print("Process complete")
        else:
            print("Error: can't transfer that amount")





class UserAccount:
    user_emails = []

    def __init__(self, first_name, last_name, age, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password

    @staticmethod
    def signup(first_name, last_name, age, email, password):
        listerrors = 0
        if len(password) < 10:
            print("Error: less than 10 characters")
            listerrors += 1
        if age < 16:
            print("Error: age is less than 16")
            listerrors += 1
        if len(first_name) <= 0 or len(last_name) <= 0:
            print("Error: Invalid first or last name")
            listerrors += 1
        if UserAccount.user_emails.count(email) > 0:
            print("Error: email is already registered")
            listerrors += 1
        if len(email) <= 0:
            print("invalid email")
            listerrors += 1
        if listerrors == 0:
            UserAccount.user_emails.append(email)
            return UserAccount(first_name, last_name, age, email, password)




acc1 = BankAccount(100)


# acc1.withdraw(2000)
# acc1.deposit(5000)

acc2 = BankAccount(101)


acc1.transfer_to(acc2, 10_001)

# print(acc1.check_balance())
# print(acc2.check_balance())






blank = UserAccount.signup("Chris", "King", 18, "cskings14@gmail.com", "kfjnfd8737373")






