#ฟังก์ชั่นเสริม
class Employee:
    minSalary = 12000
    maxSalary = 50000
    _companyName = "บริษัท XYZ จำกัด"
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))
    
    def _getIncome(self):
        return self.salary * 12
    
    def __str__(self):
        return ("ชื่อพนักงาน = {} , เงินเดือน = {} , ตำแหน่ง = {}".format(self.name,self.salary,self.department))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary):
         super().__init__(name,salary,self.__departmentName)

class Programmer(Employee):
    __departmentName = "โปรแกรมเมอร์"
    def __init__(self,name,salary,experience):
         super().__init__(name,salary,self.__departmentName)
         self.exp = experience
    
    def __str__(self):
        return (super().__str__()+" , ประสบการณ์ทำงาน = {} ปี".format(self.exp))


programmer = Programmer("ก้อง",15000,2)
print(programmer.__str__())
print("รายได้ต่อปี = {}".format(programmer._getIncome()))