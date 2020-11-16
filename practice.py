row1 = ['1', '2', '3']
row2 = ['4', '5', '6']
row3 = ['7', '8', '9']

dic = {1:row1[0], 2:row1[1], 3:row1[2], 4:row2[0], 5:row2[1], 6:row2[2], 7:row3[0], 8:row3[1], 9:row3[2]}

player1_numbers = []
player2_numbers = []
win_conditions = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['1','4','7'], ['2','5','8'], ['3','6','9'], ['1','5','9'], ['3','5','7']]

def print_game_board():
    print(row1)
    print(row2)
    print(row3)

 

def game_play():
    print_game_board()
    game_over = False
    player1 = True
    player2 = True
     
    while not game_over:
        while player1:
            #Get player1 input
            player1_input = int(input('player 1 enter a number: '))
            
            #Get value associated with player input
            check_player1_input = dic.get(player1_input)
            
            #Check if space is already used, if not Append value to player1 list
            if check_player1_input == 'X' or 'O':
                print('the space is invalid, enter a different number')
                break
            else:
                player1_numbers.append(check_player1_input)
            
            #Check if value is in row and change value to 'x'
            if check_player1_input in row1:
                myindex = row1.index(check_player1_input) 
                row1[myindex] = 'X'
            elif check_player1_input in row2:
                myindex = row2.index(check_player1_input) 
                row2[myindex] = 'X'
            elif check_player1_input in row3:
                myindex = row3.index(check_player1_input) 
                row3[myindex] = 'X'
            else:
                pass
            
            #Print the updated game board
            print_game_board()
            
            #Check to see if player1 won the game
            if player1_numbers in win_conditions:
                game_over = True
                    #player2_input = False
            else:
                pass      
      
        ##while player2:        
            #Get player1 input
            player2_input = int(input('player 2 enter a number: '))
            
            #Get value associated with player input
            check_player2_input = dic.get(player2_input)
            
            #Check if space is already used, if not Append value to player1 list
            if check_player2_input == 'X' or 'O':
                print('the space is invalid, enter a different number')
                break
            else:
                player2_numbers.append(check_player2_input)
            
            #Check if value is in row and change value to 'o'
            if check_player2_input in row1:
                myindex = row1.index(check_player2_input) 
                row1[myindex] = 'O'
            elif check_player2_input in row2:
                myindex = row2.index(check_player2_input) 
                row2[myindex] = 'O'
            elif check_player2_input in row3:
                myindex = row3.index(check_player2_input) 
                row3[myindex] = 'O'
            else:
                pass
            
            #Print the updated game board
            print_game_board()
            
            #Check to see if player2 won the game
            if player2_numbers in win_conditions:
                game_over = True
                    
            else:
                pass      
       
        while game_over:
            print('you win!')
            break
game_play() 



    

    

