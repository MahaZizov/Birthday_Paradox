import datetime, random

def get_birthdays(numb_of_birthdays):
    birthdays = []
    for i in range(numb_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
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
birthdays = get_birthdays(numbday)

for i, birthday in enumerate (birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month -1]
    dateText = '{}{}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = get_match(birthdays)
print('In this simulation ', end='')

if match is not None:
    monthName = MONTHS[match.month-1]
    dateText = '{}{}'.format(monthName, match.day)
    print('Multiple have a birthday on ', dateText)
else:
    print('There are no matching birthdays')
print()

print('Generating', numbday, 'random birthdays 100000 times')
input('Press enter to begin')

print('Let\'s run another 100000 simulations')

simMatch = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(numbday)
    if get_match(birthdays) is not None:
        simMatch += 1
print('100000 simulations run')

probability = round(simMatch / 100000 * 100, 2)
print('Out of 100000 simulations of', numbday, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numbday, 'people have a', probability, '% chance of')
print('having a matching birthday in their group')
print('That\'s probably more than you would think!')








