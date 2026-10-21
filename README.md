# 🏧 ATM Withdrawal System in Python

## 📌 Project Description

The **ATM Withdrawal System** is a simple Python project that simulates an ATM cash withdrawal process. It allows users to enter their account balance and withdrawal amount, validates the input, checks the available balance, and ensures that a minimum balance of ₹500 is maintained after withdrawal.

This project is designed to practice Python fundamentals such as conditional statements, exception handling, and user input validation.

## ✨ Features

- 💰 Accepts the user's account balance.
- 💵 Takes the withdrawal amount as input.
- ✅ Validates account balance and withdrawal amount.
- 🚫 Prevents withdrawals when the balance is insufficient.
- 🏦 Maintains a minimum balance of ₹500.
- 📊 Displays a transaction report after successful withdrawal.
- ⚠️ Handles invalid numeric inputs using `try-except`.
- 🔚 Uses a `finally` block to display the transaction completion message.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** `if-elif-else`, `try-except-finally`, user input, arithmetic operations, and conditional validation.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/safamariyam1902-tech/ATM-Withdrawal-System.git
```

### 2. Navigate to the Project Folder

```bash
cd ATM-Withdrawal-System
```

### 3. Run the Python Program

```bash
python atm.py
```

Replace `atm.py` with your actual Python filename if it is different.

## 💻 Example Output

```text
Enter Account Balance: 5000
Enter withdrawal amount: 1000

Status: Withdrawal successful!
----------- ATM Transaction Report -----------
Previous Balance  : 5000
Withdrawal Amount : 1000
Remaining Balance: 4000
ATM transaction completed successfully.
ATM transaction process ended.
```

## 📋 Validation Rules

1. The account balance must be greater than zero.
2. The withdrawal amount must be greater than zero.
3. The withdrawal amount cannot exceed the available balance.
4. A minimum balance of ₹500 must remain after withdrawal.
5. Invalid numeric inputs display an error message.

## 📚 Learning Objectives

Through this project, I practiced:

- Using conditional statements to make decisions.
- Handling invalid inputs with exception handling.
- Performing arithmetic calculations.
- Implementing basic banking transaction rules.
- Generating a simple ATM transaction report.

## 🔮 Future Improvements

- Add a PIN authentication system.
- Support multiple transactions.
- Add deposit and balance inquiry options.
- Store transaction history.
- Create a menu-driven ATM interface.

## 👩‍💻 Author

Created as a Python practice project to improve programming and problem-solving skills.

---

⭐ If you find this project useful, consider giving the repository a star!
