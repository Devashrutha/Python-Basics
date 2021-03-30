#Aggregation is a subset of association
#One class is independent of the other
#That is one can exist without the other
#Unidirectional only (House--->Desk)

class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
        return (self.pay*12)+self.bonus

class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def total_salary(self):
        return self.salary.annual_salary()
s=Salary(100000,100000)
e=employee('Dev',22,s)
print(e.total_salary())
