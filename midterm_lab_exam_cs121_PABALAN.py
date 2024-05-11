#Importing sys for the exit function of the program
import sys

# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    "Space Invaders": {"quantity": 4, "cost": 2},
    "Pac-man": {"quantity": 1, "cost": 5},
    # Add more games as needed
}

# Dictionary to store user accounts with their balances and points
user_accounts = {}
balance = float(0)
points = 0

# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# Function to display available games with their numbers and rental costs
def display_available_games():
    clear_terminal()
    print("\nWelcome to the Game Rental System!")
    print("\nHere is the list of available games: ")
    for game,game_info in game_library.items():
         print(f'{game} - copies {game_info["quantity"]} - rental cost {game_info["cost"]}$')

# Function to register a new user
def register_user():
    clear_terminal()
    print("\nRegister to create an account!")
    username = input(str("Input a username: "))
    if username == "":
        main()
    password = input(str("Input a password (must atleast be 8 characters long): "))
    if password == "":
        main()
    if len (password) <8:
        print("\nYour password must atleast be 8 characters long.")
    else:
        user_accounts[username] = {'password':password, 'balance':balance, 'points':points, 'inventory':[]}
        print("\nYou have succesfully created an account!")
    main()

# Function to login to your account
def log_in():
    clear_terminal()
    print("\nLog-in to your account!")
    username = input(str("Enter your username: "))
    if username == "":
        main()
    password = input(str("Enter your password: "))
    if password == "":
        main()
    if username in user_accounts and password == user_accounts[username]['password']:
        print("\nYou have successfully logged in to your account!")
        logged_in_menu(username)
    else:
        print("Invalid Username/Password")
        return
    
# Function to rent a game
def rent_game(username):
    clear_terminal()
    print("\nRent Games!")
    print("\nHere's the list of available games: ")
    try:
        for game, game_info in game_library.items():
            print(f'{game} - copies {game_info["quantity"]} - rental cost {game_info["cost"]}$')
        rent_choice = input(str("Enter the title of the game you want to rent: "))
        if rent_choice == "":
            logged_in_menu(username)
        if rent_choice in game_library:
            if game_library[rent_choice]["quantity"] >0:
                game_price = game_library[rent_choice]["cost"]
                if user_accounts[username]['balance'] >= game_price:
                    game_library[rent_choice]["quantity"] -=1
                    user_accounts[username]['inventory'].append(rent_choice)
                    user_accounts[username]['balance'] -= game_price
                    print(f'You have succesfully rented {rent_choice}.')
                    print(f'Your new Balance is: {user_accounts[username]['balance']}$.')
                    if game_price >= 2:
                        points_earned = game_price/2
                        user_accounts[username]['points'] += points_earned
                        print("\nYou earned one point!")
                else:
                    print("\nInsufficient funds to rent the game.")
            else:
                print("\nThere are no available copies for the game you want to rent.")
        elif input == "":
            return
        else:
            print("\nInvalid title (Type the specific title of the game you want to rent).")
    except ValueError:
        print("Enter only the specific title of the game you want to rent")

# Function to return a game
def return_game(username):
    clear_terminal()
    print("\nReturn a game!")
    print("\nThe following is the list of the games you currently own: ")
    try: 
        user_inventory = user_accounts[username]['inventory']
        if user_inventory:
          for game in user_inventory:
              print(game)
          return_choice = input(str("Enter the title of the game you want to return: "))
          if return_choice in user_inventory:
             game_library[return_choice]['quantity'] +=1
             user_inventory.remove(return_choice)
             print(f'\nYou have successfully returned {return_choice}.')
          elif input == "":
            return
          else:
              print("\nInvalid title (Type the specific title of the game you want to rent).")
        else:
            print("\nYou currently don't own a game")
    except ValueError:
        print("Enter only the specific title of the game you want to return")

# Function to top-up user account
def top_up_account(username):
    clear_terminal()
    while True:
        print("\nWelcome to top-up!")
        print("Top-up your User balance!")
        try:
            amount = float(input("Enter the amount you want to top-up and add to your balance: "))
            if amount > 0:
                user_accounts[username]['balance'] +=amount
                print(f'\nYou have successfully topped-up/added {amount}$ into your account balance.')
                print(f'\nYour new account balance is {user_accounts[username]['balance']}$.')
                return
            elif amount == "":
                return
            else:
                print("Invalid amount (Enter only a sufficient numeric value).")
        except ValueError:
            print("\nEnter only a number.")

# Function to display user's inventory
def display_inventory(username):
    clear_terminal()
    print("\nHere is the list of the games you own: ")
    user_inventory = user_accounts[username]['inventory']
    if user_inventory: 
        for game in user_inventory:
            print(game)
    else:
        print("\nYou currently don't own a game.")
    
# Function for admin to update game details
def admin_update_game(username):
    clear_terminal()
    while True:
        print("\nUpdate games!")
        print("\nHere is the list of available games: ")
        for game,game_info in game_library.items():
            print(f'{game} - copies {game_info["quantity"]} - rental cost {game_info["cost"]}$')
        
        try:
            game_name = input(str("Enter the title of the game you want to update: "))
            if game_name == "":
                admin_menu()
            if game_name in game_library:
                new_quantity = input("Enter the new number of copies of the game: ")
                if new_quantity == "":
                    admin_menu()
                new_cost = input("Enter the new cost of the game: ")
                if new_quantity == "":
                    admin_menu()
                game_library[game_name]['quantity'] = int(new_quantity)
                game_library[game_name]['cost'] = float(new_cost)
                print(f'\nYou have successfully updated {game_name} details.')
                break
            else:
                print("\nInvald title (Enter only the specific title of the game you want to update.")
        except ValueError:
            print("Enter only the specific title of the game you want to update")


# Function for admin login
def admin_login():
    clear_terminal()
    print("\nLogin into an admin account!")
    admin_un = input(str("Enter your username: "))
    admin_pw = input(str("Enter your password: "))
    if admin_un == admin_username and admin_pw == admin_password:
        print("\nYou have successfully logged in to a admin account!")
        admin_menu()
    elif input == "":
        return
    else:
        print("\nInvalid admin username and password.")

# Admin menu
def admin_menu():
    clear_terminal()
    while True:
        print("\nWelcome to the admin menu!")
        print("1) Update game details.")
        print("2) Log out.\n")

        choice = input("Enter the number of your choice: ")
        try:
            if choice == "1":
                admin_update_game(admin_username)
            elif choice == "2":
                print("\nLogging out...")
                break
                main()
            else:
                print("\nInvalid input. (Enter only the number of your choice).")
        except ValueError:
            print("\nEnter only a number.")

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    clear_terminal()
    print("\nRedeem a free game!")
    print("\nHere is the list of available games")
    for game,game_info in game_library.items():
         print(f'{game} - copies {game_info["quantity"]} - rental cost {game_info["cost"]}$')
    try:
        if user_accounts[username]['points'] >= 3:
            game_choice = input(str("Enter the title of the game you want to redeem with your points: "))
            if game_choice in game_library:
                if game_library[game_choice]['quantity'] >0:
                    user_accounts[username]['inventory'].append(game_choice)
                    game_library[game_choice]['quantity'] -=1
                    user_accounts[username]['points'] -=3
                    print(f'\nYou have successfully redeemed {game_choice}')
                    print(f'You have {user_accounts[username]['points']} remaining points.')
                else:
                    print("\nThere are no available copies for the game you want to redeem.")
            elif input == "":
                return
            else:
                print("\nInvalid title (Enter only the specific title of the game you want to redeem).")
        else:
            print("\nInsufficient number of points")
    except ValueError:
        print("\nEnter only the specific title of the game you want to redeem.")

#Function to clear Terminal
def clear_terminal():
    print('\n'*10)

# Function to handle user's logged-in menu
def logged_in_menu(username):
    while True:
        print("\nWelcome to the Game Rental System!")
        print("1) Display available games.")
        print("2) Rent game.")
        print("3) Return game.")
        print("4) Top-up.")
        print("5) Display inventory.")
        print("6) Redeem.")
        print("7) Log-out.")

        choice = input(str("Enter the number of your choice: "))
        try:
            if choice == "1":
                display_available_games()
            elif choice == "2":
                rent_game(username)
            elif choice == "3":
                return_game(username)
            elif choice == "4":
                top_up_account(username)
            elif choice == "5":
                display_inventory(username)
            elif choice == "6":
                redeem_free_rental(username)
            elif choice == "7":
                print("\nLogging out...")
                break
            else: 
                print("\nEnter only the number of your choice")
        except ValueError:
            print("\nEnter only a number")
                                
    
# Main function to run the program
def main():
    while True:
        print("\nWelcome to the Game Rental System")
        print("1) Register.")
        print("2) Log-in.")
        print("3) Admin Log-in.")
        print("4) Exit.\n")

        choice = input("Enter the number of your choice: ")
        try:
            if choice == "1":
                register_user()
            elif choice == "2":
                log_in()
            elif choice == "3":
                admin_login()
            elif choice == "4":
                print("\nExiting the program...")
                sys.exit()
            else:
                print("Input only a number")
        except ValueError:
            print("\nEnter only a number")
main()