# learning exercise 1 - coin duel

matrix = [["p1 wins","p2 wins"],
          ["p2 wins","p1 wins"]]
choice_dict = {"Head":0,"Tail":1}
#player should be represented as player1, player2, player3,......
def ask_player_choice(player):
    player_index = player[-1]
    player_choice = input(f"What Does Player {player_index} Choose?: ").title().strip()
    player_choice_index = choice_dict.get(player_choice,"Invalid Input Was Given")
    return player_choice_index

player1_choice = ""
while not player1_choice in (0,1):
    player1_choice = ask_player_choice("player1")
    
player2_choice = ""
while not player2_choice in (0,1):
    player2_choice = ask_player_choice("player2")

result = matrix[player1_choice][player2_choice]
result_dict = {"p1 wins":{"English":"Player 1 Wins!","Hindi": "खिलाड़ी 1 जीत गया!"},
"p2 wins":{"English":"Player 2 Wins!","Hindi": "खिलाड़ी 2 जीत गया!"}}
language = "Hindi" #can ask it using input later on
final_result = result_dict[result][language]
print(final_result)