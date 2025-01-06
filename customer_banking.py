from cd_account import create_cd_account
from savings_account import create_savings_account

def main():
    """Main function to calculate and display savings and CD account details."""
    def get_input(account_type):
        """Prompts the user for account details."""
        while True:
            try:
                print(f"\n--- {account_type} Account Details ---")
                balance = float(input(f"Enter the {account_type.lower()} account balance: $"))
                if balance < 0:
                    raise ValueError("Balance cannot be negative.")
                interest_rate = float(input(f"Enter the annual interest rate for the {account_type.lower()} account (as a percentage): "))
                if interest_rate < 0:
                    raise ValueError("Interest rate cannot be negative.")
                interest_rate /= 100
                months = int(input(f"Enter the number of months for the {account_type.lower()} account: "))
                if months <= 0:
                    raise ValueError("Months must be a positive integer.")
                return balance, interest_rate, months
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.\n")

    # Savings account details
    savings_balance, savings_interest, savings_maturity = get_input("Savings")
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )
    print("\n--- Savings Account Summary ---")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    # CD account details
    cd_balance, cd_interest, cd_maturity = get_input("CD")
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )
    print("\n--- CD Account Summary ---")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()