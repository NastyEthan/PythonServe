import random

def rps():
  player = input("Enter rock, paper, or scissors:")
  choices = ["rock", "paper", "scissors"]
  computer = random.choice(choices)

  print(f"The computer chose {computer}")

  if player == computer:
    print("It's a tie!")
  elif player == "paper":
      if computer == "rock":
          print("Paper beats rock! you win!")
      else:
          print("Scissors beats paper, you lose.")
  elif player == "rock":
      if computer == "scissors":
          print("Rock beats scissors, you win!")
      else:
          print("Paper beats rock, you lose.") 
  elif player == "scissors":
      if computer == "paper":
          print("Scissors beats paper, you win!")
      else:
        print("Rock beats scissors, you lose.")