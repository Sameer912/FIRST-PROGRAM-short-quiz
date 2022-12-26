print("Do you want to play a quiz? ") 


answer = input("Shall we begin? ").lower()

if answer != 'yes':
    quit()
print("Lets proceed with the questions \n")

total_score = 0

answer = input("What does TRT stand for? ").lower()
if answer == "testosterone":
    print(" Inshallah! Correct")
    total_score +=1 
else:
    print("WTF, it is incorrect!")
    total_score += 0
print ("Score :", total_score, '\n')

answer = input("What does ASCII stand for? ").lower()
if answer == "american standard code for information interchange":
    print(" Inshallah! Correct")
    total_score +=1 
else:
    print("WTF, it is incorrect!")
    total_score += 0
print ("Score :", total_score, '\n')


answer = input("What does BAM stand for? ").lower()
if answer == "binary alignment map":
    print(" Inshallah! Correct")
    total_score +=1 
else:
    print("WTF, it is incorrect!")
    total_score += 0
print ("Score :", total_score, '\n')


answer = input("What does cDNA stand for? ").lower()
if answer == "complementary dna":
    print(" Inshallah! Correct")
    total_score +=1 
else:
    print("WTF, it is incorrect!")
    total_score += 0
print ("Score :", total_score, '\n')

answer = input("What does IBL stand for? ").lower()
if answer == "internal branch length":
    print(" Inshallah! Correct")
    total_score +=1 
else:
    print("WTF, it is incorrect!")
    total_score += 0
print ("Score :", total_score, '\n')

if total_score == 5:
    print("What a talent:)")
elif total_score >1 and total_score <4:
    print("You did pretty well :)")
else:
    print("Big loser :)") 