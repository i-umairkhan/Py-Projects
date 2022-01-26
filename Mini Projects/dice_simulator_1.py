import random
from os import system


def dice(self):
    if num == 1:
        print("*")
    if num == 2:
        print("* *")
    if num == 3:
        print("* * *")
    if num == 4:
        print('''* * 
* *''')
    if num == 5:
        print('''*   * 
  * 
*   * ''')
    if num == 6:
        print('''* * 
* * 
* * ''')


if __name__ == "__main__":
    _ = system('cls')
    num = random.randint(1, 6)
    dice(num)
