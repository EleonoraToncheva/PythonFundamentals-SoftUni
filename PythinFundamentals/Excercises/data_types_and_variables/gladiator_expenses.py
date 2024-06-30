

lost_fight_count = int(input())

helmet_price = float(input())
swored_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmet_brocken_count = 0
sword_brocken_count = 0
shield_brocken_count = 0
armor_brocken_count = 0



for lost_fight in range (1, lost_fight_count + 1):
    if lost_fight % 2 == 0:
        helmet_brocken_count += 1
    if lost_fight % 3 == 0:
        sword_brocken_count += 1

    if lost_fight % 6 == 0 :
        shield_brocken_count += 1
        if shield_brocken_count % 2 == 0:
            armor_brocken_count += 1

total_expences = (helmet_price * helmet_brocken_count) + (swored_price * sword_brocken_count )+ (shield_price * shield_brocken_count) + (armor_price * armor_brocken_count)

print(f"Gladiator expenses: {total_expences:.2f} aureus")


# lost_fight_count = int(input())
#
# helmet_price = float(input())
# swored_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# helmet_brocken = False
# sword_brocken = False
# helmet_brocken_count = 0
# sword_brocken_count = 0
# shield_brocken_count = 0
# armor_brocken_count = 0
#
#
#
# for lost_fight in range (1, lost_fight_count + 1):
#     if lost_fight % 2 == 0:
#         helmet_brocken_count += 1
#         helmet_brocken = True
#     if lost_fight % 3 == 0:
#         sword_brocken_count += 1
#         sword_brocken = True
#     if helmet_brocken and sword_brocken:
#         shield_brocken_count += 1
#         if shield_brocken_count % 2 == 0:
#             armor_brocken_count += 1
#     helmet_brocken = False
#     sword_brocken = False
#
# total_expences = (helmet_price * helmet_brocken_count) + (swored_price * sword_brocken_count )+ (shield_price * shield_brocken_count) + (armor_price * armor_brocken_count)
#
# print(f"Gladiator expenses: {total_expences:.2f} aureus")
