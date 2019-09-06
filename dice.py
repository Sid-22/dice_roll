# Run with python3

from random import randrange

def roll(i):
    print(randrange(1,i+1))
    print('\n')
    s = input("Do you want to roll the dice again? (Y or N)")
    if (s=='Y' or s=='y'):
        roll(i)

def main():
    print("Welcome \n")
    i = int(input('Specify the maximum number possible for the dice'))

    print('The maximum possible number is ', i)
    roll(i)

    print("Thanks for playing")

if __name__ == "__main__":
    main()