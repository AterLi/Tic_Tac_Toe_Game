from game_brain import GameBrain

game_dict = {1: "1", 2: "2", 3: "3",
             4: "4", 5: "5", 6: "6",
             7: "7", 8: "8", 9: "9"}

game_start = True
count_steps = [0]

while game_start:
    initiate_game = GameBrain(game_dict)

    # Check if its draw:
    if len(count_steps) == 10:
        print("Draw")
        game_start = False
    else:
        # Calcul which signe turn is
        if (len(count_steps) - 1) % 2 == 0:
            sign = "X"
            player_nr = 1
        else:
            sign = "O"
            player_nr = 2
        try:
            # Show player turn
            print(f"Player nr. {player_nr} turn with {sign} signe")
            user_in = int(input("Choose position: "))
            if user_in in count_steps:
                print("Place already choosen, try again")
                print(count_steps)
                continue
            count_steps.append(user_in)
        except (ValueError, KeyError):
            print("Invalid input, tray again!!!")
        else:
            # “If the input data from the user doesn’t repeat the chosen step or if the input data is not a character,
            # the game continues.
            initiate_game.input_signe(user_in, sign)
            # Find the winner and stop the game
            find_winner = initiate_game.show_winner(sign, player_nr)
            game_start = find_winner
