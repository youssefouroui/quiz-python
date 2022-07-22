print("welcom to my game")

player=input("do you want to play")
if player!="yes":
     quit()
print("ok let's play")
score=0
answer1=input("what is python?:")
if answer1=="Python is an interpreted object oriented":
     print("Correct!")
     score+=1

else:
     print("Incorrect!")
answer2=input("How do you insert COMMENTS in Python code?:")
if answer2=="# this is a comments":
     print("Correct!")
     score += 1
else:
     print("Incorrect!")
answer3=input("What is the correct file extension for Python files??:")
if answer3==".py":
     print("Correct!")
     score += 1
else:
     print("Incorrect!")
answer4=input("What is the correct way to create a function in Python?:")
if answer4=="def myFunction():":
     print("Correct!")
     score += 1
else:
     print("Incorrect!")
answer5=input("Which operator is used to multiply numbers?:")
if answer5=="*":
     print("Correct!")
     score += 1
else:
     print("Incorrect!")
print( score, "question correct!")