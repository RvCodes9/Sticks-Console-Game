from colorama import Fore, Style

print(f'\n{Fore.YELLOW}Sticks-Console-Game{Style.RESET_ALL}')

count = 15
char = '|'

def interface(count):
    print(f"\n{Fore.YELLOW}{(char + ' ') * count}{Style.RESET_ALL}")

interface(count)

def control(player):

    global count

    if player == 1:
        count -= 1
        interface(count)

    elif player == 2:
        count -= 2
        interface(count)


game_loop = True

while game_loop:
    
    # Player 1

    player1 = int(input(f"\n{Fore.MAGENTA}Player1 --> {Style.RESET_ALL}"))


    if player1 == 1 or player1 == 2:
        control(player1)

        if count == 1 or count == 0:
            print(f'\n{Fore.GREEN}Win Player1{Style.RESET_ALL}')
            game_loop = False
    
    else:

        while True:
            player1 = int(input(f"\n{Fore.MAGENTA}:: Player1 --> {Style.RESET_ALL}"))

            if player1 == 1 or player1 == 2:
                control(player1)

                if count == 1 or count == 0:
                    print(f'\n{Fore.GREEN}Win Player1{Style.RESET_ALL}')
                    game_loop = False

                break
    
    
    # Player 2

    player2 = int(input(f"\n{Fore.MAGENTA}Player2 --> {Style.RESET_ALL}"))

    if player2 == 1 or player2 == 2:
        control(player2)

        if count == 1 or count == 0:
            print(f'\n{Fore.GREEN}Win Player2{Style.RESET_ALL}')
            game_loop = False

    else:

        while True:
            player2 = int(input(f"\n{Fore.MAGENTA}:: Player2 --> {Style.RESET_ALL}"))

            if player2 == 1 or player2 == 2:
                control(player2)

                if count == 1 or count == 0:
                    print(f'\n{Fore.GREEN}Win Player2{Style.RESET_ALL}')
                    game_loop = False

                break