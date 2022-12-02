class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    @property # we can now access the pay
    def pay_amount(self):
        return self.pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount): # the class method is bound to the class
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day): # do not operate on instance or the class
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return f'{self.first} {self.last} works at Kingscompany.'


employees = [Employee('Christian', 'King', 50_000),
             Employee('Test', 'Employee', 60_000)]

employee2 = Employee('bruh', 'boy', 100_000)

Employee.set_raise_amt(1.05)

print(employees[0].pay_amount)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

print(employee2)

boob = None