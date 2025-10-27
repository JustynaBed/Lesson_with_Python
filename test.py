# TODO 2: Ask the user for a number and check if it’s even or odd.

# yourNumber = 0
#
# yourNumber = int(input("Podaj liczbę: "))
#
# if yourNumber % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

# TODO 3: Ask for a number N and print all numbers from 1 to N..

# Version 0
# userNumberN = int(input("Give number N: "))
# i = 0
# temporaryNumber = 0
#
# for i in range(userNumberN):
#     i += 1
#     temporaryNumber += 1
#     if temporaryNumber < userNumberN:
#         print("Temporary number is: ", temporaryNumber)
#     elif temporaryNumber == userNumberN:
#         print("Temporary number is equal user number N", temporaryNumber, userNumberN)

# Version 2
# userNumberN = int(input("Give number N: "))
#
# for i in range(1, userNumberN + 1):
#     if i < userNumberN:
#         print("Temporary number is: ", i)
#     elif i == userNumberN:
#         print("Temporary number is equal user number N", i, userNumberN)

# Version 3
# userNumberN = int(input("Give number N: "))
#
# for i in range(1, userNumberN + 1):
#    print(i)

# TODO 4: Calculate the sum of all numbers from 1 to 100 using a loop.
#
# i =  1
# result = 0
#
# while i <= 100:
#     result += i
#     print(i, result)
#     i += 1

# TODO 5: Print all numbers from 1 to 100 that are divisible by 3 but not by 5.

# version 1
i = 1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

# version 2
# i = 1
# startNumber = 0
# endNumber = 100
# for i in range(startNumber, endNumber + 1):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)

# version 3
# i = 1
# endNumber = 100
#
# while i <= endNumber:
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)
#     i += 1