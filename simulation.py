import getpass

users = [
    {"username": "admin", "password": "admin01", "balance": 1000, "role": "admin"},
    {"username": "user1", "password": "user01", "balance": 500, "role": "user"},
    {"username": "user2", "password": "user02", "balance": 300, "role": "user"},
]

current_user = None

def find_user_by_username(username):
    for user in users:
        if user["username"] == username:
            return user
    return None

def main():
    global current_user
    print("Welcome to the ATM Simulation!")
    while current_user is None:
        print("\nEnter your username and password to log in.")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        user = find_user_by_username(username)
        if user and user["password"] == password:
            print("Login successful!")
            current_user = user
            user_menu()
        else:
            print("Invalid username or password. Please try again.")
    print("Thank you for using the ATM!")



def login(users):
    max_attempts =3
    attempts = 0
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        user = find_user_by_username(username)
        if user and user["password"] == password:
            print("Login successful!")
            return user
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1
    print("Maximum login attempts exceeded. Exiting.")


def admin_menu():
    while current_user and current_user["role"] == "admin":
        print("\nAdmin Menu:")
        print("1. Create User")
        print("2. View Users")
        print("3. Logout")
        print("4. Exit ATM")
        choice = input("Select an option: ")
        if choice == 1:
            create_user()
        elif choice == 2:
            view_users()
        elif choice == 3:
            logout()
            break
        elif choice == 4:
            exit_atm()
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while current_user and current_user["role"] == "user":
        print("\nMain Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Update Profile")
        print("6. Logout")
        print("7. Exit ATM")
        choice = int(input("Select an option: "))
        print(choice)
        if choice == 1:
            deposit(current_user)
        elif choice == 2:
            withdraw(current_user)
        elif choice == 3:
            transfer(current_user)
        elif choice == 4:
            check_balance(current_user)
        elif choice == 5:
            update_profile(current_user)
        elif choice == 6:
            logout()
            break
        elif choice == 7:
            exit_atm()
            break
        else:
            print("Invalid choice. Please try again.")

def create_user():
    print("\nCreate User:")
    username = input("Enter username: ")
    if find_user_by_username(username):
        print("Username already exists. Please try again.")
        return
    password = input("Enter password: ")
    balance = validate_input("Enter initial balance: ", float)
    if balance is not None:
        new_user = {
            "username": username,
            "password": password,
            "balance": balance,
            "role": "user",
        }
        users.append(new_user)
        print("User {username} created successfully.")

def view_users():
    print("\nUser List:")
    for user in users:
        print("Username: {user['username']}, Role: {user['role']}, Balance: {user['balance']}")

def deposit(current_user):
    print("\nDeposit:")
    amount = validate_input("Enter amount to deposit: ", float)
    if amount is not None and amount > 0:
        current_user["balance"] += amount
        print("Deposited {amount} to {current_user['username']}'s account. New balance: {current_user['balance']}")
    elif amount is not None and amount <= 0:
        print("Invalid amount. Please enter a positive value.")

def withdraw(current_user):
    print("\nWithdraw:")
    amount = validate_input("Enter amount to withdraw: ", float)
    if amount is not None and amount > 0:
        if current_user["balance"] >= amount:
            current_user["balance"] -= amount
            print("Withdrew {amount} from {current_user['username']}'s account. New balance: {current_user['balance']}")
        else:
            print("Insufficient funds.")
    elif amount is not None and amount <= 0:
        print("Invalid amount. Please enter a positive value.")

def transfer(current_user):
    print("\nTransfer:")
    recipient_username = input("Enter recipient's username: ")
    amount = validate_input("Enter amount to transfer: ", float)
    if amount is not None and amount > 0:
        if current_user["balance"] >= amount:
            recipient_user = find_user_by_username(recipient_username)
            if recipient_user:
                if recipient_user != current_user:
                    current_user["balance"] -= amount
                    recipient_user["balance"] += amount
                    print("amount: ",amount)
                    print("recipient_user: ",recipient_user)
                else:
                    print("Cannot transfer to your own account.")
            else:
                print("Recipient not found.")
        else:
            print("Insufficient funds.")
    elif amount is not None and amount <= 0:
        print("Invalid amount. Please enter a positive value.")

def check_balance(current_user):
    print(current_user['balance'])

def update_profile(current_user):
    while True:
        print("\nUpdate Profile:")
        print("1. Change Password")
        print("2. Change Username")
        print("3. Back to User Menu")
        choice = input("Select an option: ")

        if choice == 1:
            new_password = getpass.getpass("Enter new password: ")
            current_user["password"] = new_password
            print("Password updated successfully.")
        elif choice == 2:
            new_username = input("Enter new username: ")
            if find_user_by_username(new_username):
                print("Username already exists. Please try again.")
            else:
                current_user["username"] = new_username
                print("Username updated successfully.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

def logout():
    global current_user
    print("\nLogging out...")
    current_user = None
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