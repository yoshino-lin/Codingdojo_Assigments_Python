#Basic
for i in range(0,151):
    print(i)

#Multiples of Five
for i in range(5,1001,5):
    print(i)

#Counting, the Dojo Way
for i in range(1,101,1):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge
sum = 0
for i in range(0,500000,2):
    sum+=i
print(sum)

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
def flexible_counter(lowNum,highNum,mult):
    same_line=""
    for i in range(lowNum,highNum+1):
        if i%mult==0:
            same_line+=str(i)+", "
    return same_line.strip(', ')
#print(flexible_counter(2,9,3))
