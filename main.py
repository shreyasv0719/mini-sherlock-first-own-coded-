print("MINI SHERLOCK — The Detective Trials.\n")
print("------------------------------------------------------------------------------------")
print("Level 1 : The Mystery of the Missing Diamond.\n")
print("------------------------------------------------------------------------------------")
print("A priceless diamond has been stolen from a mansion during a grand party. \n" 
"The theft was discovered at 9:30 PM,\n ")
print("and three suspects are under investigation: the Personal Assistant, the Business Partner,\n"
" and the Gardener.\n")
print("Interrogate the suspects, study the clues, and identify the real thief. Earn 10 points for a correct accusation and 5 for a wrong one.")
print("------------------------------------------------------------------------------------")
print("Solve four mysteries and score at least 35/40 to earn the SHERLOCK BADGE.\n")
print("Your investigation begins now, Detective!")
print("------------------------------------------------------------------------------------")

print("Minimum needed 35/40 points to get SHERLOCK BADGE.\n")

print("Who do you want to interrogate?")
b=print("1. The Personal Assistant")
c=print("2. The Business Partner")
d=print("3. The Gardener")

a = input("Enter your choice (1, 2, or 3): \n")
print("------------------------------------------------------------------------------------\n")
if a == "1":
    print("You chose to interrogate the Personal Assistant.")

elif a == "2":
    print("You chose to interrogate the Business Partner.")

elif a == "3":
    print("You chose to interrogate the Gardener.")

else:
    print("Invalid choice. Please enter 1, 2, or 3.\n")
print("------------------------------------------------------------------------------------")
print("---------------->")
print("Statement of the choosen suspect.\n")
if a == "1":    
    print("I was organizing documents in the office. I never entered the display room.\n")

elif a== "2":
    print("I was talking to guests in the dining hall during the party.\n")       

else:
    print("I was outside tending the garden. I never entered the mansion.\n")    
print  ("------------------------------------------------------------------------------------")
print("clues : .\n")

print("1. Security log: The display room was opened at 9:15 PM using a spare key.\n")
print("Key access: Only the Personal Assistant was authorized to use the spare key that evening.\n")
print("Contradiction: The Personal Assistant claims they never entered the display room.\n")

q=input("Who do you accuse of stealing the diamond? (1, 2, or 3):\n" )
print("------------------------------------------------------------------------------------\n")
print("---------------->")
if q == "1":
    print("You accuse the Personal Assistant.")
elif q == "2":
    print("You accuse the Business Partner.")
else:
    print("You accuse the Gardener.")    

if q == "1":
    print("Correct accusation! You solved the mystery.")
    print("Award 10 points.")
    score= 10
else:
    print("Wrong accusation! The Personal Assistant stole the diamond.")
    print("Award 5 points.")    
    score = 5
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Your score for Level 1: {score}/10")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")