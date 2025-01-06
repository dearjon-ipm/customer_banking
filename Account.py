class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    def set_interest(self, interest):
        """Sets the interest gained for the account"""
        self.interest = interest