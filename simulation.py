import getpass

def main():
    print("Welcome to the ATM Simulation!")

    
admin_users = {
        "username": "admin",
        "password": "adminpass",
        "balance": 1000.00,
        "role": "admin",
    }

users_db = []
users_db.append(admin_users)

def find_user_by_username(username):
    for user in users_db:
           if user["username"] == username:
               return user
           return None
    
def main_menu():
    print("\nMain Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. Update Profile")
    print("6. Logout")
    print("7. Exit ATM")
    choice = input("Select an option: ")

def create_user(users):
        print("\nCreate User:")
        username = input("Enter username: ")
        if find_user_by_username(username):
                print("Username already exists. Please try again.")
                return
        password = input("Enter password: ")  
        balance = validate_input("Enter initial balance: ", float)
        new_user = {
            "username": username,
            "password": password,
            "balance": balance,
            "role": "user",
        }
        users.db.append(new_user)
        print("User {username} created successfully.")

def deposit(current_user):
        print("\nDeposit:")
        amount = validate_input("Enter amount to deposit: ", float)
        if amount is None and amount > 0:
            current_user["balance"] += amount
            print("Deposited {amount} to {current_user['username']}'s account. New balance: {current_user['balance']}")
        elif amount <= 0:
                print("Invalid amount. Please try again.")

def withdraw(current_user):
        print("\nWithdraw:")
        amount = validate_input("Enter amount to withdraw: ", float)
        if amount is None and amount > 0:
            if current_user["balance"] >= amount:
                current_user["balance"] -= amount
                print("Withdrew {amount} from {current_user['username']}'s account. New balance: {current_user['balance']}")
            else:
                print("Insufficient funds.")
        elif amount <= 0:
                print("Invalid amount. Please try again.")

def transfer(users):
        print("\nTransfer:")
        recipient_username = input("Enter recipient's username: ")
        amount = validate_input("Enter amount to transfer: ", float)
        if amount is not None and amount > 0:
                if users["balance"] >= amount:
                    recipient_user = find_user_by_username(users, recipient_username)
                    if recipient_user:
                        users["balance"] -= amount
                        recipient_user["balance"] += amount
                        print("Transferred {amount} from {current_user['username']} to {recipient_username}.")
                    else:
                        print("Recipient not found.")
                else:
                    print("Insufficient funds.")
        elif amount <= 0:
                print("Invalid amount. Please try again.")

def check_balance(current_user):
        print("\n{current_user['username']}'s Balance: {current_user['balance']}")


def update_profile(users):
        print("\nUpdate Profile:")
        print("1. Change Password")
        print("2. Change Username")
        print("3. Back to User Menu")
        choice = input("Select an option: ")

        if choice == "1":
            new_password = getpass.getpass("Enter new password: ")
            users["password"] = new_password
            print("Password updated successfully.")
        elif choice == "2":
            new_username = input("Enter new username: ")
            if find_user_by_username(new_username):
                print("Username already exists. Please try again.")
            else:
                users["username"] = new_username
                print("Username updated successfully.")
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please try again.")
    
def logout():
        print("\nLogging out...")
        print("Logged out successfully.")
    
def exit_atm():
        print("\nExiting ATM. Goodbye!")
    
def validate_input(prompt, data_type):
        while True:
            try:
                value = data_type(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid {data_type.__name__}.")
            except TypeError:
                print("Invalid input. Please enter a valid {data_type.__name__}.")
                return None
    
if __name__ == "__main__":
        main()