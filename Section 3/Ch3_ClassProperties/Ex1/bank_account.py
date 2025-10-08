class BankAccount:
    # TODO: Add class variable interest_rate set to 0.02 (2%)
    interest_rate = 0.02
    
    def __init__(self, account_holder, balance):
        # TODO: Initialize instance variables:
        # - account_holder: the name of the account holder
        # - balance: the account balance
        self.name = account_holder
        self.balance = balance
        #pass
    
    def display_info(self):
        # TODO: Print account information in this exact format:
        # "Account: [account_holder]"
        # "Balance: $[balance]"
        # "Interest Rate: [interest_rate]%"
        # Don't forget to multiply interest_rate by 100 for percentage display
        # Add a blank line after the information
        print(f"Account: {self.name}")
        print(f"Balance: ${self.balance}")
        final_interest_rate = BankAccount.interest_rate * 100
        print(f"Interest Rate: {final_interest_rate}%")
        print()
        #pass