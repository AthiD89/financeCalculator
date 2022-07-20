import math

print("choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("bond to calculate the amount you'll have to pay on a home loan\n")
#Enter choice
choice = input("Enter your choice")
#Investment Calculator
if choice.lower() == "Investment":
    p = int(input("Enter amount you are depositing"))
    r = int(input("Enter the number of years you're investing for:"))
    t = int(input("Enter the interest rate you want"))/100
    interest = input("Do you want simple or compound interest ?")

    if interest == 'Simple':
        pi = p * (1 + (t/100) *p)
        print("Your total is is R",interest)

    elif interest == 'compound':
        r = p * math.pow((1 + r / 100), r)
        print("Your total is R",t)

elif choice.lower() == "bond":
    pv = int(input("Enter the present value of the house"))
    ib = int(input("Enter the interst rate of the bond"))/100
    ny = int(input("Enter the number of years "))
    ad = int(input("Enter the amount you're depositing"))
    repayment = ((ad / 12) * pv) / (1 - (1 + ib / 12) ** (-1 * ny))
    print("Your bond per month will be R", repayment, "per month")
    
    
