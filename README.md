
# Banking System in Python

This project implements a basic banking system in Python, allowing a user to perform the following operations:
- **Deposit**: Allows the user to deposit a positive amount of money into their account.
- **Withdrawal**: Limits the user to 3 daily withdrawals, with a maximum amount of R$500 per transaction. If the user has insufficient funds, the withdrawal will not be allowed.
- **Statement**: Displays the user’s transaction history (deposits and withdrawals) along with the current balance.

## Project Details
- This is the first version of the banking system, and it works with only one user.
- No identification (like agency or account number) is required, as all transactions are associated with the single user.
- Deposits and withdrawals are stored and displayed when the user requests a statement.

## System Operations
1. **Depositing**: Enter the amount to be deposited. The amount must be greater than 0.
2. **Withdrawing**: Enter the amount to withdraw. The system will check if the user has enough balance and if the amount is within the daily limit.
3. **Statement**: View the list of transactions and the current balance.

## Running the Project
To run the system, you need to have Python installed on your machine. Clone this repository, navigate to the project directory, and run the script:

```bash
python Challenge-DIO-01-Bank-System-in-Python.py
```

## Technologies Used
- **Python**: The system was built using basic Python programming, focusing on flow control, user input, and variable manipulation.

## Future Enhancements
- Implementing multiple users with unique accounts.
- Adding authentication (PIN or password).
- Including interest calculation for savings accounts.
- Allowing transfers between accounts.

---

This project is designed to practice basic Python concepts and simulate a simple banking system. Future versions will add more complexity and functionality.
