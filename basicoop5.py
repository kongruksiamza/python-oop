#ฟังก์ชั่นเสริม
class Employee:

    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

#การสร้างวัตถุ
obj1 = Employee("ก้อง",20000,"บัญชี")
obj2 = Employee("โจโจ้",40000,"โปรแกรมเมอร์")
obj3 = Employee("นัท",100000,"ผู้จัดการ")

print(obj1.__class__)