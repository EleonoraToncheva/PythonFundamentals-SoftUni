# Write a program to read an integer N and print all triples of the
# first N small Latin letters, ordered alphabetically:

n = int(input())

start = 97
for i in range (start, start + n):
    for j in range (start, start + n):
        for k in range (start, start + n):
            print(f"{chr(i)}{chr(j)}{chr(k)}")