class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self): # this overrides the log method into making it print the following
        print("I'm a teacher!")

class Customer(User):
    def __init__(self, name, mem_type):  # we are going to make name a property
        self.name = name
        self.mem_type = mem_type

    @property
    def name(self):
        print('getting name')
        return self._name  # this is private. You can't touch it outside the class

    @name.setter
    def name(self, name):
        print('setting name')
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def update_mem(self, new_mem):
        print('Calculation costs')
        self.mem_type = new_mem

    def read_customer():  # u want this to be to any person (static method: invoked on the class)
        print('Reading customer from database...')

    def __str__(self):  # any time we want to covert to string and not read the data location
        return self.name + " " + self.mem_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):  # will compare if two customers are equal
        if self.name == other.name and self.mem_type == other.mem_type:
            return True
        return False  # if this was here, it would see if the memory locations are equal

    __hash__ = None

    __repr__ = __str__  # instead of saying the location, it just makes a list of the customers


users = [Customer('Caleb', 'Gold'),
             Customer('Caleb', 'Gold'),
             Teacher()]

# Customer.read_customer()
#
# print(customers[0])
#
# Customer.print_all_customers(customers)
#
# print(customers[0] == customers[1])
#
# print(customers)
#
# customers[0].log()

for user in users:
    user.log()





