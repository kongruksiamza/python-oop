from accounting import Accounting
from programmer import Programmer
from sale import Sale


account = Accounting("ก้อง",10000,30)
print("บัญชี รายได้ต่อปี = "+str(account._getIncome(3000)))

programmer = Programmer("โจโจ้",40000,2,"พัฒนาเกม")
print("โปรแกรมเมอร์ รายได้ต่อปี = "+str(programmer._getIncome(10000,500)))

sale = Sale("นัท",35000,"เชียงใหม่")
print("ฝ่านขาย รายได้ต่อปี = "+str(sale._getIncome()))