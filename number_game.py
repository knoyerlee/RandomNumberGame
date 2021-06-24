import random

class NumbersGame:
    def __init__(self):
        self.ran_int = 0
        self.user_guess = ''

    def generate_random_number(self):
        self.ran_int = random.randint(1, 101)
        return self.ran_int

    def prompt_user(self):
        self.user_guess = input(f"Please enter a number between 1 and 100: ")
        return self.user_guess

    def compare_numbers(self, pcnum, usernum):
        if(int(usernum) > pcnum):
            print(f"Your guess is too high please try again.")
        elif(int(usernum) < pcnum):
            print(f"Your guess is too low please try again")
        else:
            print(f"You win!")
        