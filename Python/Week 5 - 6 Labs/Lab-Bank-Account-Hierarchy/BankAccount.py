from datetime import datetime
class BankAccount:
    def __init__(self, acct_ID, acct_holder, balance):
        self._acct_Id = acct_ID
        self._acct_holder = acct_holder
        self._date_opened = datetime.now()
        self._balance = balance
        
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
            print(f'Value {new_bal} invalid for balance field; no change made')
        else:
            self._balance = new_bal
            
    def make_deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
        else:
            print(f'Value {deposit_amount} invalid for deposit amount; no change made')
            
    def make_withdrawal(self, withdrawal_amount):
        if withdrawal_amount > 0 and self.balance - withdrawal_amount > 0:
            self.balance -= withdrawal_amount
        else:
            print(f'Value {withdrawal_amount} invalid for withdrawal amount; no change made')
            
    def transfer_funds(self, transfer_amount, another_account):
        if self._acct_holder == another_account._acct_holder:
            if self.balance - transfer_amount > 0:
                self.make_withdrawal(transfer_amount)
                another_account.make_deposit(transfer_amount)
            else:
                print(f'Insufficient funds in account with ID {self._acct_Id}')
                print(f'Required: {transfer_amount}: Available: {self.balance}.')
        else:
            print("Account holders not the same")
            
    def print_acct_info(self):
        print(f'{"*" * 50}\nAccount info for account ID: {self._acct_Id}')
        print(f'Holder: {self._acct_holder}\tDate opened: {self._date_opened}\tBalance: {self.balance:,}\n{"*" * 50}')
            
            