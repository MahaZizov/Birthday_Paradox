import random, sys, time

WIDTH = 140

try:
    columns = [0] * WIDTH
    while True:
        for i in range (WIDTH):
            if random.random() < 0.02:
                columns[i] = random.randint(4, 14)#length of streak
            if columns[i] == 0:
                print(' ', end='')
            else:
                print(random.choice([0, 1]), end='') #the part that prints 0s and 1s
                columns[i] -= 1 #diminishes the length of said streak
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
