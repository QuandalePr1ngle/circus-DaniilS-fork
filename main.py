import random


computer_score = 1
player_score = 1

player_dice = 1
computer_dice = 1

#Blue_Ladders
Blue_Ladder18 = 18
Blue_Ladder67 = 67
Blue_Ladder80 = 80
Blue_Ladder74 = 74
#Red_Ladders
Red_Ladder15 = 15
Red_Ladder39 = 39
Red_Ladder33 = 33
Red_Ladder87 = 87
for Round in range(26):
  Round += 1
  if Round != 26:
    print("Round " + str(Round))
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    Throw = input("Press Enter to throw dice ")
    print(" ")
    if Throw == '':
      player_dice = random.randint(1, 6)
      print(f"You got {player_dice}")
      player_score = player_score + player_dice
      #Blue_Ladders
      if player_score == Blue_Ladder18:
        player_score = 7
        print(
            "You stepped on blue ladder. Your score was changed from 18 to 7")
        print(" ")
      elif player_score == Blue_Ladder67:
        player_score = 46
        print(
            "You stepped on blue ladder. Your score was changed from 67 to 46")
        print(" ")
      elif player_score == Blue_Ladder74:
        player_score = 63
        print(
            "You stepped on blue ladder. Your score was changed from 74 to 63")
        print(" ")
      elif player_score == Blue_Ladder80:
        player_score = 69
        print(
            "You stepped on blue ladder. Your score was changed from 80 to 69")
        print(" ")
        #Red_Ladders
      if player_score == Red_Ladder15:
        player_score = 24
        print(
            "You stepped on red ladder. Your score was changed from 15 to 24")
        print(" ")
      elif player_score == Red_Ladder39:
        player_score = 48
        print(
            "You stepped on red ladder. Your score was changed from 39 to 48")
        print(" ")
      elif player_score == Red_Ladder33:
        player_score = 52
        print(
            "You stepped on red ladder. Your score was changed from 33 to 52")
        print(" ")
      elif player_score == Red_Ladder87:
        player_score = 96
        print(
            "You stepped on red ladder. Your score was changed from 87 to 96")
        print(" ")
      computer_dice = random.randint(1, 6)
      print(f"Computer got {computer_dice}")
      computer_score = computer_score + computer_dice
      #Blue_Ladders
      if computer_score == Blue_Ladder18:
        computer_score = 7
        print(
            "Computer stepped on blue ladder. His score was changed from 18 to 7"
        )
        print(" ")
      elif computer_score == Blue_Ladder67:
        computer_score = 46
        print(
            "Computer stepped on blue ladder. His score was changed from 67 to 46"
        )
        print(" ")
      elif computer_score == Blue_Ladder74:
        computer_score = 63
        print(
            "Computer stepped on blue ladder. His score was changed from 74 to 63"
        )
        print(" ")
      elif computer_score == Blue_Ladder80:
        computer_score = 69
        print(
            "Computer stepped on blue ladder. His score was changed from 80 to 69"
        )
        print(" ")
        #Red_Ladders
      if computer_score == Red_Ladder15:
        computer_score = 24
        print(
            "Computer stepped on red ladder. His score was changed from 15 to 24"
        )
        print(" ")
      elif computer_score == Red_Ladder39:
        computer_score = 48
        print(
            "Computer stepped on red ladder. His score was changed from 39 to 48"
        )
        print(" ")
      elif computer_score == Red_Ladder33:
        computer_score = 52
        print(
            "Computer stepped on red ladder. His score was changed from 33 to 52"
        )
        print(" ")
      elif computer_score == Red_Ladder87:
        computer_score = 96
        print(
            "Computer stepped on red ladder. His score was changed from 87 to 96"
        )
        print(" ")
      else:
        print(" ")
        pass
    if computer_score >= 100:
      print(f"Computer won with score {computer_score}")
      break
    if player_score >= 100:
      print(f"You won with score {player_score}")
      break
  if Round == 26:
    print("Draw!")
    print(
        f"Your score is {player_score} and Computer score is {computer_score}")
