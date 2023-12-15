import random
import time
print('Welcome to TicTacToe!')
while True: 
    play_or_quit=input('Press p to play and q to quit: ').lower()
    if play_or_quit=='p':
        break
    elif play_or_quit=='q':
        quit()
    else: play_or_quit not in ['p','q']
    continue
boardboxes=['tl','tm','tr','ml','mm','mr','bl','bm','br']
def computer_is_moving():
    while True:
                computer_move=random.randint(0,8)
                if boardboxes[computer_move]!='_':
                    continue
                else:
                    boardboxes[computer_move]=computer_choice
                    print('My turn!')
                    time.sleep(1.25)
                    board()
                    break
def hard_computer_is_moving():
    global boardboxes,computer_choice,player_identity
    while True:
        if boardboxes[2]==boardboxes[5] and boardboxes[2]==computer_choice and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[2]==boardboxes[8] and boardboxes[2]==computer_choice and boardboxes[5]=='_':
            boardboxes[5]=computer_choice
            break
        elif boardboxes[8]==boardboxes[5] and boardboxes[8]==computer_choice and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break
        elif boardboxes[1]==boardboxes[4] and boardboxes[1]==computer_choice and boardboxes[7]=='_':
            boardboxes[7]=computer_choice
            break
        elif boardboxes[1]==boardboxes[7] and boardboxes[1]==computer_choice and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[4]==boardboxes[7] and boardboxes[4]==computer_choice and boardboxes[1]=='_':
            boardboxes[1]=computer_choice
            break
        elif boardboxes[0]==boardboxes[3] and boardboxes[0]==computer_choice and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[0]==boardboxes[6] and boardboxes[0]==computer_choice and boardboxes[3]=='_':
            boardboxes[3]=computer_choice
            break
        elif boardboxes[6]==boardboxes[3] and boardboxes[6]==computer_choice and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break  
        elif boardboxes[6]==boardboxes[4] and boardboxes[6]==computer_choice and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break  
        elif boardboxes[6]==boardboxes[2] and boardboxes[2]==computer_choice and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break  
        elif boardboxes[2]==boardboxes[4] and boardboxes[2]==computer_choice and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[0]==boardboxes[4] and boardboxes[0]==computer_choice and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[0]==boardboxes[8] and boardboxes[0]==computer_choice and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[8]==boardboxes[4] and boardboxes[8]==computer_choice and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break
        elif boardboxes[6]==boardboxes[7] and boardboxes[6]==computer_choice and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[6]==boardboxes[8] and boardboxes[6]==computer_choice and boardboxes[7]=='_':
            boardboxes[7]=computer_choice
            break
        elif boardboxes[8]==boardboxes[7] and boardboxes[8]==computer_choice and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[3]==boardboxes[4] and boardboxes[3]==computer_choice and boardboxes[5]=='_':
            boardboxes[5]=computer_choice
            break
        elif boardboxes[3]==boardboxes[5] and boardboxes[3]==computer_choice and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[5]==boardboxes[4] and boardboxes[5]==computer_choice and boardboxes[3]=='_':
            boardboxes[3]=computer_choice
            break   
        elif boardboxes[0]==boardboxes[1] and boardboxes[0]==computer_choice and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break
        elif boardboxes[0]==boardboxes[2] and boardboxes[0]==computer_choice and boardboxes[1]=='_':
            boardboxes[1]=computer_choice
            break
        elif boardboxes[2]==boardboxes[1] and boardboxes[2]==computer_choice and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break
        elif boardboxes[2]==boardboxes[5] and boardboxes[2]!='_'and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[2]==boardboxes[8] and boardboxes[2]!='_'and boardboxes[5]=='_':
            boardboxes[5]=computer_choice
            break
        elif boardboxes[8]==boardboxes[5] and boardboxes[8]!='_'and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break
        elif boardboxes[1]==boardboxes[4] and boardboxes[1]!='_'and boardboxes[7]=='_':
            boardboxes[7]=computer_choice
            break
        elif boardboxes[1]==boardboxes[7] and boardboxes[1]!='_'and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[4]==boardboxes[7] and boardboxes[4]!='_'and boardboxes[1]=='_':
            boardboxes[1]=computer_choice
            break
        elif boardboxes[0]==boardboxes[3] and boardboxes[0]!='_'and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[0]==boardboxes[6] and boardboxes[0]!='_'and boardboxes[3]=='_':
            boardboxes[3]=computer_choice
            break
        elif boardboxes[6]==boardboxes[3] and boardboxes[6]!='_'and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break  
        elif boardboxes[6]==boardboxes[4] and boardboxes[6]!='_'and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break  
        elif boardboxes[6]==boardboxes[2] and boardboxes[2]!='_'and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break  
        elif boardboxes[2]==boardboxes[4] and boardboxes[2]!='_'and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[0]==boardboxes[4] and boardboxes[0]!='_'and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[0]==boardboxes[8] and boardboxes[0]!='_'and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[8]==boardboxes[4] and boardboxes[8]!='_'and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break
        elif boardboxes[6]==boardboxes[7] and boardboxes[6]!='_'and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[6]==boardboxes[8] and boardboxes[6]!='_'and boardboxes[7]=='_':
            boardboxes[7]=computer_choice
            break
        elif boardboxes[8]==boardboxes[7] and boardboxes[8]!='_'and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[3]==boardboxes[4] and boardboxes[3]!='_'and boardboxes[5]=='_':
            boardboxes[5]=computer_choice
            break
        elif boardboxes[3]==boardboxes[5] and boardboxes[3]!='_'and boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[5]==boardboxes[4] and boardboxes[5]!='_'and boardboxes[3]=='_':
            boardboxes[3]=computer_choice
            break   
        elif boardboxes[0]==boardboxes[1] and boardboxes[0]!='_'and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break
        elif boardboxes[0]==boardboxes[2] and boardboxes[0]!='_'and boardboxes[1]=='_':
            boardboxes[1]=computer_choice
            break
        elif boardboxes[2]==boardboxes[1] and boardboxes[2]!='_'and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break
        #wins ^
        elif boardboxes[4]==player_identity and all (boardboxes[m]=='_' for m in [1,2,3,5,6,7,8]):
            boardboxes[0]=computer_choice
            break
        elif boardboxes[4]==boardboxes[0] and boardboxes[0]==player_identity and boardboxes[8]==computer_choice and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break
        elif boardboxes[4]==boardboxes[2] and boardboxes[2]==player_identity and boardboxes[6]==computer_choice and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[4]==boardboxes[6] and boardboxes[6]==player_identity and boardboxes[2]==computer_choice and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[4]==boardboxes[8] and boardboxes[8]==player_identity and boardboxes[0]==computer_choice and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        #special defense^
        elif boardboxes[4]=='_':
            boardboxes[4]=computer_choice
            break
        elif boardboxes[0]==player_identity and boardboxes[8]=='_':
            boardboxes[8]=computer_choice
            break
        elif boardboxes[2]==player_identity and boardboxes[6]=='_':
            boardboxes[6]=computer_choice
            break
        elif boardboxes[6]==player_identity and boardboxes[2]=='_':
            boardboxes[2]=computer_choice
            break
        elif boardboxes[8]==player_identity and boardboxes[0]=='_':
            boardboxes[0]=computer_choice
            break
        else:
            while True:
                computer_move=random.randint(0,8)
                if boardboxes[computer_move]!='_':
                    continue
                else:
                    boardboxes[computer_move]=computer_choice
                    break
            
            break
    print('My turn!')
    time.sleep(1.25)
    board()


def emptyboard():
    boardboxes[0]='_'
    boardboxes[1]='_'
    boardboxes[2]='_'
    boardboxes[3]='_'
    boardboxes[4]='_'
    boardboxes[5]='_'
    boardboxes[6]='_'
    boardboxes[7]='_'
    boardboxes[8]='_'
def board():
        print(boardboxes[0], boardboxes[1],boardboxes[2])
        print(boardboxes[3], boardboxes[4],boardboxes[5])
        print(boardboxes[6], boardboxes[7],boardboxes[8])
def rules():
    global win,tie
    if boardboxes[2]==boardboxes[5]==boardboxes[8]and boardboxes[2]!='_':
        win=True
    elif boardboxes[1]==boardboxes[4]==boardboxes[7]and boardboxes[1]!='_':
        win=True
    elif boardboxes[0]==boardboxes[3]==boardboxes[6]and boardboxes[0]!='_':
        win=True
    elif boardboxes[6]==boardboxes[4]==boardboxes[2]and boardboxes[6]!='_':
        win=True
    elif boardboxes[0]==boardboxes[4]==boardboxes[8]and boardboxes[0]!='_':
        win=True
    elif boardboxes[6]==boardboxes[7]==boardboxes[8]and boardboxes[6]!='_':
        win=True
    elif boardboxes[3]==boardboxes[4]==boardboxes[5]and boardboxes[3]!='_':
        win=True
    elif boardboxes[0]==boardboxes[1]==boardboxes[2]and boardboxes[0]!='_':
        win=True
    elif boardboxes[0] != '_' and boardboxes[1] != '_' and boardboxes[2] != '_' and boardboxes[3] != '_' and boardboxes[4] != '_' and boardboxes[5] != '_' and boardboxes[6] != '_' and boardboxes[7] != '_' and boardboxes[8] != '_':
        tie=True
print('Do you want a tutorial?')
emptyboard()
while True:
    tutorial=input('y/n: ').lower()
    if tutorial== 'n':
        print('Alright let\'s play')
        break
    if tutorial== 'y':
        print('Here is the board')
        board() 
        print('')
        print('We\'ll randomly assign x and o')
        print('You\'ll be x for the tutorial')
        print('To choose where to go type tl, tm, tr, ml, mm, mr, bl, bm, br')
        print('These represent top middle bottom and left middle right')
        print('Here try putting x in the middle spot on the board')
        while True:
            tutorial_move=input('Your Move: ').lower()
            if tutorial_move== 'mm':
                    print('Great job!')
                    print('Here is the new board:')
                    boardboxes[4]='x'
                    board()
                    print('')
                    print('You ready to leave?')
                    tutorial_leave=input('y/n: ').lower()
                    if tutorial_leave== 'y':
                        break
                    else: 
                        print("Yes you are.")
                        break
            else:
                print('Thats not quite it.')
        break
    if not tutorial== ['n','y']:
        continue
emptyboard()
while True:
    number_of_games=input('How many games do you want to play? ')
    if not number_of_games.isdigit():
         print("Please write a number")
    else:
         break
print(('Hard or easy mode?'))

while True:
    hard_or_easy=input('h/e: ').lower()
    if hard_or_easy=='h':
        hard_mode=True
        break
    if hard_or_easy=='e':
        hard_mode=False
        break
    else: print('Please choose h or e')

number_of_games=int(number_of_games)
current_game=0
word_current_games=1
computer_win=0
player_win=0
player_turn_first=0
player_turn_second=0
tie_win=0
while True:
    if current_game>=number_of_games:
          print('Score '+str(player_win)+' - '+str(computer_win))
          break
    if current_game<number_of_games: 
        current_game+=1
        win=False
        tie=False
        emptyboard()
        print('Score '+str(player_win)+' - '+str(computer_win))
        print('')
        time.sleep(1)
        print('Lets start game '+str(word_current_games)+'!')
        word_current_games+=1
        computer_choice=random.choice(['x','o'])
        if computer_choice=='x':
            player_identity='o'
            player_turn_second+=1
            print('I\'ll be x')
            while True:
                    rules()
                    if win==True:
                        player_win+=1
                        print('Tic...Tac...Toe')
                        time.sleep(1)
                        print('You win!')
                        break
                    if tie==True:
                        tie_win+=1
                        time.sleep(1)
                        print('No more moves we tie!')
                        break
                    if hard_mode==False:
                        computer_is_moving()
                    if hard_mode==True:
                        hard_computer_is_moving()
                    rules()
                    if win==True:
                        computer_win+=1
                        print('Tic...Tac...Toe')
                        time.sleep(1)
                        print('I win!')
                        break
                    if tie==True:
                        tie_win+=1
                        time.sleep(1)
                        print('No more moves we tie!')
                        break
                    while True:
                                player_choice=input('Your Move: ')
                                if player_choice=='tl':
                                    if boardboxes[0]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[0]=player_identity
                                        board()    
                                        break
                                if player_choice=='tm':
                                    if boardboxes[1]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[1]=player_identity
                                        board()    
                                        break
                                if player_choice=='tr':
                                    if boardboxes[2]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[2]=player_identity
                                        board()    
                                        break
                                if player_choice=='ml':
                                    if boardboxes[3]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[3]=player_identity
                                        board()    
                                        break
                                if player_choice=='mm':
                                    if boardboxes[4]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[4]=player_identity
                                        board()    
                                        break
                                if player_choice=='mr':
                                    if boardboxes[5]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[5]=player_identity
                                        board()    
                                        break
                                if player_choice=='bl':
                                    if boardboxes[6]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[6]=player_identity
                                        board()    
                                        break
                                if player_choice=='bm':
                                    if boardboxes[7]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[7]=player_identity
                                        board()   
                                        break
                                if player_choice=='br':
                                    if boardboxes[8]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[8]=player_identity
                                        board()   
                                        break   
                                if player_choice not in ['tl','tm','tr','ml','mm','mr','bl','bm','br']: 
                                    print('Please choose a valid move.')  
        if computer_choice=='o':
            player_identity='x'
            player_turn_first+=1
            print('I\'ll be o')
            print('You go')
            board()
            while True:
                    rules()
                    if win==True:
                        computer_win+=1
                        print('Tic...Tac...Toe')
                        time.sleep(1)
                        print('I win!')
                        break
                    if tie==True:
                        tie_win+=1
                        time.sleep(1)
                        print('No more moves we tie!')
                        break
                    while True:
                                player_choice=input('Your Move: ')
                                if player_choice=='tl':
                                    if boardboxes[0]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[0]=player_identity
                                        board()    
                                        break
                                if player_choice=='tm':
                                    if boardboxes[1]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[1]=player_identity
                                        board()    
                                        break
                                if player_choice=='tr':
                                    if boardboxes[2]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[2]=player_identity
                                        board()    
                                        break
                                if player_choice=='ml':
                                    if boardboxes[3]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[3]=player_identity
                                        board()    
                                        break
                                if player_choice=='mm':
                                    if boardboxes[4]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[4]=player_identity
                                        board()    
                                        break
                                if player_choice=='mr':
                                    if boardboxes[5]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[5]=player_identity
                                        board()    
                                        break
                                if player_choice=='bl':
                                    if boardboxes[6]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[6]=player_identity
                                        board()    
                                        break
                                if player_choice=='bm':
                                    if boardboxes[7]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[7]=player_identity
                                        board()   
                                        break
                                if player_choice=='br':
                                    if boardboxes[8]!='_':
                                        print('That square is taken.')
                                    else:
                                        boardboxes[8]=player_identity
                                        board()   
                                        break   
                                if player_choice not in ['tl','tm','tr','ml','mm','mr','bl','bm','br']: 
                                    print('Please choose a valid move.')
                    rules()
                    if win==True:
                        player_win+=1
                        print('Tic...Tac...Toe')
                        time.sleep(1)
                        print('You win!')
                        break
                    if tie==True:
                        tie_win+=1
                        time.sleep(1)
                        print('No more moves we tie!')
                        break
                    if hard_mode==False:
                        computer_is_moving()
                    if hard_mode==True:
                        hard_computer_is_moving()
print('GG!')
print('Do you wanna see some stats?')
interesting=['i','n','t','e','r','e','s','t','i','n','g','?']
while True:
    stats_q=input('y/n: ').lower()
    if stats_q== 'y':
        print('You won '+str(player_win/number_of_games*100)+'%'+ ' of the time!')
        time.sleep(2)
        print('We tied '+str(tie_win/number_of_games*100)+'%'+ ' of the time!')
        time.sleep(2)
        print('You played first '+str(player_turn_first/number_of_games*100)+'%'+' of games and went second the other ' +str(player_turn_second/number_of_games*100)+'%!')
        time.sleep(2)
        print('Isn\'t that')
        time.sleep(1)
        for x in interesting:
            print(x,end="")
            time.sleep(.5)
        print('')
        print('You waited this long for absolutely no reason...')
        time.sleep(3)
        print('You\'ll never be able to take back those 12 seconds, I hope you realize that...')
        time.sleep(3)
        break
    else:
        break
print('Goodbye!')