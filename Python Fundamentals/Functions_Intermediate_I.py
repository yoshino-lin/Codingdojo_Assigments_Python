import random
def randInt(min=0, max=100):
    if max<min or max<0:
        return False
    else:
        num = random.randint(min,max)
        return num
# should print a random integer between 0 to 100
print(randInt())
# should print a random integer between 0 to 50
print(randInt(max=50))
# should print a random integer between 50 to 100
print(randInt(min=50))
# should print a random integer between 50 and 500
print(randInt(min=50, max=500))
#bonus
print(randInt(min=500, max=50))
print(randInt(min=-500, max=-50))
