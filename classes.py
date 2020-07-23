class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def display(self):
        print("name: " + self.first + " " + self.last)
        print("pay: " + str(self.pay))
        print("email: " + self.email)


bob = Employee("Bob", "Smith", 75000)
bob.display()
