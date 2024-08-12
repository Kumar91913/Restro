user={'pin': 1234,'balance': 5000}
print("Welcome to SandeepCorporationBank ATM")
pin=int(input("please enter your four digit pin: "))
def withdraw_cash():
    while True:
        amount = int(input("Enter the amount of money you want to widthdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} successfully widthdrawn your remaining balance is {user['balance']}")
            print('')
        return False
        
def balance_enquiry():
        print(f"Total balance {user['balance']}")
        print('')
if pin==user['pin']:

    print("What do yo want to do")
    print(" Enter 1 to Widthdrawcash \n Enter 2 for Balance Enquiry \n Enter 3 to Quit")
    query=int(input("Enter the number corresponding to the activity you want to do"))
    if query == 1:
        withdraw_cash();
    elif query == 2:
        balance_enquiry();
    else:
        print("please enter correct value shown")

else:
    print("Entered wrong pin")




        
    
            
