from number_game import NumbersGame as ng

game = ng()
attempts = 0
random_num = game.generate_random_number()
print(random_num)

while(True):
    print(f"(Type q and hit enter to end the game or win.)\n")
    try:
        user_guess = game.prompt_user()
        if(user_guess == 'q'):
            print("Exiting...")
            break
        game.compare_numbers(random_num, user_guess)
    except ValueError:
        print("Please only enter a number or the letter q")
        continue
    
    attempts += 1
    if(attempts == 1):
        print(f"You have made {attempts} guess so far")
    else:
        print(f"You have made {attempts} guesses so far")

    if(int(user_guess) == random_num):
            break
    print("__________________________________________________________________")


