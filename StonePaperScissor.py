import random


class Game :
    def __init__ (self) :
        # get the computer's pick
        self.computer_pick = self.get_computer_pick()
        # get the computer's pick
        self.user_input = self.get_user_input()
        # get the winner
        self.winner = self.get_winner()

    def get_computer_pick (self) :
        random_number = random.randint(1, 3)
        selection = selections = {1 : "Rock", 2 : "Scissor", 3 : "Paper"}
        return selection[random_number]

    def get_user_input (self) :
        while True :
            user_input = input("Enter rock/paper/scissor: ")
            if user_input in ("rock", "paper", "scissor") :
                user_input = user_input.capitalize()
                break
            else :
                print("Invalid details!! Please, enter again..")
        return user_input

    def get_winner (self) :
        if self.user_input == self.computer_pick :
            return "Draw!"
        elif self.user_input == "Rock" and self.computer_pick == "Scissor" :
            return "You won!***Rock crushed Scissor***"
        elif self.user_input == "Scissor" and self.computer_pick == "Paper" :
            return "You won!***Scissor cuts Paper***"
        elif self.user_input == "Paper" and self.computer_pick == "Rock" :
            return "You won!***Paper wrapped Rock***"
        else :
            return "You lose!***Better Luck Next Time...***"

    def print_winner (self) :
        print(f"Yours input: {self.user_input}")
        print(f"Computer\'s input: {self.computer_pick}")
        print(self.winner)


# Asking the user to play game again
while True :
    game = Game()
    game.print_winner()
    play_again = input("Do you want to play_again?(y/n)")
    if play_again != 'y' :
        break

# Suppose we want to run our game 2 times, here's how we can do that:
# for i in range(2):
#     c1 = Game()
#     c1.print_winner()

# To play one time only
# c1 = Game()
# c1.print_winner()


