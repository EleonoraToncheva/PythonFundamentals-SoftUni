# Input
# •	On the first input line, you will receive N – the number of snowballs.
# •	On the next N*3 input lines, you will be receiving data about each snowball.
# Output
# •	You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
# •	The number of snowballs (N) will be an integer in range [0, 100].
# •	The weight is an integer in the range [0, 1000].
# •	The time is an integer in the range [1, 500].
# •	The quality is an integer in the range [0, 100].


# snowball_num = int(input())
#
# best_snowbal = float('-inf')
# for balls in range (1, snowball_num + 1):
#     snowball_weight = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#
#     snowball_value = (snowball_weight // snowball_time) ** snowball_quality
#
#     if snowball_value > best_snowbal:
#         best_snowbal = snowball_value
#         output = f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
#
# print(output)

import sys
snowball_num = int(input())

best_snowbal = float(-sys.maxsize)
for balls in range (1, snowball_num + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight // snowball_time) ** snowball_quality

    if snowball_value > best_snowbal:
        best_snowbal = snowball_value
        print(f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})")


