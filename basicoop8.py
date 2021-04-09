#Class Variable
class Employee:
    #class variable
    __minSalary = 12000
    __maxSalary = 50000
    _companyName = "บริษัท XYZ จำกัด"
    def __init__(self,name,salary,department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

        #private method
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)


obj1 = Employee("ก้อง",20000,"บัญชี")
print(Employee._companyName)