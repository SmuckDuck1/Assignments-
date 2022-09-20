import random

#f = open("./sdev140-python-loops/Num.txt" ,"at")

f = open("output.txt", "wt")

rangeNum = int(input("How many random number do you want to generate?"))

for i in range (rangeNum):
    num = random.randint(1,500)

    f.write(str(num) + "\n")

f.close()
