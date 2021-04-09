#Inheritance
class Employee:
    #class variable
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    def __init__(self,name,salary,department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self):
        pass

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self):
        pass



account = Accounting()
programmer = Programmer()
sale = Sale()
