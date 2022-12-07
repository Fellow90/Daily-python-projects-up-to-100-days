# #calculating the share of each individual in a party
print("Welcome to the share calculator")
bill = int(input("What is the actual amount of bill?"))
print("The total amount of bill is: ",bill)
percentage = int(input("What percentage of tip would you prefer to give? 10, 20 or 30??"))
total = bill*(100+percentage)/100
no_of_people = int(input("How many people to split the ball?"))
per_person = float(total/no_of_people)
exact_bill = "{:.2f}".format(per_person)
message = f"The individual share is : {exact_bill}"
print(message)