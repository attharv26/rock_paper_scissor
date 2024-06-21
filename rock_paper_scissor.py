# Author: Atharv Pandey
# Date  : 20th JUNE, 2024
from random import randint
def winner(user, comp):
    if user == comp:
        return None
    elif(user == 1):
        if(comp == 2):return False
        elif(comp == 3):return True
    elif(user == 2):
        if(comp == 1):return True
        elif(comp == 3):return False
    elif(user == 3):
        if(comp == 1):return False
        elif(comp == 2):return True

arr = {1: 'Rock🪨', 2: 'Paper📃', 3: 'Scissor✂️'}
user_score = 0
comp_score = 0
i = 0
while i!=3:
    try:
        user = int(input('Press\n1: Rock🪨 \n2: Paper📃 \n3: Scissors✂️\n\n\n'))
        comp = randint(1,3)
        print(f'YOU     :{arr[user]}\nCOMPUTER:{arr[comp]}  \n')
        i += 1
        if winner(user, comp):
            user_score += 1
        else:
            comp_score += 1
    except:
        print('INVALID CHOICE')
if user_score > comp_score:
    print("YOU WIN!")
elif comp_score > user_score:
    print("🖥️ WINS!")
elif user_score == comp_score:
    print('its a tie!'.upper())