class Employee:
    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'
    
    def fullname (self):
        return '{} {}' .format(self.first, self.last)

emp_1 = Employee ('Nurlan', 'Mirzayev', 50000)
emp_2 = Employee ('Test', 'User', 60000)

# print (emp_1.first)
# print (emp_2.first)
# print (emp_1.fullname())
# print (emp_2.fullname())
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
# print ('{} {}' .format (emp_1.first, emp_1.last))