class Atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number= card_number
        self.pin_number= pin_number
    def cashWithdrawl(self,amount):
        print("You have withdrawn ",amount)
    def checkBalance(self):
        print("your balance is $10,000")

def main():
    card_number=input("Enter your card number:")
    pin_number=input("Enter your pin number:")
    user = Atm(card_number,pin_number)
    print("Choose your activity\n1.check balance\n2.Cash Withdrawl")
    activity = int(input("Enter your activity"))
    if(activity ==1):
        user.checkBalance()
    else:
        amount = int(input("enter the amount"))
        user.cashWithdrawl(amount)
main()