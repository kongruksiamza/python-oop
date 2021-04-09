#Getter Setter Method
class Employee:
    def __init__(self,name,salary,department):
        #private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

        #private method
    def _showData(self):
        print("ชื่อพนักงาน = "+self.getName())
        print("เงินเดือน = ",format(self.getSalary()))
        print("ตำแหน่ง = "+self.getDepartment())

    # setter method
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary

    def setDepartment(self,department):
        self.__department = department

    #getter method
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department


obj1 = Employee("ก้อง",20000,"บัญชี")
print(obj1.getName())
