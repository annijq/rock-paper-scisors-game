import random
turns = ['rock', 'paper', 'scissors']
human_turn = input("Enter your turn: ")
computer_turn = random.choice(turns)
human_turns = []
computer_turns = []

while(True):
    print(f'Human:{human_turn} vs. {computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
        if human_turn == 'exit':
            break
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'scissors' :
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock' :
        print('Human wins!')
    else:
        print('Computer wins!')
        
        human_turn = input("Enter your turn: ")
        computer_turn = random.choice(turns)
        print(f' You have played {len(human_turns)}) times')
        human_turns.append(human_turn)
        computer_turns.append(computer_turn)
