# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

# one:
#
# first_num_character = int(input())
# last_num_character = int(input())
#
# for num in range (first_num_character, last_num_character + 1):
#     num = chr(num)
#     print(num, end= ' ')

# two:
     
first = int(input())
second = int(input())

delimeter = " "
result = ""
for i in range (first, second + 1):
    result += chr(i) + delimeter

print(result.strip())




