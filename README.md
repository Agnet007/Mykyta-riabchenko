This repository is for school project.

class's:
ATM, Bank, Calculator, Screen, Input, Controller, Output, InputSystem, Money
Money - _nominal
Bank - __bank = {}, addMoney(money), withdrawMoney(nominal), getCountOfMoney(nominal)
Calculator - getListOfMoney(inputedMoney : list) 
# method accepts a list of entered money and gives out exchange depending on the specified function
# Why a list? Because the answer can use the user's coins
Input - __buffer = [], pushInput(value)
IO:
Input money > 1 
(Input.pushInput(1)

Input command > 2 (2 - inputCoin)
Input money > 5
Input money > 5
Input money > 5
Input money > 5
Input money > 100 
Input money > 100
Input money > 100
Input money > All done ("All done" - 
You have insert 3.23$
Get in other nominal:
2$
1$
20¢
2¢
1¢
Thanks for using our service

Input money > 1
Input money > 2
Input money > 5
Input money > 5
Input money > 5
Input money > 5
Input money > 100
Input money > 100
Input money > 100
Input money > -1
We return you your money back.
Thanks for using our service

Input money > 






press button -> list.append(addOneToList())

ATM: 
 Visual, IO, Operatioanal part

 Visual:
  Window, menu, 


  import abc
class Bank():
  def __init__(self):
    self.__bank = {}
  def addMoney(self, money : int) -> None:
    if money not in self.__bank: 
      self.__bank[money] = 0
    self.__bank[money] += 1
  def withdrawMoney(self, nominal : int):
      if nominal in self.__bank:
        self.__bank[nominal] -= 1
  def getNominals(self):
    return list(self.__bank)
  def getCountOfMoney(self, nominal : int) -> int:
    if nominal in self.__bank:
      return self.__bank[nominal]
    return -1
  
class Calculator():
    def _bankSize(self, bank: Bank):
        bankSize = sum(bank.getCountOfMoney(n) * n for n in bank.getNominals() if isinstance(n, int))
        return bankSize

    def exchangeMoney(self, inputedMoney: list, bank: Bank):
        changedMoney = [10,10,10]
        inputedSum = sum(inputedMoney)

        #if given sum is larger then amount of money in the bank: return -1
        if inputedSum > self._bankSize(bank):
            return -1             
        
        return changedMoney

class UI():
    @abc.abstractmethod
    def listen(self): pass
    @abc.abstractmethod
    def addInputMethod(self, props, func): pass
    @abc.abstractmethod
    def show(self, props): pass
class ConsoleUI():
    def __init__(self):
       self.run = False
       self.commands = {}
    @abc.abstractmethod
    def listen(self):
        self.run = True
        while self.run:
            command = input("Input > ")
            if command in self.commands:
                self.commands[command]()
    @abc.abstractmethod
    def addInputMethod(self, props, func): pass
    @abc.abstractmethod
    def show(self, props): pass
bank = Bank()
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
calc = Calculator()
print(calc._bankSize(bank))
calc.exchangeMoney([5], bank)
calc.exchangeMoney([5], bank)
calc.exchangeMoney([5], bank)
print(bank.getNominals())
print(calc._bankSize(bank))
12

<!---
Mykyta-riabchenko/Mykyta-riabchenko is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
