import random

def run():
    player_points = 20
    guess_left = 10
    num = list(str(random.randint(1000,9999)))
    while guess_left > 0:   
        user_guess=list(str(input("Guess a Number (4 Digits):")))
        n = num.copy()
        
        guess_left -= 1
        i_p = []
        c_p = []
        if user_guess == num :
            print('All digits are in correct place!\nYou Win!')
            player_points+=5
            break
        else:
            for i in range(len(num)):
                if num[i]==user_guess[i]:
                        c_p.append(num[i])
            
            for digit in user_guess:
                if digit in n:
                    i_p.append(digit)
                    n.remove(digit)

            print(f'{len(i_p)} digits: {i_p} guessed correctly. {len(c_p)} in correct position')
            print(f'{guess_left} turns left')
            player_points-=2
    if guess_left>0:
        print(f"Your Score = {player_points}")
    else:
        print(f'You have lost the Game and Scored {player_points}')

ch = ['y','Y']
while 'y' in ch or "Y" in ch:
    run()
    print('Do you want to Play again? (Y/N)')
    ch = [input()]
