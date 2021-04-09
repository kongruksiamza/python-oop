#การสร้าง class
class Employee:
    #สร้าง method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

#การสร้างวัตถุ
obj1 = Employee()
obj1.detail("ก้อง",50000,"บัญชี")
obj2 = Employee()
obj2.detail("โจโจ้",40000,"โปรแกรมเมอร์")
obj3 = Employee()
obj3.detail("นัท",100000,"ผู้จัดการ")

obj1.showData()
obj2.showData()