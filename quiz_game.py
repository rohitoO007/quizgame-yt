print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
     print("incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
     print("incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
     print("incorrect!")  

print(" you got"+ str(score) +"questions correct!")
print(" you got"+ str((score/4)*100) +"%.")

