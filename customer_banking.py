# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Define an inner function to get user input
    def get_input(account_type):
        """
        Prompts the user to enter balance, interest rate, and months for an account.

        Args:
            account_type (str): Type of account (Savings or CD).

        Returns:
            tuple: (balance, interest_rate, months) entered by the user.
        """
        while True:
            try:
                print(f"\n--- {account_type} Account Details ---")
                # Prompt for account balance
                balance = float(input(f"Enter the {account_type.lower()} account balance: $"))
                if balance < 0:
                    raise ValueError("Balance cannot be negative.")

                # Prompt for interest rate (as a percentage, e.g., 5 for 5%)
                interest_rate = float(input(f"Enter the annual interest rate for the {account_type.lower()} account (as a percentage): "))
                if interest_rate < 0:
                    raise ValueError("Interest rate cannot be negative.")

                # Convert percentage to decimal
                interest_rate /= 100

                # Prompt for the duration in months
                months = int(input(f"Enter the number of months for the {account_type.lower()} account: "))
                if months <= 0:
                    raise ValueError("Months must be a positive integer.")

                return balance, interest_rate, months
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.\n")

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance, savings_interest, savings_maturity = get_input("Savings")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("\n--- Savings Account Summary ---")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance, cd_interest, cd_maturity = get_input("CD")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("\n--- CD Account Summary ---")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()