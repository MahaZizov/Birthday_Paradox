import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfyear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfyear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumarate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA


print("Birthday Paradox")
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:
    print("How many birthdays shall I generate?(Max 100)")
    response = input("> ")
    if response.isdecimal() and 0 < int(response) <= 100:
        numbday = int(response)
        break
print()

print("Here are", numbday, "birthdays:")
birthdays = getBirthdays(numbday)
