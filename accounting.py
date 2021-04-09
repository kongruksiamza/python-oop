from employee import Employee

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.__age = age
    
    def _showData(self):
        super()._showData()
        print("อายุ = "+str(self.__age))
        print("###############")
    
    def __str__(self):
        return (super().__str__()+" , อายุ = {} ปี".format(self.__age))