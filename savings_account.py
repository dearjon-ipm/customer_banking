from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance."""
    # Create an instance of the Account class
    savings_account = Account(balance, 0)
    # Calculate interest earned
    interest_earned = balance * (interest_rate * months / 12)
    # Update the savings account balance
    updated_balance = balance + interest_earned
    # Update the instance with the new values
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    return updated_balance, interest_earned