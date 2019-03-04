
color = input("Whats your favorite color?")
print("Your favorite color is: ", color)

principal = int(input("How much do you want to invest?"))
rate = float(input("What is the rate of interest?"))
years = int(input("How long do you want to apply the interest?"))
perYear = int(input("How many times per year is your interest compounded?"))

amount = principal * ((1 + (rate / perYear)) ** (perYear * years))

print( "Your final amount is: ", amount)


