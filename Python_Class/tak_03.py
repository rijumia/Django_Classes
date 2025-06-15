numbers = [12, 85, 98, 47, 69, -9]

print("************Print Odd Or Even Number**********")
for num in numbers:
    if num%2==0:
        print("It's Even Number")
    else:
        print("It's Odd Number")

print("*************Print Possitive Or Negative Number****")
for num in numbers:
    if num>=0:
        print("It's Possitive Number")
    else:
        print("It's Negative Number")

print("************Print Odd Or Even Number from 1 to 20**********")
for item in range(1,21):
    if item%2==0:
        print(item,"Is Even Number")
    else:
        print(item,"Is Odd Number")



print("************Print Sum of the all number from a list**********")
total = 0
for num in numbers:
    total += num
print("Sum Of List Number :", total)


print("Count How Many Odd Or Even Numbers From 1 To 20")
even = 0
odd = 0
for n in range(1, 21):
    if n%2==0:
        even += 1
    else:
        odd += 1
print("Total Odd Num:",odd,"Total Even Num: ",even)


print("Find Largest Number in a list")
largest = 0
for num in numbers:
    if num > largest:
        largest = num
print("Largest Number is: ", largest)


print("Print the Multiplication Table of Number 5")
for m in range(1,11):
    print("5*",m,"=",m*5)




