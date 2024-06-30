# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.

# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.

# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion.
# But if you have a motivational party the same day, you spend additional 2 coins per companion.

# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, b
# ut every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.

group_size = int(input())
days = int(input())


coins = 0
for day in range (1, days +1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins += 50 - 2 * group_size

    if day % 3 == 0:
        coins -= 3 * group_size

    if day % 5 == 0:
        coins += 20 * group_size

    if day % 5 == 0 and day % 3 == 0:
        coins -= 2 * group_size

print(f"{group_size} companions received {coins//group_size} coins each.")





