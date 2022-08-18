print("Welcome to Health Management System \n")

clients = ["Ram", "Gita", "Sita"]

i = 1
for client in clients:
    print(f"{i} --> {client}")
    i = i+1
print("Please select Your Choice")
name = int(input())-1
fullname = clients[name]

print("Select Your Choice \n Press \n 1. Data Entry \n 2. Data Retrieve")
choice = int(input())

print("Select Your Plan \n 1. Diet \n 2. Exercise")
plan = int(input())

def gettime():
    import datetime
    return datetime.datetime.now()

def dataentry(name, plan):
    if plan == 1:
         with open(f"{name}__adddiet", "a") as addFood:
                foodname = input("Enter Diet Name")
                timing = gettime()
                addFood.write(f"{timing} -- > {foodname}")
    else:
        with open(f"{name}__addexercise", "a") as addExercise:
            foodname = input("Enter Exercise Name")
            timing = gettime()
            addExercise.write(f"{timing} -- > {foodname}")


def dataretrieve(name, plan):
    if plan == 1:
        with open(f"{name}__adddiet", "a") as addFood:
            addFood.read()
    else:
        with open(f"{name}__addexercise", "a") as addExercise:
            addExercise.read()
if choice == 1:
    dataentry(fullname, plan)
else:
    dataretrieve(fullname, plan)
