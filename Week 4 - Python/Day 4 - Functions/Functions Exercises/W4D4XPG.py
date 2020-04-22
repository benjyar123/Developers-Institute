# Exercise 1

from random import randint

def get_random_temp(season):
    if season == "winter":
        return randint(-10, 10)
    elif season == "spring" or "autumn":
        return randint(0, 20)
    elif season == "summer":
        return randint(10, 40)

def main():
    user_season = input("What season would you like a random temperature for?")
    temp = get_random_temp(user_season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temp < 24:
        print("Shorts and t-shirt weather.")
    elif 24 <= temp < 32:
        print("Perfect weather for cricket!")
    elif 32 < temp:
        print("That's way too hot for humans.")
main()

# skipping bonus questions feel comfortable with that already

# Exercise 2

def throw_dice ():
    dice1 = (randint(1, 6))
    dice2 = (randint(1, 6))
    return dice1, dice2

def throw_until_double(roll_count=0):
    rolls = throw_dice()
    while rolls[0] != rolls[1]:
        roll_count += 1
        rolls = throw_dice()
    roll_count += 1
    return(roll_count)

def main ():
    total_rolls = 0
    track_record = []
    for x in range(100):
        total_rolls += throw_until_double()
        track_record.append(throw_until_double())

    average = (total_rolls/len(track_record))

    print(f"Total throws to reach 100 doubles: {total_rolls}")
    print(f"Average number of throws for each double roll: {average}")
    print(f"List of attempts required for each double roll: {track_record}")

main ()

# Exercise 1 from XP Ninja

def get_full_name(**kwargs):
    print(kwargs["first_name"]+kwargs["middle_name"]+kwargs["last_name"])

get_full_name(first_name="John ", middle_name="Lee ", last_name="Hooker")

# Couldn't work out how to make one of the arguments optional'




