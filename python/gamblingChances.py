import random
import datetime
count = 0
print("What percentage do you have to win?")
beforePercent = input("")
try:
    beforePercentInt = float(beforePercent)
except:
    print("Number was not a valid percentage. Exiting...")
    exit()
print('How much does it cost?')
moneyCost = input("")
try:
    moneyCostInt = float(moneyCost)
except:
    print('Invalid response. Exiting...')
    exit()
afterPercent = beforePercentInt / 100
chances = 1 / afterPercent
option = input("Brute force (run until success) or run set amount of times? (brute/set):")
countOption = input("Count how many tries it took? (required for cost calculation) (y/n):")
print(f"Chances: 1 in {chances}")
if option == "brute":
    while True:
        startDate = datetime.datetime.now()
        randomNumber = random.randint(1,chances)
        if countOption == "y":
            count = count + 1
        if randomNumber == 1:
            endDate = datetime.datetime.now()
            diff = endDate - startDate
            if countOption == "y":
                print(f"Took {count} tries.")
                print(f"Costs {count * moneyCostInt} for {count} tries.")
            print(f"Success! Processing took {diff.total_seconds()} seconds. Press enter to continue.")
            input("")
            exit()
elif option == "set":
    print("How many times to run?")
    times = input("")
    try:
        timesInt = int(times)
    except:
        print("Invalid response. Exiting...")
        exit()
    startDate = datetime.datetime.now()
    for i in range(timesInt):
        randomNumber = random.randint(1,chances)
        if countOption == "y":
            count = count + 1
        if randomNumber == 1:
            endDate = datetime.datetime.now()
            diff = endDate - startDate
            if countOption == "y":
                print(f"Took {count} tries.")
            print(f"Success! Processing took {diff.total_seconds()} seconds. Press enter to exit.")
            input("")
            exit()
    print("Number not found. Press enter to exit.")
    input("")
    exit()
    pass
else:
    print("Invalid option selected. Exiting...")
    exit()
