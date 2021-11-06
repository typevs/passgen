import random, string


def main():
    try:
        print(f'Put how many characters you want to generate (If you put 0 or nothing, it will come with 8)')
        amount = input('> ')
    
        if amount == '0':
            amount = '8'

        if amount == '':
            amount = '8'

        print(f'\nPassword Generated:\n')
        try:
            for i in range(int(amount)):
        
                senha = print(random.choice(string.digits + string.ascii_letters), end="")
            print(f'\n')
        except:
            main()
    except KeyboardInterrupt:
        exit()



if __name__ == '__main__':
    main()
