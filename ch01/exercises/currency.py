rate = float(input("What is the current exchange rate for the Euro to Dollar? (Euro per dollar): "))
var1 = rate
print("You said the rate is: €", rate, "per US Dollar")

amount = float(input("What amount of currency do you want to exchange? (€): "))
var2 = amount
print("You said the amount is: €", amount)

total = (amount / rate)
var2 = total
print("The total USD you will receive from the exchange: $", round(total, 2))

result = (total - 3)
var3 = result
print("After a $3.00 service fee, you will receive: $", round(result, 2))
