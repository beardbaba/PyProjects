#If the bill was $150.00, split between 5 people with 12% tip.
#Each person should pay (150/5)*1.12 [[rounded off to 2 Decimal places]]


print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
converted_percent_tip = (1 + (percent_tip/100))
split = int(input("How many people to split the bill? "))
total_split = total_bill/split
tip_split = round(total_split * converted_percent_tip,2)
print(f"Each person should pay {tip_split}")
