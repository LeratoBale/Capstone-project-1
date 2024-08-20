#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section==== 
# The code for login details in file for user and give feedback if incorrect.
def login_details():
    user = {}
    with open ("user.txt", "r") as file:
        for line in file:
            username, password =line.strip().split(", ")
            user[username] = password
    return user 

# The code for login details in file for user and give feedback if incorrect.
# The code also saves username for future use in code to confirm which user logged in.
def login():
    user = login_details()
    while True:
        username = input("Please enter your Username: \n")
        password = input("Please enter your Password: \n")
        if username in user and user[username] == password:
            print("You have successfully logged in!! \n")
            return username
        else:
            print("You entered the incorrect username or password, Please try again!")

# The program starts below
current_user = login()

while True:
    # The code below will ask user to select options
    # I will add an option for admin to display statistics
    menu = input('''\nSelect one of the following options:
r - register a user (admin only)
a - add task
va - view all tasks
vm - view my tasks
s - view statistics (admin only)                 
e - exit
: ''').lower()
    
    # The Below code will check who logged in to establish if they can register a user
    # It will also confirm that the passwords match.
    # Both the username and password will be saved on txt file 
    # It will allow only the admin to register users but will not allow users who arent admin
    
    if menu == 'r':
        admin_username = "admin"

        if current_user != admin_username:
            print("Only the admin can register users")
            break
        new_username = input("Please enter the new username: \n")
        if new_username in current_user:
                print("The username you entered already exists.")
                new_username = input("\nPlease enter the new username: \n")
        else:
                print("You have successfully registered a username!")
        new_password = input("Enter a new password: \n")
        confirm_password =input("Please confirm the password: \n")
        if new_password == confirm_password:
            with open("user.txt", "a") as file:
                file.write(f"\n{new_username}, {new_password}")
                print("User registered successfully! \n")
                break
        else:
            print("Passwords do not match. Please try again. \n")

    elif menu == 'a':
        # Asked the user of all input needed from instructions and added to txt file.
        # Used date import for app to be able to show current date.
        # All user input was added to task.txt
        username = input("Enter the username of the person the task is assigned to: \n")
        title = input("Enter the title of the task: \n")
        description = input("Enter the description of the task: \n")
        date_assigned = datetime.date.today() 
        due_date = input("Enter the due date of the task (YYYY-MM-DD): \n")
        task_completed = ("No")
        with open("tasks.txt", "a") as file:
            file.write(f"\n{username}, {title}, {description}, {date_assigned}, {due_date}, {task_completed}")
        print("Task added successfully! \n")

    elif menu == 'va':
        # The below code will show the list of all the tasks in the company
        with open("tasks.txt", "r") as file:
            for line in file:
                username, title, description, due_date, new_task_completed, task_completed = line.strip().split(", ") 
                print(f"Task: {title}")
                print(f"Assigned to: {username}")
                print(f"Date Assigned: {new_task_completed}")
                print(f"Due Date: {due_date}")
                print(f"Task Completed: {task_completed}")
                print(f"Task Description: {description}")
                print()

    elif menu == 'vm':
        # In this code I will view task according to who logged in to programme
        # I will also check txt file and print relevant task to username
        # Code Checks Username line by line       
        with open("tasks.txt", "r") as file:
            for line in file:
                username, title, description, due_date, new_task_completed, task_completed = line.strip().split(", ")
                if username == current_user:
                    print(f"Task: {title}")
                    print(f"Assigned to: {username}")
                    print(f"Date Assigned: {new_task_completed}")
                    print(f"Due Date: {due_date}")
                    print(f"Task Completed: {task_completed}")
                    print(f"Task Description: {description}")
                    print()
    
    elif menu == 's':
        # The number of tasks and users will be read by using len and printed as stats
        # If the user is not admin, it will not print stats.
        if current_user == "admin":
            with open("user.txt", "r") as file:
                users = len(file.readlines())
            with open("tasks.txt", "r") as file:
                tasks = len(file.readlines())
            print(f"The number of users is:{users}")
            print(f"The number of tasks are:{tasks}")
        else:
            print("Only the Admin can view Stats!")

    elif menu == 'e':
        print("Goodbye!!! \n")
        exit()

    else:
        print("You have made entered an invalid input. Please try again \n")