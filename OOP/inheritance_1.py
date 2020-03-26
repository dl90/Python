class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return self.pay * 12 + self.bonus

class Employee:
    # def __init__(self, name, age, pay, bonus):
    def __init__(self, name, age, salary_obj):
        self.name = name
        self.age = age
        # composition => Employee is a container class (contains Salary)
        self.salary = salary_obj

    def total_salary(self):
        return self.salary.annual_salary()

# interface to check if Salary object is Salary object
class checkSalary:
    def __init__(self, obj):
        if obj.pay and obj.bonus:
            self.obj = obj
    def get_pay(self):
        if self.obj:
            return self.obj

sal = Salary(10, 1000)
pay = checkSalary(sal).get_pay()
emp1 = Employee("Test1", 10, pay)
print(emp1.total_salary())

# --- DUCK TYPING ---
# interface IDUCK:
#     quack
#     fly
class Duck: # IDUCK
    def quack(self):
        print("quack")
    def fly(self):
        print("flap")
class Person: # IDUCK
    def quack(self):
        print("Quack?")
    def fly(self):
        print("Ill try I guess...")

def test(obj):
    obj.quack()
    obj.fly()

# test(Duck())
# test(Person())
# --- DUCK TYPING ---