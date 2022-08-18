client = ["Dipesh", "Ram", "Sita"]

print("Enter the client code")
i = 1
for clients in client:
    print(f"{i} --> {clients}")
    i = i+1

print("Enter: ")
clientno = int(input())-1
name = client[clientno]

print(f"You have Choose {name} \n Press \n 1. Data Entry \n 2. Retrieve Data")
choice = int(input())

print("Press\n 1. Diet \n 2. Exercise")
plan = int(input())

def getTime():
    import datetime
    return datetime.datetime.now()

def getData(nam, choice):
    namef = nam
    plan = choice
    if plan == 1:
        with open(f"{namef}_addFood", "w") as addFood:
            timing = getTime()
            diet = (input("Enter diet name"))
            addFood.write(f"{timing} --> {diet}")
    else:
        with open(f"{namef}_addExercise", "w") as addExercise:
            timing = getTime()
            exercise = input("Enter Exercie name")
            addExercise.write(f"{timing}--> {exercise}")

def retrieveData(nam, choice):
    namef = nam
    plan = choice
    if plan == 1:
        with open(f"{namef}_addFood", "rt") as retriveFood:
            retriveFood.read()
    else:
        with open(f"{namef}_addExercise", "rt") as retrieveExercise:
            retrieveExercise.read()

if choice == 1:
    getData(name, plan)
else:
    retrieveData(name, plan)