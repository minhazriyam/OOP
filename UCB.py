class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = int(input('''
                           
                           Hello! Welcome to UCB ATM.
                           1. Enter 1 to create PIN
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit 
'''))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.checkbalance()
        else:
            self.exit()
        
    def create_pin(self):
        self.pin = int(input("Enter your PIN= "))
        print("Pin Set Successful")
    def deposit(self):
        code = int(input("Enter the pin= "))
        if code == self.pin:
            depo = int(input("Enter the amount= "))
            self.balance = self.balance + depo
            print("Depostion Successful. Your Current Balance is {}".format(self.balance))
        else:
            print("Wrong Pin")
    def withdraw(self):
        code = int(input("Enter the pin= "))
        if code == self.pin:
            wd = int(input("Enter the amount= "))
            self.balance = self.balance - wd
            print("Withdraw Successful. Your Current Balance is {}".format(self.balance))
        else:
            print("Wrong Pin")
    def checkbalance(self):
        code = int(input("Enter the pin= "))
        if code == self.pin:
            print("Your Current Balance is {}".format(self.balance))
        else:
            print("Wrong Pin")
    def exit(self):
       print("Thank you for taking the service") 
        
  
        
        
        
        
        
        
        
        
        
        
        