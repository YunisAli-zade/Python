def solution():
    from enum import Enum

    class TransactionType(Enum):
        DEPOSIT = "Deposit"
        WITHDRAW = "Withdraw"

    class BankAccount:
        def __init__(self, account_number: str):
            # Initialize attributes
            self._balance = 0.0
            self._transactions = []
            self._account_number = account_number
            self.account_type = "Basic"

        def _validate_amount(self, amount: float) -> bool:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            return True

        def deposit(self, amount: float) -> float:
            # Validate
            self._validate_amount(amount)
            # Update balance
            self._balance += amount
            # Record transaction
            self._transactions.append({"type": TransactionType.DEPOSIT, "amount": amount})
            # Return new balance
            return self._balance

        def withdraw(self, amount: float) -> float:
            # Validate
            self._validate_amount(amount)
            # Check funds
            if amount > self._balance:
                raise ValueError("Insufficient funds")
            # Update balance
            self._balance -= amount
            # Record transaction
            self._transactions.append({"type": TransactionType.WITHDRAW, "amount": amount})
            # Return new balance
            return self._balance

        def get_balance(self) -> float:
            return self._balance

        def get_transactions(self, transaction_type=None):
            if transaction_type is None:
                return self._transactions
            return [rec for rec in self._transactions if rec["type"] == transaction_type]

    class SavingsAccount(BankAccount):
        def __init__(self, account_number: str, interest_rate: float):
            super().__init__(account_number)
            self.__interest_rate = interest_rate
            self.account_type = "Savings"

        def apply_interest(self) -> float:
            interest = self.get_balance() * self.__interest_rate
            self._balance += interest
            return self._balance
            # Note: no transaction record for interest

        def withdraw(self, amount: float) -> float:
            self._validate_amount(amount)
            if self._balance - amount < 100:
                raise ValueError("Minimum balance of 100 must be maintained")
            self._balance -= amount
            self._transactions.append({"type": TransactionType.WITHDRAW, "amount": amount})
            return self._balance

    return (TransactionType, BankAccount, SavingsAccount)
