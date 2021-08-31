# Basic

for x in range(151):
    print(x)

# Multiples of Five

for y in range(5,1001,5):
    print(y)

# Counting, the Dojo Way

for z in range(1,101):
    if z % 10 == 0:
        print('Dojo')
    elif z % 5 == 0:
        print('Coding')
    else:
        print(z)

# Whoa. That Sucker's Huge

b = 0
for a in range(0,500001):
    if a % 2 == 1:
        b += a
print(b)

# Counting by Fours

for c in range(2018,0,-4):
    print(c)

# Flexible Counter

lowNum = 2
highNum = 9
mult = 3

for d in range(lowNum,highNum+1):
    if d % mult == 0:
        print(d)