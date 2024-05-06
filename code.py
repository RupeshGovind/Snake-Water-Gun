import random

choices = {
    0: "Snake",
    1: "Water",
    2: "Gun"
}

def check(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    return 1

while True:
    comp = random.randint(0, 2)

    user = int(input("0 for Snake, 1 for Water, and 2 for Gun: "))
    
    if user not in choices:
      print("Invalid choice.\nPlease type S for Snake\nW for Water\nG for Gun.")
      continue
    
    print("You choose:", choices[user])
    print("Computer choose:", choices[comp])
    result = check(comp, user)
     
    if result == 0:
        print("It's a draw!")
    elif result == -1:
        print("You lose!")
    else:
        print("You win!")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != 'Y':
        print("Thanks for playing. Goodbye!")
        break
    