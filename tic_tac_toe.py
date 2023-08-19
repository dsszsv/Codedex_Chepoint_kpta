import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊ \n2) ✋ \n3) ✌️")


player = int(input("Pick a number: "))
print("===================")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@player@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
player_chose = 0
if player == 1:
    player_chose = "✊"
elif player == 2:
    player_chose = "✋"
elif player == 3:
    player_chose = "✌️"

print("You chose: "+player_chose)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@CPU@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
cpu = random.randint(1,3)

cpu_chose = "0"
if cpu == 1:
    cpu_chose = "✊"
elif cpu == 2:
    cpu_chose = "✋"
elif cpu == 3:
    cpu_chose = "✌️"


print("CPU chose: " + cpu_chose)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Victory@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#1print(player,  cpu)
if player == 1 and cpu == 3:
    print("The player won! ✊ x ✌️")
elif player == 2 and cpu == 1:
    print("The player won! ✋ x ✊")
elif player == 3 and cpu == 2:
    print("The player won! ✌️ x ✋")
elif player == cpu:
    print("It's a TIE!!")
else:
    print("CPU won !!")
