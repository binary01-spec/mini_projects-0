print("Welcome to my computer quiz!")

play= input("Do you want to play? ").lower()

if play != "yes":
    quit()

print("That's awsome let's play :)")
score = 0
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply ":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print(f"you got {score} question correct")