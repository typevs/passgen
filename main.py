import os, time, random, sys

cmd = os.system

carac = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']




def main():
    cmd('cls')
    print(f'Put how many characters you want to generate (If you put 0 or nothing, it will come with 8)')
    amount = input('> ')
    cmd('cls')
    
    if amount == '0':
        amount = '8'

    if amount == '':
        amount = '8'
    print(f'\nSenha Gerada:\n')
    for i in range(int(amount)):
        
        
        password = print(random.choice(carac), end="")
    print(f'\n')
        



if __name__ == '__main__':
    main()
