from bank.account import show_balance
from bank.app.calculator import deposit
from bank.fees import apply_fee


balance = 1000

print(show_balance(balance))


balance = deposit(balance, 500)
print(show_balance(balance))


balance = apply_fee(balance, 50)
print(show_balance(balance))

'''

tozih:

    
dar 'git bash' dar folder 'bank_project' dastore 

'python -m bank.app.main'
 
ra eja mikonim



khorooji : 


Zagros@DESKTOP-7NVT4GM MINGW64 ~/Desktop/تکالیف جلسه هفتم (master)
$ ls
Q7.1.py  Q7.2.py  Q7.3.py  Q7.4.py  bank_project/  

Zagros@DESKTOP-7NVT4GM MINGW64 ~/Desktop/تکالیف جلسه هفتم (master)
$ cd bank_project/

Zagros@DESKTOP-7NVT4GM MINGW64 ~/Desktop/تکالیف جلسه هفتم/bank_project (master)
$ python -m bank.app.main
100000
150000
145000




'''



