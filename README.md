Banking Program
This is a simple command-line-based banking application written in Python. It allows users to perform basic operations like showing the account balance, making deposits, and withdrawing funds.

Features
View Balance: Check the current balance of your account.
Deposit: Add funds to your account.
Withdraw: Subtract funds from your account while ensuring sufficient balance.
Exit: Close the application safely.
How to Run
Ensure you have Python installed on your system (version 3.x recommended).
Download the main.py file from this repository.
Open a terminal or command prompt in the directory containing the file.
Run the program using the following command:
bash
Copy code
python main.py
Usage
Start the program.
Follow the on-screen menu to select an action:
Press 1 to view the current balance.
Press 2 to make a deposit.
Press 3 to withdraw funds.
Press 4 to exit the program.
Notes
Ensure the deposit amount is a positive number.
Withdrawals will fail if the entered amount exceeds the available balance or if it is less than 0.
The program uses a basic balance tracking system, and the balance resets upon restarting the program.
Future Improvements
Persist data using a database or file storage.
Add user authentication for secure access.
Enhance the user interface with a graphical interface.
Handle exceptions and edge cases more robustly.
