def rps():
  player = input("Enter rock, paper, or scissors:")
  choices = ["rock", "paper", "scissors"]
  computer = random.choice(choices)

  if player == computer:
    print(f"Both players selected {computer}. It's a tie!")
  elif player == "rock":
      if computer == "scissors":
          print("Rock smashes scissors! You win!")
      else:
          print("Paper covers rock! You lose.")
  elif player == "paper":
      if computer == "rock":
          print("Paper covers rock! You win!")
      else:
          print("Scissors cuts paper! You lose.")
  elif player == "scissors":
      if computer == "paper":
          print("Scissors cuts paper! You win!")
      else:
        print("Rock smashes scissors! You lose.")