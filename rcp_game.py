while True:
    import random
    choices=['rock','paper','scissor']
    robo=random.choice(choices)
    player=None

    while player not in choices:
        player=input('rock,paper,scissor? :').lower()

    if robo==player:
        print('Robo :',robo)
        print('Player :',player)
        print('Tie !!!')

    elif robo == 'rock':
        if player == 'paper':
            print('Robo :',robo)
            print('Player :',player)
            print('You Win!!!')
        if player == 'scissor' :
            print('Robo :',robo)
            print('Player :',player)
            print('You Loose !!!')

    elif robo == 'paper':
        if player == 'scissor':
            print('Robo :',robo)
            print('Player :',player)
            print('You Win!!!')
        if player == 'rock' :
            print('Robo :',robo)
            print('Player :',player)
            print('You Loose !!!')

    elif robo == 'scissor':
        if player == 'rock':
            print('Robo :',robo)
            print('Player :',player)
            print('You Win!!!')
        if player == 'paper' :
            print('Robo :',robo)
            print('Player :',player)
            print('You Loose !!!')

    play_again=input('you want to play again (yes/no)')
    if play_again != 'yes':
        break
print('Bye!!!!')

