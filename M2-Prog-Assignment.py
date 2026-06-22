# 4.1 -
secret = 7
guess = int(input("Guess "))

if secret > guess:
    print("too low")
elif secret < guess:
    print("too high")
else:
    print("just right")

# 4.2 -

small = True
green = True

if small and green:
    print("pea")
elif small and not green:
    print("cherry")
elif not small and green:
    print("watermelon")
else:
    print("pumpkin")

# 6.1 -
for i in range (3,-1,-1):
    print(i)

# 6.2 -
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    else:
        print("oops")
        break
    number += 1

# 6.3 -
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    else:
        print("oops")
        break

    
