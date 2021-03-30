#Composition is a subset of association
#One class is dependent on the other
#That is one cannot exist without the other

class salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
        return self.pay*12+self.bonus
class employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.Salary=salary(pay,bonus) #Passing salary object to class employee
    def total_salary(self):
        return self.Salary.annual_salary()

emp=employee("Dev",22,100000,100000)
print(emp.total_salary())
