import random
random.seed()
max = 5

stat1 = random.randint(0,max)
max = max - stat1

stat2 = random.randint(0,max)
max = max - stat2

stat3 = random.randint(max,max)
max = max - stat3

print(str(stat1) + " " + str(stat2) + " " + str(stat3))