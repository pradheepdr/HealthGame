import random

initial_health = 50

print("Choose game level ")
game_level = int(input())

print("Your health is ", initial_health)

health = initial_health

number_of_tries = 0

while health <= 100:
    print("Enter random number between 1 to 5 to get health potion")
    try:
        player_input = int(input())
    except ValueError:
        print("Enter only numbers between 1 to 5")

    health_portion_bonus_check = random.randint(1, 5)

    if player_input == health_portion_bonus_check:
        potion_health = int(random.randint(25, 50) / game_level)
        if health + potion_health >= 100:
            health = 100
            break
        else:
            health = health + potion_health
        print("Your increased health is ", str(health))

    else:
        print("Try Again!")

    number_of_tries = number_of_tries + 1

print("You got 100 health in " + str(number_of_tries + 1) + " tries")