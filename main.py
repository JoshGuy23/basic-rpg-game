from hero import Hero
from slime import Slime
import random

player = Hero("Hero")
enemy = Slime()


def enemy_action(en):
    enemy_choice = random.randint(1, 2)
    return enemy_choice


while enemy.hp > 0 and player.hp > 0:
    print("What would you like to do?")
    choice = int(input("1. Attack or 2. Defend?: "))
    enemy_turn = enemy_action(enemy)

    if choice == 1:
        if enemy_turn == 2:
            print("The Slime defends itself.")
            enemy.defend()
        dmg = int(player.attack(enemy))
        print(f"You did {dmg} damage to the Slime!")
    elif choice == 2:
        print("You take a defensive stance.")
        player.defend()

    if enemy_turn == 1 and enemy.hp > 0:
        dmg = int(enemy.attack(player))
        print(f"The Slime attacked! You took {dmg} damage. You have {player.hp} HP left.")
        if choice == 2:
            player.stop_defending()
    elif enemy_turn == 2:
        enemy.stop_defending()

if enemy.hp <= 0:
    print("You defeated the Slime! Congratulations!")
    player.level_up(enemy)
elif player.hp <= 0:
    print("Game Over.")
