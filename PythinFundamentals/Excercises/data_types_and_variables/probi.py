#  ord

# letter = input()
#
# print(ord(letter))

# chr
# number = int(input())
#
# print(chr(number))


lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = False
sword_broken = False
count_helmet = 0
count_sword = 0
count_shield = 0
count_armor = 0

for i in range(1, lost_fights_count + 1):

    if i % 2 == 0:
        count_helmet += 1
        helmet_broken = True
    if i % 3 == 0:
        count_sword += 1
        sword_broken = True
    if sword_broken and helmet_broken:
        count_shield += 1
        if count_shield % 2 == 0:
            count_armor += 1

    helmet_broken = False
    sword_broken = False

all = (count_helmet * helmet_price) + (count_armor * armor_price) + (count_sword * sword_price) + (
        count_shield * shield_price)

print(f'Gladiator expenses: {all:.2f} aureus')
