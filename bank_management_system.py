import random

class BankUtility:
    """
    A utility class providing various helper methods related to banking operations.
    """

    @staticmethod
    def isNumeric(str):
        """
        Check if a string is numeric.

        :param str: The string to check.
        :return: True if the string is numeric, False otherwise.

        >>> BankUtility.isNumeric("1234")
        True
        >>> BankUtility.isNumeric("12.34")
        False
        >>> BankUtility.isNumeric("abcd")
        False
        >>> BankUtility.isNumeric("1234abcd")
        False
        >>> BankUtility.isNumeric("5678")
        True
        """
        return str.isdigit()

    @staticmethod
    def promptUserForString(prompt):
        """
        Prompt the user for a string input.

        :param prompt: The prompt message to display to the user.
        :return: The user's input as a string.
        """
        return input(prompt)

    @staticmethod
    def promptUserForPositiveNumber(prompt):
        """
        Prompt the user for a positive number input.

        :param prompt: The prompt message to display to the user.
        :return: The user's input as a positive float number.
        """
        while True:
            try:
                number = float(input(prompt))
                if number > 0:
                    return number
                else:
                    print("Amount must be positive. Try again.")
            except ValueError:
                print("Invalid input, please enter a number.")

    @staticmethod
    def convertFromDollarsToCents(dollars):
        """
        Convert an amount in dollars to cents.

        :param dollars: The amount in dollars.
        :return: The amount in cents.

        >>> BankUtility.convertFromDollarsToCents(2.57)
        257
        >>> BankUtility.convertFromDollarsToCents(0)
        0
        >>> BankUtility.convertFromDollarsToCents(1.23)
        123
        >>> BankUtility.convertFromDollarsToCents(100)
        10000
        >>> BankUtility.convertFromDollarsToCents(0.99)
        99
        >>> BankUtility.convertFromDollarsToCents(-2.57)  # Edge case: negative value
        -257
        >>> BankUtility.convertFromDollarsToCents(0.004)  # Edge case: value less than 1 cent
        0
        """
        return int(round(dollars * 100))

    @staticmethod
    def generateRandomInteger(min, max):
        """
        Generate a random integer between min and max, inclusive.

        :param min: The minimum value.
        :param max: The maximum value.
        :return: A random integer between min and max.

        >>> 1 <= BankUtility.generateRandomInteger(1, 10) <= 10
        True
        >>> 100 <= BankUtility.generateRandomInteger(100, 200) <= 200
        True
        >>> BankUtility.generateRandomInteger(0, 0) == 0  # Edge case: min and max are the same
        True
        >>> BankUtility.generateRandomInteger(-10, -1) <= -1  # Edge case: negative range
        True
        """
        return random.randint(min, max)

class CoinCollector:
    """
    A class that handles the parsing and conversion of various coin types into their respective values in cents.
    """

    @staticmethod
    def parseChange(coins):
        """
        Parse a string of coins and return the total value in cents.

        Valid coin types are:
        - 'P' for pennies (1 cent)
        - 'N' for nickels (5 cents)
        - 'D' for dimes (10 cents)
        - 'Q' for quarters (25 cents)
        - 'H' for half dollars (50 cents)
        - 'W' for dollar coins (100 cents)

        If an invalid coin type is provided, the method will print an error message and ignore that entry.

        :param coins: A string of coin types (e.g., 'QPDNNDXHW').
        :return: The total value of the coins in cents.

        >>> CoinCollector.parseChange("QPDNNDHW")
        206
        >>> CoinCollector.parseChange("QQQXXXWWP")
        Invalid coin: X
        Invalid coin: X
        Invalid coin: X
        276
        >>> CoinCollector.parseChange("QQQpnnDdhhww")
        406
        >>> CoinCollector.parseChange("")  # Edge case: empty string
        0
        >>> CoinCollector.parseChange("A1$%^")  # Edge case: invalid characters
        Invalid coin: A
        Invalid coin: 1
        Invalid coin: $
        Invalid coin: %
        Invalid coin: ^
        0
        """
        coin_values = {'P': 1, 'N': 5, 'D': 10, 'Q': 25, 'H': 50, 'W': 100}
        total_cents = 0
        for coin in coins.upper():
            if coin in coin_values:
                total_cents += coin_values[coin]
            else:
                print(f"Invalid coin: {coin}")
        return total_cents

class Account:
    """
    A class representing a bank account with functionalities to manage deposits, withdrawals, and other account-related operations.
    """

    ATM_WITHDRAWAL_FEE = 250  # A fixed fee in cents for ATM withdrawals.

    def __init__(self, firstName, lastName, ssn, accountNumber=None):
        """
        Initialize a new account with the given details. Generates a random account number and PIN if not provided.

        :param firstName: The first name of the account owner.
        :param lastName: The last name of the account owner.
        :param ssn: The Social Security Number of the account owner.
        :param accountNumber: Optional account number. If not provided, a random one is generated.
        """
        self.accountNumber = accountNumber if accountNumber else self.generate_account_number()
        self.ownerFirstName = firstName
        self.ownerLastName = lastName
        self.socialSecurityNumber = ssn
        self.PIN = self.generate_pin()
        self.balance = 0

    @staticmethod
    def generate_account_number():
        """
        Generate a random account number.

        :return: A randomly generated 8-digit account number.
        """
        return random.randint(10000000, 99999999)

    @staticmethod
    def generate_pin():
        """
        Generate a random 4-digit PIN.

        :return: A randomly generated 4-digit PIN as a string.
        """
        return f"{random.randint(0, 9999):04}"

    def getOwnerFirstName(self):
        """
        Get the first name of the account owner.

        :return: The first name of the account owner.
        """
        return self.ownerFirstName

    def setOwnerFirstName(self, firstName):
        """
        Set a new first name for the account owner.

        :param firstName: The new first name.
        """
        self.ownerFirstName = firstName

    def getOwnerLastName(self):
        """
        Get the last name of the account owner.

        :return: The last name of the account owner.
        """
        return self.ownerLastName

    def setOwnerLastName(self, lastName):
        """
        Set a new last name for the account owner.

        :param lastName: The new last name.
        """
        self.ownerLastName = lastName

    def getSocialSecurityNumber(self):
        """
        Get the Social Security Number of the account owner.

        :return: The Social Security Number of the account owner.
        """
        return self.socialSecurityNumber

    def setSocialSecurityNumber(self, ssn):
        """
        Set a new Social Security Number for the account owner.

        :param ssn: The new Social Security Number.
        """
        self.socialSecurityNumber = ssn

    def getPIN(self):
        """
        Get the PIN of the account.

        :return: The PIN of the account.
        """
        return self.PIN

    def setPIN(self, pin):
        """
        Set a new PIN for the account.

        :param pin: The new PIN.
        """
        self.PIN = pin

    def getBalance(self):
        """
        Get the current balance of the account.

        :return: The current balance in cents.
        """
        return self.balance

    def setBalance(self, balance):
        """
        Set a new balance for the account.

        :param balance: The new balance in cents.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        :param amount: The amount to deposit in cents.
        :return: The new balance after the deposit in cents.

        >>> account = Account("John", "Doe", "999123456", accountNumber=999123456)
        >>> account.deposit(500)
        500
        >>> account.deposit(-100)
        Deposit amount must be positive.
        500
        >>> account.deposit(1000)
        1500
        >>> account.deposit(0)
        Deposit amount must be positive.
        1500
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.

        :param amount: The amount to withdraw in cents.
        :return: The new balance after the withdrawal in cents.

        >>> account = Account("John", "Doe", "999123456", accountNumber=999123456)
        >>> account.deposit(1000)
        1000
        >>> account.withdraw(500)
        500
        >>> account.withdraw(600)
        Insufficient funds in account 999123456
        500
        >>> account.withdraw(-100)
        Withdrawal amount must be positive.
        500
        >>> account.withdraw(0)
        Withdrawal amount must be positive.
        500
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.balance
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print(f"Insufficient funds in account {self.accountNumber}")
            return self.balance

    def atmWithdraw(self, amount):
        """
        Withdraw a specified amount from the account via an ATM, including a fixed withdrawal fee.

        :param amount: The amount to withdraw in cents.
        :return: The new balance after the withdrawal in cents.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.balance
        
        total_amount = amount + self.ATM_WITHDRAWAL_FEE
        if self.balance < total_amount:
            print(f"Insufficient funds in account {self.accountNumber}")
            return self.balance
        
        return self.withdraw(total_amount)

    def isValidPIN(self, pin):
        """
        Compares the input PIN with the account's PIN and returns True if they match, False otherwise.

        :param pin: The PIN to compare.
        :return: True if the PIN matches, False otherwise.

        >>> account = Account("John", "Doe", "999123456", accountNumber=999123456)
        >>> account.isValidPIN(account.getPIN())
        True
        >>> account.isValidPIN("0000")
        False
        >>> account.isValidPIN("1234")
        False
        >>> account.isValidPIN(account.PIN)
        True
        >>> account.isValidPIN("")  # Edge case: empty string
        False
        >>> account.isValidPIN("abcd")  # Edge case: non-numeric PIN
        False
        """
        return self.PIN == pin

    def __str__(self):
        """
        Return a string representation of the account, masking the SSN except for the last 4 digits.

        :return: A string representing the account details.
        """
        masked_ssn = f"XXX-XX-{self.socialSecurityNumber[-4:]}"
        return (f"\nAccount Number: {self.accountNumber}\nOwner First Name: {self.ownerFirstName}\nOwner Last Name: {self.ownerLastName}\n"
                f"Owner SSN: {masked_ssn}\nPIN: {self.PIN}\nBalance: ${self.balance / 100:.2f}")

class Bank:
    """
    A class representing a bank that can hold and manage multiple accounts.
    """

    NUM_ACCOUNTS = 100  # The maximum number of accounts the bank can hold.

    def __init__(self):
        """
        Initialize a new bank with an array of accounts.
        """
        self.accounts = [None] * Bank.NUM_ACCOUNTS

    def addAccountToBank(self, account):
        """
        Add an account to the bank.

        :param account: The account to add.
        :return: True if the account was added, False otherwise.

        >>> bank = Bank()
        >>> account1 = Account("John", "Doe", "999123456")
        >>> bank.addAccountToBank(account1)
        True
        >>> account2 = Account("Jane", "Doe", "999123457")
        >>> bank.addAccountToBank(account2)
        True
        >>> len([acc for acc in bank.accounts if acc is not None])
        2
        >>> bank.addAccountToBank(account1)  # Edge case: adding the same account twice
        True
        >>> [acc for acc in bank.accounts if acc is not None].count(account1)  # Check if the same account is added twice
        2
        """
        for i in range(len(self.accounts)):
            if self.accounts[i] is None:
                self.accounts[i] = account
                return True
        print("No more accounts available.")
        return False

    def removeAccountFromBank(self, account):
        """
        Remove an account from the bank.

        :param account: The account to remove.

        >>> bank = Bank()
        >>> account = Account("John", "Doe", "999123456")
        >>> bank.addAccountToBank(account)
        True
        >>> bank.removeAccountFromBank(account)
        >>> bank.findAccount(account.accountNumber) is None
        True
        >>> bank.removeAccountFromBank(account)
        >>> bank.findAccount(account.accountNumber) is None
        True
        """
        for i in range(len(self.accounts)):
            if self.accounts[i] == account:
                self.accounts[i] = None

    def findAccount(self, accountNumber):
        """
        Find an account in the bank by account number.

        :param accountNumber: The account number to search for.
        :return: The account if found, None otherwise.

        >>> bank = Bank()
        >>> account = Account("John", "Doe", "999123456")
        >>> bank.addAccountToBank(account)
        True
        >>> found_account = bank.findAccount(account.accountNumber)
        >>> found_account.getOwnerFirstName()
        'John'
        >>> bank.findAccount(87654321) is None
        True
        >>> bank.findAccount(-1) is None  # Edge case: invalid account number
        True
        """
        for account in self.accounts:
            if account and account.accountNumber == accountNumber:
                return account
        return None

    def addMonthlyInterest(self, annualInterestRate):
        """
        Add monthly interest to all accounts in the bank.

        :param annualInterestRate: The annual interest rate as a decimal.

        >>> bank = Bank()
        >>> account1 = Account("John", "Doe", "999123456")
        >>> account2 = Account("Jane", "Doe", "999123457")
        >>> account1.deposit(10000)
        10000
        >>> account2.deposit(20000)
        20000
        >>> bank.addAccountToBank(account1)
        True
        >>> bank.addAccountToBank(account2)
        True
        >>> bank.addMonthlyInterest(1.25)
        >>> account1.getBalance()
        10010
        >>> account2.getBalance()
        20020
        """
        monthlyRate = annualInterestRate / 12 / 100
        for account in self.accounts:
            if account:
                interest = int(account.getBalance() * monthlyRate)
                account.deposit(interest)

class BankManager:
    """
    A class to manage the interaction between the user and the bank system.
    """

    def __init__(self):
        """
        Initialize the BankManager with a new Bank instance.
        """
        self.bank = Bank()

    def main(self):
        """
        The main method that provides a menu-driven interface for the user to interact with the bank system.
        """
        while True:
            print("============================================================")
            print("What do you want to do?")
            print("1. Open an account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. End Program")
            print("============================================================")

            choice = BankUtility.promptUserForString("Enter your choice: ")
            if choice == '11':
                break
            elif choice == '1':
                self.openAccount()
            elif choice == '2':
                self.getAccountInformation()
            elif choice == '3':
                self.changePIN()
            elif choice == '4':
                self.depositMoney()
            elif choice == '5':
                self.transferMoney()
            elif choice == '6':
                self.withdrawMoney()
            elif choice == '7':
                self.atmWithdrawal()
            elif choice == '8':
                self.depositChange()
            elif choice == '9':
                self.closeAccount()
            elif choice == '10':
                self.addMonthlyInterest()
            else:
                print("Invalid choice.")

    def promptForAccountNumberAndPIN(self, bank):
        """
        Prompt the user for an account number and PIN, and validate them.

        :param bank: The Bank instance to search for the account.
        :return: The account if the account number and PIN are valid, None otherwise.
        """
        while True:
            accountNumber = BankUtility.promptUserForString("Enter account number: ")
            if not BankUtility.isNumeric(accountNumber):
                print("Account number must be numeric. Please try again.")
                continue
            accountNumber = int(accountNumber)
            account = bank.findAccount(accountNumber)
            if not account:
                print(f"Account not found for account number: {accountNumber}.")
                return None
            pin = BankUtility.promptUserForString("Enter PIN: ")
            if not account.isValidPIN(pin):
                print("Invalid PIN.")
                return None
            return account

    def openAccount(self):
        """
        Handle the process of opening a new account, including prompting the user for necessary information.
        """
        firstName = BankUtility.promptUserForString("Enter Account Owner's First Name: ")
        lastName = BankUtility.promptUserForString("Enter Account Owner's Last Name: ")
        while True:
            ssn = BankUtility.promptUserForString("Enter Account Owner's SSN (9 digits): ")
            if len(ssn) == 9 and ssn.isdigit():
                break
            else:
                print("Social Security Number must be 9 digits. Please try again.")

        newAccount = Account(firstName, lastName, ssn)
        
        if not self.bank.addAccountToBank(newAccount):
            print("No more accounts can be added. Please try again later.")
            return
        
        print(newAccount)

    def getAccountInformation(self):
        """
        Retrieve and display the account information based on the user's input.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            print(account)

    def changePIN(self):
        """
        Allow the user to change the PIN for their account after validating the current PIN.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            while True:
                newPin = BankUtility.promptUserForString("Enter new PIN: ")
                if len(newPin) == 4 and newPin.isdigit():
                    confirmPin = BankUtility.promptUserForString("Enter new PIN again to confirm: ")
                    if newPin == confirmPin:
                        account.setPIN(newPin)
                        print("PIN updated.")
                        break
                    else:
                        print("PINs do not match. Please try again.")
                else:
                    print("PIN must be 4 digits. Please try again.")

    def depositMoney(self):
        """
        Handle the process of depositing money into an account.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            while True:
                amount = BankUtility.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
                cents = BankUtility.convertFromDollarsToCents(amount)
                if cents <= 0:
                    print("Deposit amount must be positive. Please try again.")
                else:
                    newBalance = account.deposit(cents)
                    print(f"New balance: ${newBalance / 100:.2f}")
                    break

    def transferMoney(self):
        """
        Handle the process of transferring money from one account to another.
        """
        fromAccount = self.promptForAccountNumberAndPIN(self.bank)
        if fromAccount:
            while True:
                toAccountNumber = BankUtility.promptUserForString("Enter account number to transfer to: ")
                if not BankUtility.isNumeric(toAccountNumber):
                    print("Account number must be numeric. Please try again.")
                    continue
                toAccountNumber = int(toAccountNumber)
                toAccount = self.bank.findAccount(toAccountNumber)
                if toAccount:
                    while True:
                        amount = BankUtility.promptUserForPositiveNumber("Enter amount to transfer in dollars and cents (e.g. 2.57): ")
                        cents = BankUtility.convertFromDollarsToCents(amount)
                        if cents <= 0:
                            print("Transfer amount must be positive. Please try again.")
                        else:
                            fromBalanceBefore = fromAccount.getBalance()
                            fromBalanceAfter = fromAccount.withdraw(cents)
                            if fromBalanceBefore == fromBalanceAfter:
                                # Already handled by withdraw method
                                break
                            else:
                                toBalance = toAccount.deposit(cents)
                                print(f"Transfer Complete\nNew balance in account {fromAccount.accountNumber} is: ${fromBalanceAfter / 100:.2f}\nNew balance in account {toAccount.accountNumber} is: ${toBalance / 100:.2f}")
                            break
                    break
                else:
                    print(f"Account not found for account number: {toAccountNumber}. Please try again.")

    def withdrawMoney(self):
        """
        Handle the process of withdrawing money from an account.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            while True:
                amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
                cents = BankUtility.convertFromDollarsToCents(amount)
                if cents <= 0:
                    print("Withdrawal amount must be positive. Please try again.")
                else:
                    balance_before = account.getBalance()
                    account.withdraw(cents)
                    if balance_before == account.getBalance():
                        # Insufficient funds, no need to print the new balance
                        break
                    else:
                        print(f"New balance: ${account.getBalance() / 100:.2f}")
                        break

    def atmWithdrawal(self):
        """
        Handle the process of withdrawing money from an account via an ATM.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            while True:
                amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): ")
                if amount < 5 or amount > 1000 or amount % 5 != 0:
                    print("Invalid amount. Try again.")
                else:
                    # Calculate the total amount in cents
                    amount_in_cents = BankUtility.convertFromDollarsToCents(amount)
                    total_amount_in_cents = amount_in_cents + account.ATM_WITHDRAWAL_FEE
                    
                    # Check if there's enough balance for the withdrawal
                    if account.getBalance() < total_amount_in_cents:
                        print(f"Insufficient funds in account {account.accountNumber}")
                        break

                    # Calculate the number of bills
                    num_20_bills = amount // 20
                    remainder = amount % 20
                    num_10_bills = remainder // 10
                    remainder = remainder % 10
                    num_5_bills = remainder // 5

                    # Perform the withdrawal
                    new_balance = account.withdraw(total_amount_in_cents)

                    # Output the details
                    print(f"Number of 20-dollar bills: {num_20_bills}")
                    print(f"Number of 10-dollar bills: {num_10_bills}")
                    print(f"Number of 5-dollar bills: {num_5_bills}")
                    print(f"New balance: ${new_balance / 100:.2f}")
                    break

    def depositChange(self):
        """
        Handle the process of depositing coin change into an account.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            coins = BankUtility.promptUserForString("Enter coin change to deposit (e.g. QPDNNDXHW): ")
            cents = CoinCollector.parseChange(coins)
            if cents > 0:
                newBalance = account.deposit(cents)
                print(f"${cents / 100:.2f} in coins deposited into account {account.accountNumber}")
                print(f"New balance: ${newBalance / 100:.2f}")
            else:
                print("No valid coins were entered.")

    def closeAccount(self):
        """
        Handle the process of closing an account after validating the user's credentials.
        """
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            self.bank.removeAccountFromBank(account)
            print(f"Account {account.accountNumber} closed.")

    def addMonthlyInterest(self):
        """
        Add monthly interest to all accounts in the bank based on an annual interest rate provided by the user.
        """
        annualRate = BankUtility.promptUserForPositiveNumber("Enter annual interest rate (e.g. 2.75): ")
        monthlyRate = annualRate / 12 / 100
        for account in self.bank.accounts:
            if account:
                interest = int(account.getBalance() * monthlyRate)
                account.deposit(interest)
                print(f"Deposited interest: ${interest / 100:.2f} into account number: {account.accountNumber}, new balance: ${account.getBalance() / 100:.2f}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    manager = BankManager()
    manager.main()