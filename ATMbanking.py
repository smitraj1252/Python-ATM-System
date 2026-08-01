accounts=[]
ACC_Count=int(input("Enter how many account you want to add:"))
for i in range(ACC_Count):
    Name=input(f"Enter your {i+1} account name:")
    Account_no=int(input("Enter your Account number:"))
    PIN=int(input("Enter your pin number:"))
    BALANCE=int(input("Enter your Balance:"))

    Account_data={
    "NAME":Name,
    "Account_no":Account_no,
    "PIN":PIN,
    "BALANCE":BALANCE
}
    accounts.append(Account_data)
print("Account Details is:",accounts)

###LOGIN SYSTEM
print("\n====LOGIN SYSTEM====")
Login_Account_no=int(input("Enter your Account number:"))   
PIN=int(input("Enter your pin number:"))

login = False
current_account = None
for account in accounts:
    if account["Account_no"] == Login_Account_no and account["PIN"] == PIN:
        print("Login Successful")
        login = True
        current_account = account   
        break

if not login:
    print("Login Failed")
    exit()
####ADDING MENU
print("\n====ATM BANKING MENU====")
print("1.CHECK BALANCE")
print("2.DEPOSIT MONEY")
print("3.WITHDRAW MONEY")
print("4.LOGOUT")
print("=================================")

while True:
    choice=int(input("Enter your choice:"))
    if choice == 1:
        print("Your Account Balance is:",current_account["BALANCE"])

    elif choice == 2:
            Deposit=int(input("Enter Amount you want to Deposit:"))
            if Deposit<=0:
                print("INVALID AMOUNT")
            else:
                current_account["BALANCE"]+=Deposit
                print("Deposit Successful")
                print("Your Final Balance is:",current_account["BALANCE"])

    elif choice == 3:
            Withrawal=int(input("Enter Amount you want to Withdraw:"))
            if Withrawal<=0:
                print("INVALID AMOUNT")
            elif Withrawal>current_account["BALANCE"]:
                 print("INSUFFICIENT BALANCE")
            else:
                current_account["BALANCE"]-=Withrawal
                print("withdrawal Successful")
                print("Your Final Balance is:",current_account["BALANCE"])

    elif choice ==4:
             print("LOGOUT SUCCESSFUL")
             print("THANK YOU FOR USING ATM BANKING")
             break
 
    else:
         print("PLEASE ENTER VALID CHOICE:")