bill = float(input("Whats the total bill? "))

tip = int(input("What percentage tip would you like to give? "))

people = int(input("How many people to split the bill? "))

tip_to_decimal = tip / 100

bill_with_tip = tip_to_decimal * bill

total = bill + bill_with_tip

total_per_ppl = total / people

print(f"Each person should pay {round(total_per_ppl , 2)}")