import random  # importing random to make bot choices


print(
    '''
--- Rock Paper Seccior Game by Umair Khan ---

Rules : 
- First Bot will chose from given options automatically.
- Next it will your turn to choose to from given options.
- According to game rules winner will be decided.

Options :
- Rock = 'r' 
- Paper = 'p' 
- Seccior = 's' 
''')


Bot = random.randint(1, 3)  # Selecting random number in bot value
print("Bot : 'I have selected my choice. Now its your turn.'")
playerchoice = input("Enter your choice : ")


# making bot and botvalues equal to each other
Botchoice = None
if Bot == 1:
    Botchoice = 'r'
elif Bot == 2:
    Botchoice = 'p'
elif Bot == 3:
    Botchoice = 's'


# Comparing both values to get winner
def winner(bc, pc):
    if(bc == pc):
        print("- Its a Tie.")
    elif(bc == 'r' and pc == 'p'):
        print("- You won.")
    elif(bc == 'r' and pc == 's'):
        print("- Bot wins.")
    elif(bc == 'p' and pc == 's'):
        print("- You wons.")
    elif(bc == 'p' and pc == 'r'):
        print("- Bot wins.")
    elif(bc == 's' and pc == 'p'):
        print("- Bot wins.")
    elif(bc == 's' and pc == 'r'):
        print("- You won.")


# Showing bot and player choics
print(f"- Bot choose {Botchoice} and you choose {playerchoice}")


# Using winner function to get winner
winner(Botchoice, playerchoice)
