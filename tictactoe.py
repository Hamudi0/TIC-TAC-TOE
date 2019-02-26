# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:05:12 2018

@author: hamudi
"""
import itertools
import time

print("WELCOME TO THE TIC TAC TOE GAME!")

time.sleep(0.5)

name = input('What is the name of player1? ')
name2 = input('What is the name of player2? ')

time.sleep(1.0)

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    #Horizontal
    for row in game:
        print(row)
        if all_same(row):
            if row[0] == 1:
                print(f'Player {name} won horizontally!')
            else:
                print(f'Player {name2} won horizontally!')
            return True
    #Diagonal
    diags = []
    
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
        
    if all_same(diags):
            if diags[0] == 1:
                print(f'Player {name} won diagonally!')
            else:
                print(f'Player {name2} won diagonally!')
            return True
            
    diags = []
    
    for ix in range(len(game)):
        diags.append(game[ix][ix])
        
    if all_same(diags):
            if diags[0] == 1:
                print(f'Player {name} won diagonally!')
            else:
                print(f'Player {name2} won diagonally!')
            return True
    #Vertical
    for col in range(len(game)):
        check = []
        
        for row in game:
            check.append(row[col])
        
        if all_same(check):
                if check[0] == 1:
                    print(f'Player {name} won vertically!')
                else:
                    print(f'Player {name2} won vertically!')
                return True
          
    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print('Position already taken! choose another.')
            return game_map, False
        print('   ' + '  '.join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player     
        for count, row in enumerate(game_map):
            print(count, row)
        
        return game_map, True
    
    except IndexError as e:
        print("Did you input row/column correctly? ", e) 
        return game_map, False
    
    except Exception as e:
        print("Something went wrong!! ", e)        
        return game_map, False

play = True
players = [1, 2]

while play:
    game_size = int(input('What size of game do you want? '))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f'Current player: { current_player }')
        played = False
        
        while not played:
            col_choice = int(input('What column would you like to play? (0, 1, 2): '))
            row_choice = int(input('What row would you like to play? (0, 1, 2): '))
            game, played = game_board(game, current_player, row_choice, col_choice)
            
        if win(game):
            game_won = True
            again = input('Would you like to play again? (y/n) ')
            if again.lower() == 'y':
                print('Restarting.....')
                time.sleep(1.0)
            elif again.lower() == 'n':
                print('Byeeee!.....')
                play = False
            else:
                print('Invalid input. See you later.')
                play = False
      
#game = game_board(game, just_display=True)
#game = game_board(game, 1, 3, 1)



