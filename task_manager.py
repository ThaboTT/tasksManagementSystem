#----Files Project----

#imports
import datetime


def menu():
    option = input("Select an option: ")
    return option
# menu selection function

def reg_user():
    userNamelist = []
    users_list = []
    #variables to store usernames
    new_user = input("Enter your username: ")
    with open('user.txt', 'r+') as f:
     for line in f:
       userNamelist = line.strip().split(", ")
       for i in range(len(userNamelist)):
           if i%2 == 0:
               users_list.append(userNamelist[i])
       while new_user in users_list:                    # checks if inputted name is not on the file
           print(new_user + " already exists. Enter a different username")
           new_user = input("Enter your username: ")
       if new_user not in users_list:
          newPassword = input("Enter your password: ")
          conPassword = input("Confirm your password: ")
          while newPassword != conPassword:
                print("Password does not match. Please enter a matching passwords")
                newPassword = input("Enter new password:")
                conPassword = input("Confirm password:")
          if newPassword == conPassword:
             f.write(", " + new_user + ", " + conPassword)   # writes new user on the file

# registration of new user function

def add_task(taskUser, taskTitle, taskDescription, dateIssued, taskDueDate, taskComplete):
    with open('tasks.txt', 'a+') as f:
         f.write("\n" + taskUser + ", " + taskTitle + ", " + taskDescription + ", " + dateIssued + ", " + taskDueDate + ", " + taskComplete)
# new task addition function

def view_all():
    num = 11
    with open("tasks.txt", "r") as f:
        for line in f:
              f_list = line.split(', ')
              taskNumber = f_list[0]
              taskUser = f_list[1]                             # Sort information
              taskTitle = f_list[2]
              taskDescription = f_list[3]
              dateIssued = f_list[4]
              taskDueDate = f_list[5]
              taskComplete = f_list[6]

              print("\nTask Number:\t\t", num)
              print("Task:\t\t\t", taskTitle)              # Format display
              print("Assigned to:\t\t", taskUser)
              print("Task description:\t", taskDescription)
              print("Date assigned:\t\t", dateIssued)
              print("Due date:\t\t", taskDueDate)
              print("Task Complete?\t\t", taskComplete)
              num += 1
# All tasks viewer function              

def view_mine(username):
    taskNumberCheck = ''
    task_list = ''
    num = 11
    with open("tasks.txt", "r") as f:
          for line in f:
              f_list = line.split(", ")
              task_list = f_list
              if username in line:                        # checks user if false the else statement is executed
                 taskNumber = f_list[0]
                 taskUser = f_list[1]                          # Sort information
                 taskTitle = f_list[2]
                 taskDescription = f_list[3]
                 dateIssued = f_list[4]
                 taskDueDate = f_list[5]
                 taskComplete = f_list[6]
                 print("\nTask Number:\t\t", taskNumber)
                 print("Task:\t\t\t", taskTitle)          # Format information display
                 print("Assigned to:\t\t", taskUser)
                 print("Task description:\t", taskDescription)
                 print("Date assigned:\t\t", dateIssued)
                 print("Due date:\t\t", taskDueDate)
                 print("Task Complete?\t\t", taskComplete)
                 num += 1
                 
                 selection = input("Enter number -1 to return to main menu or task number to edit: ")
                 if selection != "-1" and selection in f_list:                                                  # Checks if the user identifier number is selected if '-1' is not inputted 'else' is executed
                    if taskComplete != f_list[5]:
                       task_list[6] = input("Enter 'Yes' if the task is complete: ")                            # overwrites the indexed list
                       task_list[1] = input("Enter a new username: ")
                       task_list[4] = input("Enter a new due date: ")
                       with open('tasks.txt', 'w') as s:
                            s.writelines(str(", ".join(task_list)))
                    else:
                        print("Task is complete, it cannot be edited")
                 else:
                    return

#Specific user task viewer function
                 
def printMenu_admin():
    print("Please select one of the following options:")
    print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("gr - generate reports")
    print("ds - display reports")
    print("e - exit")
    print
# Print menu function for the Administrator

def printMenu_general():
    print("Please select one of the following options:")    
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    print
# Print menu function for the general user

#variables to store outputs from the open file when the programme initiates
usernameCheck = ""
passwordCheck = ""
userNameList = []
listUsers = []
listPasswords = []

with open("user.txt", "r+") as f:
# loop to read and store outputs
   for line in f:
       userNamelist = line.strip().split(", ")
       for i in range(len(userNamelist)):
           if i%2 == 0:
               listUsers.append(userNamelist[i])
           else:
               listPasswords.append(userNamelist[i])
#Removes newline character in passwords
listPasswords = ([s.strip("\n") for s in listPasswords])

# Loggin in data
login = False

usernameFind = ""
passwordFind = ""

while login == False:
      for i in range(len(listUsers)):
          usernameCheck += listUsers[i] + ""         # stores user names as a string     
      username = input("Enter your username:")
      usernameFind = usernameCheck.find(username)    # checks if username is in the string, if not else statement is executed 
      if username.find(username) != -1:                         # find username in the list and checks the index 
         usernameIndex = listUsers.index(username)   # indexing to check the passwords
         usernameCheck = listUsers[usernameIndex]
         if username == usernameCheck:                # checks for a match listed usernames
            for i in range(len(listPasswords)):
                passwordCheck += listPasswords[i] + ""         # stores passwords as a string
            password = input("Enter your password:")
            passwordFind = passwordCheck.find(password)    # searches for password in the string, if not, else statement is executed
            if password.find(password) != -1:              # finds the password in the list with username index
                    passwordIndex = usernameIndex
                    passwordCheck = listPasswords[passwordIndex]             # Checks for corrected password inputted
                    if password == passwordCheck and username == "admin":    # Login with admin menu
                       printMenu_admin()
                       login = True
                    else:
                        printMenu_general()                                  # Login with general menu
                        login = True                             
            else:
                print("Incorrect password.")                       
      else:
          print("Invalid username")
                             
# Menu Inputs and options

option = menu()

# Registration option, allowed only for the admin
                             
if option == "r" and username == "admin":               # Registers new user
   reg_user()  
# Assigning tasks option
                             
if option == "a":
   taskUser = input("Enter assignment user: ")
   taskTitle = input("Enter title of task: ")
   taskDescription = input("Describe the task: ")
   assignDate = datetime.datetime.now()
   dateIssued = assignDate.strftime("%d %b %Y")              # calls the date from the system           
   taskDueDate = input("Enter due date (dd/month/yyyy): ")   # date format for output
   taskComplete = "No"

   dateIssued = str(dateIssued)
   add_task(taskUser, taskTitle, taskDescription, dateIssued, taskDueDate, taskComplete)    # calls the function and the parameters thereof.
                             
# Viewing tasks option
                           
if option == "va":
   view_all()
   
# Viewing user specific tasks option

if option == "vm":
   view_mine(username)               
   
# report generation option for Admin only
users_task_count = ''
username_count = ''
tasks_count = ''
users_tasks_perc = ''
task_user_perc_list = []
users_tasks_list = []
listUsers = []
list_tasks_check = []
task_complete_count = 0
task_incomplete_count = 0
task_overdue_count = 0
task_user_incomplete = []
task_user_overdue = []
task_user_incomplete_list = []
task_user_totalIncomplete_dict = {}
task_user_overdue_percList = []
task_user_complete_percList = []
task_user_totalPerc_dict = {}
task_user_complete_all_dict = {}
task_user_overdue_all_dict = {}
#Variables t store statistical data

if option == "gr" and username == "admin":
   with open('task_overview.txt', 'w') as s:
    with open('tasks.txt', 'r+') as n:
        for line in n:
            list_tasks = line.split()
            users_tasks_list.append(list_tasks[1])                      #  Adds all usernames in the tasks file
            if "Yes" in list_tasks:                                     #  Checks if task is complete,
                task_complete_count =+ 1
            if "No" in list_tasks:                                      #  Checks if task is incomplete
                task_incomplete_count =+ 1
                task_user_incomplete.append(list_tasks[1])
            assignDate = datetime.datetime.now()
            current_date = assignDate.strftime("%d %b %Y")
            due_date = list_tasks[5]
            if due_date > current_date and "No" in list_tasks:          # Checks if the task is incomplete and overdue
               task_overdue_count =+ 1
               task_user_overdue.append(list_tasks[1])
            list_tasks[1:] = []                                         # Delete all info except index 0 for count
            for i in range(len(list_tasks)):
                list_tasks_check.append(list_tasks[0])
                tasks_count = len(list_tasks_check)

                incomplete_tasks_perc = (task_incomplete_count / tasks_count) * 100         # Calculates the percentage of the incomplete tasks
                overdue_tasks_perc = (task_overdue_count / tasks_count) * 100               # Calculates the percentage of the overdue tasks

        s.write(str(tasks_count) + ", " + str(task_complete_count) + ", " + str(task_incomplete_count) + ", " + str(task_overdue_count) + ", " + str(incomplete_tasks_perc) + ", " + str(overdue_tasks_perc))
         
        with open('user.txt', 'r+') as f:
            for line in f:
                userNamelist = line.split(', ')
                listUsers = []
                for i in range(len(userNamelist)):
                    if i % 2 == 0:                                      # Counts only users
                       listUsers.append(userNamelist[i])
                       username_count = len(listUsers)
        users_task_count = {user: users_tasks_list.count(user) for user in users_tasks_list}                      # counts the number of recurring names and creates a dictinary
        task_user_incomplete_count = {user: task_user_incomplete.count(user) for user in task_user_incomplete}    
        task_user_overdue_count = {user: task_user_overdue.count(user) for user in task_user_overdue}             
        for value in users_task_count.values():                                                                   # outputs the values in the dictonary for calculation 
            task_user_perc = int(value/tasks_count) * 100
            task_user_perc_list.append(task_user_perc)
            for value1 in task_user_incomplete_count.values():                                                    # nested loop to calculate percentages
                task_user_incomplete_perc = (value1/value) * 100
                task_user_incomplete_list.append(task_user_incomplete_perc)                                       # creates a list with all the percentage values
                task_user_complete_perc = 100 - task_user_incomplete_perc
                task_user_complete_percList.append(task_user_complete_perc)
            for value2 in task_user_overdue_count.values():
                task_user_overdue_perc = (value2/value) * 100
                task_user_overdue_percList.append(task_user_overdue_perc)
        for users in users_tasks_list:                                                                            # nested loop to output user and the corresponding percentage value
            for perc in task_user_perc_list:
                task_user_totalPerc_dict[users] = perc                                                            # stores output in the dictionary
            for perc1 in task_user_incomplete_list:
                task_user_totalIncomplete_dict[users] = perc1
            for perc2 in task_user_complete_percList:
                task_user_complete_all_dict[users] = perc2
            for perc3 in task_user_overdue_percList:
                task_user_overdue_all_dict[users] = perc3

        with open('user_overview.txt', 'w') as m:
             m.write(str(username_count) + ', ' )                       # writes all the stats in the file
             m.write(str(tasks_count) + ', ' )
             m.write(str(users_task_count) + ', ' )
             m.write(str(task_user_totalPerc_dict) + ', ' )
             m.write(str(task_user_complete_all_dict) + ', ' )
             m.write(str(task_user_totalIncomplete_dict) + ', ' )
             m.write(str(task_user_overdue_all_dict) + ', ')
             m.write(str(listUsers))
                        
          
if option == "ds" and username == "admin":
   with open('user_overview.txt', 'r+') as f:
        for line in f:
            user_stats_list = line.split(', ')
            username_count = user_stats_list[0]                        # sorts in information
            tasks_count = user_stats_list[1]
            users_task_count = user_stats_list[2]
            task_user_totalPerc_dict = user_stats_list[3]
            task_user_complete_all_dict = user_stats_list[4]
            task_user_totalIncomplete_dict = user_stats_list[5]
            task_user_overdue_all_dict = user_stats_list[6]
            listUsers = user_stats_list[7:]

        print("\nUser Overview Report")
        print("\nUsers Namelist:\t ")
        print('\n'.join(listUsers))
        print("\nNumber of users:\t ", username_count)            
        print("\nNumber of tasks assigned: ", tasks_count)
        print("\nTotal number of tasks assigned to each user: ")        # format display
        print(users_task_count)
        print("\nPercentage of user total number of tasks: ")                                            
        print(task_user_totalPerc_dict)
        print("\nPercentage of user completed tasks: ")
        print(task_user_complete_all_dict)
        print("\nPercentage of user incomplete tasks: ")
        print(task_user_totalIncomplete_dict)
        print("\nPercentage of user incomplete and overdue tasks: ")
        print(task_user_overdue_all_dict)
                        
   with open('task_overview.txt', 'r+') as n:
        for line in n:
            tasks_stats_list = line.split(', ')
            tasks_count = tasks_stats_list[0]
            task_complete_count = tasks_stats_list[1]                      # sorts information
            task_incomplete_count = tasks_stats_list[2]
            task_overdue_count = tasks_stats_list[3]
            incomplete_tasks_perc = tasks_stats_list[4]
            overdue_tasks_perc = tasks_stats_list[5]
            
        print("\nTask Report Overview")
        print("\nNumber of tasks:\t\t ", tasks_count)
        print("Number of Completed Tasks:\t ", task_complete_count)         # format display
        print("Number of Icomplete Tasks:\t ", task_incomplete_count)
        print("Number of overdue Tasks:\t ", task_overdue_count)
        print("Percentage of incomplete tasks: ", incomplete_tasks_perc)
        print("Percentage of incomplete and overdue tasks: ", overdue_tasks_perc)
            
            
if option == "e":
    exit()
      
   
        
