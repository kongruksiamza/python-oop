from employee import Employee

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        print("###############")
    
    def __str__(self):
        return (super().__str__()+" , ประสบการณ์ = {} ปี, ทักษะ = {}".format(self.__exp,self.__skill))