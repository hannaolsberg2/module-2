#print('hello world') 
# Input
#name_input = input()
#float integer and convert any float number or string of float and true or false
#true=1
#str() will convert anything
#lecture day 4
#and, or, not  not(True) = false  / 2>3 and 3>1 false and true = false
#never do operations in functions
#first_number = int(input())
#second_number = int(input())
#added_result = first_number + second_number
#print(added_result)
#task: convert celsius to farenhiet
#celsius = int(input())
#fahrenheit = (celsius * 9/5) + 32
#print(fahrenheit)
#input value will always be string, so it was be converted into int ot float






#number = 1 
#while number <= 20:
   # print(number)
    #number += 1

## for loop
#range(start,stop,step)

#'stop'
#range(6) 0,1,2,3,4,5
#'start and stop'
#range(2,6) 2,3,4,5
#range(5,2) nothing

#1,2,3,4,5,6,7,8,9,10
#for i in range(1,11):
   # print(i ** 2)
    
#s = input()
#for letters in s:
   # print(letters)


Final_project
    # Initialize the tracker as a dictionary to store all relevant data
def initialize_tracker(budget, project_duration, project_goals):
    tracker = {
        "budget": budget,
        "money_spent": 0,
        "revenue": 0,
        "project_duration": project_duration,  # in days
        "days_completed": 0,
        "project_goals": project_goals,  # total number of goals
        "goals_completed": 0,
        "transaction_log": []  # to track spending and revenue
    }
    return tracker

# Spend money and update the tracker
def spend_money(tracker, amount):
    if amount > tracker["budget"] - tracker["money_spent"]:
        return "Not enough budget available!"
    else:
        tracker["money_spent"] += amount
        tracker["transaction_log"].append(f"Spent {amount}")
        return f"Money spent: {amount}, Total money spent: {tracker['money_spent']}"

# Add revenue and update the tracker
def add_revenue(tracker, amount):
    tracker["revenue"] += amount
    tracker["transaction_log"].append(f"Revenue added {amount}")
    return f"Revenue added: {amount}, Total revenue: {tracker['revenue']}"

# Calculate and return profit or loss
def get_profit_or_loss(tracker):
    profit_or_loss = tracker["revenue"] - tracker["money_spent"]
    if profit_or_loss >= 0:
        return f"Profit: {profit_or_loss}"
    else:
        return f"Loss: {abs(profit_or_loss)}"

# Update project duration progress
def update_days_completed(tracker, days):
    if tracker["days_completed"] + days > tracker["project_duration"]:
        return "You cannot exceed the project duration!"
    else:
        tracker["days_completed"] += days
        return f"Days completed: {tracker['days_completed']}/{tracker['project_duration']}"

def get_project_progress(tracker):
    progress = round((tracker["days_completed"] / tracker["project_duration"]) * 100)
    return f"Project is {progress}% completed."

# Update goals progress
def update_goals_completed(tracker, goals):
    if tracker["goals_completed"] + goals > tracker["project_goals"]:
        return "You cannot exceed the number of project goals!"
    else:
        tracker["goals_completed"] += goals
        return f"Goals completed: {tracker['goals_completed']}/{tracker['project_goals']}"


# Transaction history
def show_transaction_log(tracker):
    return tracker["transaction_log"]