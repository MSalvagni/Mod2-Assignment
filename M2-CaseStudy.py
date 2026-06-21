# Megan Salvagni
# Mod 2 Case Study: If Else & While

# This program will ask a student for their name and GPA 
# and tells us what award the student qualifies for if any

last_name = input("What is your last name? ")

while last_name != "ZZZ":
    
    first_name = input("What is your first name? ")
    print(first_name, last_name)

    GPA = float(input("What is your GPA? "))
    if GPA >= 3.5:
        print("You made the Dean's list!")
    elif GPA >= 3.2:
        print("You made the honor roll!")
    else:
        print(f"GPA: {GPA}")

    last_name = input("What is your last name? (ZZZ to quit) ")

print("Program Ended")


