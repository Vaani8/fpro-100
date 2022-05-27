class atm:
    def __init__ (self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def checkBalance(self):
        print("YOUR BALANCE IS 1000 CRORE")
    def cashWithdrawl(self,amount):
        cash = 100000000000-amount
        print("YOU HAVE WITHDRAW "+amount+" . YOUR REMAINING BALANCE IS "+cash+" .")
def main():
    cardNumber=input("ENTER YOUR CARD NUMBER.....")
    pin=input("ENTER YOUR PIN NUMBER.....")
    vaani = atm(cardNumber,pin)
    activity=input("CHOOSE YOUR ACTIVITY ( 1.CHECK BALANCE OR 2.WITHDRAWL )....")
    if(activity == 1):
        vaani.checkBalance()
    elif(activity == 2):
        amount= input("ENTER YOUR WITHDRAWL AMOUNT.....")
        vaani.cashWithdrawl(amount)
    else:
        print("ENTER VALID NUMBER !!!")
if __name__ =="__main__":