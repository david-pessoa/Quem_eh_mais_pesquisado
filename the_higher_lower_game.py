from images import vs, img_high_low
from game_data import data
from random import randint
from os import system
from time import sleep
def compare(a, b, tentativa):
    if tentativa == 0:
        return False
    elif a > b:
        return a == tentativa
    else:
        return b == tentativa
score = 0
print(img_high_low)
print("This is the higher lower game, where you guess what gets more googled!")
answer = input("Do you want to play? Type 'yes' or 'no': ")
first_index = randint(0, 49) 
next_index = first_index
while answer == "yes":
    system("cls")
    print(img_high_low)
    print(data[first_index]["name"] + ", a  "+ data[first_index]["description"]+ " from "+ data[first_index]["country"]+ ", which has "+ str(data[first_index]["follower_count"])+ " followers")
    print(vs)
    while first_index == next_index:
        next_index = randint(0, 49)
    print(data[next_index]["name"] + ", a  "+ data[next_index]["description"]+ " from "+ data[next_index]["country"])
    attempt_name = input("Who has more followers, "+ data[first_index]["name"]+ " or "+ data[next_index]["name"]+ "? Type the name: ").title()
    if attempt_name == data[first_index]["name"]:
        num_of_follows = data[first_index]["follower_count"]
    elif attempt_name == data[next_index]["name"]:
        num_of_follows = data[next_index]["follower_count"]
    else:
        num_of_follows = 0
    verify = compare(data[first_index]["follower_count"], data[next_index]["follower_count"], num_of_follows)
    if verify:
        score += 1
        print("Right answer!")
        print(f"Score: {score}")
        sleep(2)
        first_index = next_index
    else:
        print("Wrong answer!")
        print(f"Final Score: {score}")
        answer = input("Do you want to try again? Type 'yes' or 'no': ")
        score = 0
        first_index = randint(0, 49)
        next_index = randint(0, 49)