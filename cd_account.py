from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance."""
    # Create an instance of the Account class
    cd_account = Account(balance, 0)
    # Calculate interest earned (months taken into account)
    cd_account_interest_earned = balance * (interest_rate / 12) * months
    # Update the CD account balance by adding the interest earned
    updated_balance = balance + cd_account_interest_earned
    # Update the instance with the new values
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(cd_account_interest_earned)
    return updated_balance, cd_account_interest_earned