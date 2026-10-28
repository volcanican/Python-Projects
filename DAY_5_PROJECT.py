#SIMPLE INTEREST
P = float(input("Enter the Prinicipal Amount: "))
R = float(input("Enter The Rate Of Interest: "))
T = float(input("Enter The Time Duration in months: "))

i = (P*R*T)/100
print("The Simple Interest On the Amount Is:",i)
A = P + i
if T/12 == 1:
    print(f"The Total at the end of {T/12} year is: {A}")
else:
    print(f"The Total at the end of {T/12} years is: {A}")