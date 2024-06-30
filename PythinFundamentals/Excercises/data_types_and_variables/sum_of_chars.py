# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines. On the following N lines – you will receive a letter
# per line. Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].

number_of_line = int(input())

sum_result = 0
for num in range (number_of_line):
    letter = input()
    sum_result += ord(letter)

print(f"The sum equals: {sum_result}")