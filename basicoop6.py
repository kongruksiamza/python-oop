#Encapsulation
class Employee:
    def __init__(self,name,salary,department):
        #private attribute
        self._name = name #protected
        self.__salary = salary
        self.__department = department
        self.__showData()

        #private method
    def __showData(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))

obj1 = Employee("ก้อง",20000,"บัญชี")
obj1._name = "โจโจ้"
obj1.__salary = 40000
obj1.__department = "ฝ่ายขาย"
