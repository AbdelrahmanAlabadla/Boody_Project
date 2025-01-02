amount=0
interest=0
time=0

while amount<=0:
    amount=float(input("Enter the amount:$"))
    if amount<=0:
        print("The amount cant be lee or equal zero.")
while interest<=0:
    interest=float(input("Enter the interest:""%"))
    if interest<=0:
        print("The interest cant be lee or equal zero.")
while time<=0:
    time=float(input("Enter the time: "))
    if time<=0:
        print("Time cant be lee or equal zero.")

total=amount*(pow(1+interest/100,time))
print(f"The total amount after {time} years is: {total:.2f}")
