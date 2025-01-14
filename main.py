def show_balance():
  print(f"Your Balance is ${Balance: .2f}")

def deposit():
  amount = float(input("enter an amount to deposit: "))

  if amount < 0:
    print("thats not a valid amount")
    return 0
  else:
    return amount
def withdraw():
    amount = float(input("Enter amount to be withdrawn:"))
    if amount > Balance:
      print("insuffient funds")
      return 0
    elif amount < 0:
      print("amount must be greater than 0")
    else:
      return amount

Balance = 0
is_running = True

while is_running:
   print("Banking Program")
   print("1. Show Balance")
   print("2. Deposit")
   print("3. Withdraw")
   print("4. Exit")
  
   choice = input("Enter your choice: ")
  
   if choice == "1":
      show_balance()
   elif choice == "2":
      Balance += deposit()
   elif choice == "3":
      Balance -= withdraw()
   elif choice == "4":
     is_running = False
   else:
     print("That is not valid")

print("Thank you for using our banking program")







    
    






