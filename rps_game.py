
import random
def rock_paper_scissors():
    score_user = 0
    score_comp = 0
    choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        if user == comp:
            print("It's a tie.")
        elif (user == 'rock' and comp == 'scissors') or              (user == 'scissors' and comp == 'paper') or              (user == 'paper' and comp == 'rock'):
            print("You win!")
            score_user += 1
        elif user in choices:
            print("Computer wins!")
            score_comp += 1
        else:
            print("Invalid choice.")
        print(f"Score: User={score_user}, Computer={score_comp}")
        again = input("Play again? (y/n): ")
        if again != 'y':
            break

rock_paper_scissors()
