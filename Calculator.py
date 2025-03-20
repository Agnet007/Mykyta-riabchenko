from Bank import Bank
class Calculator():
  
  def _bankSize(self, bank: Bank):
     bankSize = sum(bank.getCountOfMoney(n) * n for n in bank.getNominals() if isinstance(n, int))
     return bankSize
  
  def exchangeMoney(self, inputedMoney: list, bank: Bank):
    nominalList = [100, 50, 20, 10, 5, 2, 1]
    changedMoney = []
    inputedSum = sum(inputedMoney)

    #if given sum is larger then amount of money in the bank: return -1
    if inputedSum > self._bankSize(bank):
      return -1             
    startPoint = 0

    #if given money is a nominal the prog has to braek it into smaller pieces
    if inputedSum in nominalList:     
      startPoint = nominalList.index(inputedSum) + 1

    #goes through nominals, exchanges money in it untill the nominal is larger then 
    #the whole sum, then switch to smaller nominal
    for i in nominalList[startPoint:]:
      while  i <= inputedSum and bank.getCountOfMoney(i) != 0:
        changedMoney.append(i) 
        inputedSum -= i
        bank.withdrawMoney(i)
    return changedMoney
 

     #TODO:if the amount of needed coins is not enought the prog's ignoring it
          #example bank[1, 5, 5, 10] givenList[1, 1, 5, 10]



    if inputedSum is nominalList:
      startPoint = nominalList.index(inputedSum) + 1
      
