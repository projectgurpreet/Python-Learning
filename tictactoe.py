import random

rules = "1. Rows and Columns are numbered as 0 1 2 not 1 2 3\n2.Wait For Your Turn Patiently\n3. Don't Press Esc or Ctrl C or Ctrl Z, because they'll terminate the game."
print(rules)

empty_cell = "☐"
circled_cell = "🔾"
crossed_cell = "✕"
choice_list = [circled_cell,crossed_cell]

board = [[empty_cell,empty_cell,empty_cell],
         [empty_cell,empty_cell,empty_cell],
         [empty_cell,empty_cell,empty_cell]]

#*creating the board
def board_printing():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=" ")
        print()

player_list = ["Player", "Computer"]
# active_player = random.choice(player_list)
active_player = "Computer"
#print(f"Now's the Turn of {active_player}")


#* choice filling fucntion
def choice_fill(current_player,choice_to_fill,row_choice,column_choice):
    if board[row_choice][column_choice] == empty_cell:
        board[row_choice][column_choice] = choice_to_fill
    else:
        if current_player == "Player":
            print("Place Was Already Filled, Choose A Different Place")
            playing(current_player)
        else: playing(current_player)


#* Result Checking Function:
def result_check(board):
    result = ""
    if board[0][0] == board[0][1] == board[0][2]:
        result = "Victory"
    return result


#*ask row choice function
def ask_row_choice():
    row_choice = input(f"Which Row Would You Like To Put A {player_move_element}  In?: ")
    try:
        int(row_choice)
        while not int(row_choice) in (0,1,2):
            print("Enter An Integer Between 0 and 2")
            row_choice = ask_row_choice()
    except ValueError:
        print("Wrong Input Type Was Given")
        row_choice = ask_row_choice()
    return int(row_choice)

#*ask column choice function
def ask_column_choice():
    column_choice = input(f"Which Column Would You Like To Put A {player_move_element}  In?: ")
    try:
        int(column_choice)
        while not int(column_choice) in (0,1,2):
            print("Enter An Integer Between 0 and 2")
            column_choice = ask_column_choice()
    except ValueError:
        print("Wrong Input Type Was Given")
        column_choice = ask_column_choice()
    return int(column_choice)


#* checks if the board is full or not
filled_cell_count = 0 
def board_full_check():
    global filled_cell_count
    for i in range(len(board)):
        for j in range(len(board[i])):
            if filled_cell_count == 9:
                break
    print(filled_cell_count)

#* playing function
def playing(current_player):
    global filled_cell_count
    board_full_check()
    if current_player == "Computer":
        move_choice = computer_move_element
        row_choice = random.randint(0,2)
        column_choice = random.randint(0,2)
        choice_fill("Computer",move_choice,row_choice,column_choice)
        global active_player
        active_player = "Player"
        filled_cell_count+=1
        print("This Is The Updated Board After Computer's Turn:")
    else:
        move_choice = player_move_element
        player_row_choice = ask_row_choice()
        player_column_choice = ask_column_choice()
        choice_fill("Player",move_choice,player_row_choice,player_column_choice)
        active_player = "Computer"
        print("This Is The Updated Board After Your Turn:")
        filled_cell_count+=1
    # if result_check(board) == "Victory":
    #     print("Game Was Won")
    
    board_printing()
    playing(active_player)


#* move choices dictionary
move_choices = {"circle":circled_cell,
                "zero":circled_cell,
                circled_cell:circled_cell,
                "cross":crossed_cell,
                "kaata":crossed_cell,
                crossed_cell:crossed_cell}


#* asking player's choice and assigning move elements accordingly
def ask_player_choice(player):
    player_move_choice = input(f"What Would {player} Like To Choose, {circled_cell}  or {crossed_cell} ?: ").strip().lower()
    player_move = move_choices.get(player_move_choice,"Invalid Input Was Given")
    return player_move

player_move_element = ""
while not player_move_element in (circled_cell,crossed_cell):
    player_move_element = ask_player_choice("Player")

computer_move_element = crossed_cell if player_move_element == circled_cell else circled_cell

playing(active_player)

