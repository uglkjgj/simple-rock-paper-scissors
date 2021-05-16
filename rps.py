from players import Player


def winner(hand1, hand2):
    if hand1=='r' and hand2=='s':
        return -1
    elif hand1 == 's' and hand2 == 'r':
        return 1
    elif hand1=='s' and hand2=='p':
        return -1
    elif hand1 == 'p' and hand2 == 's':
        return 1
    elif hand1 == 'p' and hand2 == 'r':
        return -1
    elif hand1 == 'r' and hand2 == 'p':
        return 1
    else:
        return 0


def game(player1, player2):
    player1.move = input('Your move => ')
    import random
    player2.move= random.choice(['r', 's', 'p'])

    if winner(player1.move, player2.move)==-1:
        print(player1.move, 'beats', player2.move, 'Player 1 wins round')
        player1.add_points()
        return 1
    elif winner(player1.move, player2.move)==1:
        print(player2.move, 'beats', player1.move, 'Player 2 wins round')
        player2.add_points()
        return 1
    else:
        print(player1.move, 'is the same as', player2.move, 'Draw')
        return 0


def gameplay():
    gamenum = int(input('How many games do you want to play => '))
    player1 = Player()
    player2 = Player()
    for i in range(gamenum):
        game(player1, player2)

    if player1.points > player2.points:
        print("Player 1 wins")

    elif player1.points == player2.points:
        print("Draw")

    else:
        print("Player 2 wins")


gameplay()
