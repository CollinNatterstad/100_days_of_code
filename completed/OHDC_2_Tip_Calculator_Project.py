#objective. Create an application that takes user input for a food bill, converts them to the appropriate data type before providing the recommend split for the ultimate bill. 

print("Welcome to the tip calculator")
#collecting total, tip percentage, and number of people. 
total_bill = input("What was the total bill?\n")
tip_percentage = input("What percentage tip would you like to give?\n")
total_people = input("How many people to split the bill?\n")

total_with_tip = float(total_bill)*(1+(int(tip_percentage)/100))
split = round(total_with_tip/int(total_people),2)

print(f"Each person should pay: {split}")

