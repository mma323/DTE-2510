#Klassen Account, benyttes i atmmachine.py, testes her i main()

MONTHS_IN_YEAR = 12

class Account:
    def __init__(self, id=0, balance=100.00, annual_interest_rate=0):
        self.id = int(id)
        self.balance = float(balance)
        self.annual_interest_rate = float(annual_interest_rate) / 100  #Prosent

    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_annual_interest_rate(self, annual_interest_rate):
        self.annual_interest_rate = annual_interest_rate

    def get_annual_interest_rate(self):
        return self.annual_interest_rate

    def get_monthly_interest_rate(self):
        monthly_interest_rate = self.annual_interest_rate / MONTHS_IN_YEAR
        return monthly_interest_rate

    def get_monthly_interest(self):
        monthly_interest_rate = self.get_monthly_interest_rate()
        monthly_interest = monthly_interest_rate * self.balance
        return monthly_interest

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount


def main():
    account = Account(1122, 20000, 4.5)
    account.withdraw(2500)
    account.deposit(3000)

    print( account.id )
    print( account.balance )
    print( account.get_monthly_interest_rate() )
    print( account.get_monthly_interest() )

if __name__ == "__main__":
    main()