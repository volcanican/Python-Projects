#AVERAGE OF NUMBERS
Play = input("Enter Start if you want to start: ")
N = []
while Play == 'start':
    A = int(input("Enter any number: "))
    N.append((A))
    print("List of the numbers",N)
    print("Count of numbers",len(N))
    u = 0
    for i in N:
        u += i
        print("Sum of Numbers",u)
        Average = u/len(N)
        print("This is the Average",Average)

