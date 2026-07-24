# 🏦 Bank Management System (Python OOP)

A simple **Bank Management System** developed using **Python Object-Oriented Programming (OOP)** concepts. This project demonstrates the implementation of banking operations such as deposits, withdrawals, balance inquiry, transaction history, and different account types using inheritance.

---

## 📌 Features

- 💰 Deposit money with PIN verification
- 💸 Withdraw money with balance checking
- 🔒 Secure PIN authentication
- 📊 Check account balance
- 📝 View transaction history
- 🏦 Savings Account with interest calculation
- 🏛️ Current Account with interest calculation
- 📋 Menu-driven console application

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 📚 OOP Concepts Implemented

- Classes and Objects
- Constructors (`__init__`)
- Inheritance
- Method Overriding (Concept)
- Encapsulation
- Reusability

---

## 📂 Project Structure

```
BankManagementSystem/
│
├── bank.py          # Main Python source code
└── README.md        # Project documentation
```

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/BankManagementSystem.git
```

2. Navigate to the project folder

```bash
cd BankManagementSystem
```

3. Run the program

```bash
python bank.py
```

---

## 📋 Menu Options

```
------ Banking System ------

1. Deposit
2. Withdraw
3. Check Balance
4. Savings Account - Interest
5. Current Account - Interest
6. Transaction History
7. Exit
```

---

## 💡 Sample Output

```
------ Banking System ------

1.Deposit
2.Withdraw
3.Check Balance
4.SavingsAcc - Interest
5.CurrentAcc - Interest
6.Transaction History
7.Exit

Enter your Choice : 1
Enter the deposit amount : 500
Enter the PIN : 1234

Account Balance : 5500
```

---

## 🏗️ Class Diagram

```
                 BankAccount
                ----------------
                + accHolder
                + accBalance
                + pin
                + history
                ----------------
                + deposit()
                + withdraw()
                + show_balance()
                + transaction()

                     ▲
          ------------------------
          |                      |
          |                      |
   SavingsAcc             currentAcc
   ------------           ------------
   + savInterest()        + currInterest()
```

---

## ✨ Functionalities

### Deposit
- Verifies PIN
- Adds amount to account balance
- Stores transaction history

### Withdraw
- Verifies PIN
- Checks available balance
- Deducts amount
- Updates transaction history

### Balance Inquiry
Displays the current account balance.

### Transaction History
Shows all deposit and withdrawal transactions.

### Savings Account
Calculates and adds interest to the balance.

### Current Account
Calculates and adds interest to the balance.

---

## 🔮 Future Enhancements

- Multiple user login system
- Account number generation
- Transfer money between accounts
- Change PIN
- Delete account
- File handling for permanent data storage
- Database integration (MySQL/SQLite)
- GUI using Tkinter or PyQt
- Web application using Django

---

## 📖 Learning Outcomes

This project helps understand:

- Python Classes and Objects
- Constructors
- Inheritance
- Encapsulation
- Menu-driven programming
- Lists for transaction management
- Conditional statements
- User input handling

---

## 👨‍💻 Author

**Febin K S**
- MCA Graduate
- Passionate about Python, Django, and Software Development

---

## 📄 License

This project is developed for educational and learning purposes. Feel free to use, modify, and improve it.
