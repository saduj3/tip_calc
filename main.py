#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
print("Let's calculate the tip")
print("This is the change done by the collaborator")
bill = input("what was the total bill? $")
tip = input("how much tip would you like to give? 10,12,15 or 20? ")
people = input("how many people to split the bill? ")
total = float(bill)
tips = float(tip)
# tips_amount = total * (tips/100)
total_amount = total + (total * (tips/100))
num_people = float(people)
per_person = round(total_amount/num_people,2)
print(f"Each person should pay: ${per_person}")