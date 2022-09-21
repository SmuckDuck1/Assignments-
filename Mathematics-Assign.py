u_input = 0
total = 1

u_input = int(input("Enter a non-negative number: "))

if u_input > 0:
    for x in range(1, u_input+1):
        total = total * x

print(str(total))