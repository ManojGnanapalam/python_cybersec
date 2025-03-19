class Employee:
    empCount = 0;

    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount +=1;

    def displayCount(self):
        print("Total Employee : ",Employee.empCount);

    def displayEmployee(self):
        print("Name :",self.name, ", Salary: ",self.salary)

class Loc(Employee):
    def __init__(self, name,salary,location):
        super().__init__(name,salary)
        print("location of employee",location)

empl1 = Loc("viper",22000,"chennai")

empl1.displayEmployee()
empl1.displayCount()
