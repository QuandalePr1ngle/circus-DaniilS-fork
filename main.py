import random
# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

computer_score = 1
player_score = 1

player_dice = 1
computer_dice = 1

#Blue_Ladders
blue_ladder_18 = 18
blue_ladder_67 = 67
blue_ladder_80 = 80
blue_ladder_74 = 74
#Red_Ladders
red_ladder_15 = 15
red_ladder_39 = 39
red_ladder_33 = 33
red_ladder_87 = 87
#Amount of rounds
for round in range(26):
  round += 1
  if round != 26:
    print("Round " + str(round))
    #Every round types the score of players
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    press_enter = input("Press Enter to throw dice ")
    print(" ")
    #After pressing enter the players throws their dices, they getting number from 1 to 6
    if press_enter == '':
      player_dice = random.randint(1, 6)
      print(f"You got {player_dice}")
      #Adds the number on dice to score
      player_score = player_score + player_dice

      #If a player gets on a ladder then depending on the ladder the player's score changes (For example: if the player's score is 67 then his score changes to 46)
      #Blue Ladders
      if player_score == blue_ladder_18:
        player_score = 7
        print(
            "You stepped on blue ladder. Your score was changed from 18 to 7")
        print(" ")
      elif player_score == blue_ladder_67:
        player_score = 46
        print(
            "You stepped on blue ladder. Your score was changed from 67 to 46")
        print(" ")
      elif player_score == blue_ladder_74:
        player_score = 63
        print(
            "You stepped on blue ladder. Your score was changed from 74 to 63")
        print(" ")
      elif player_score == blue_ladder_80:
        player_score = 69
        print(
            "You stepped on blue ladder. Your score was changed from 80 to 69")
        print(" ")
        #Red Ladders
      if player_score == red_ladder_15:
        player_score = 24
        print(
            "You stepped on red ladder. Your score was changed from 15 to 24")
        print(" ")
      elif player_score == red_ladder_39:
        player_score = 48
        print(
            "You stepped on red ladder. Your score was changed from 39 to 48")
        print(" ")
      elif player_score == red_ladder_33:
        player_score = 52
        print(
            "You stepped on red ladder. Your score was changed from 33 to 52")
        print(" ")
      elif player_score == red_ladder_87:
        player_score = 96
        print(
            "You stepped on red ladder. Your score was changed from 87 to 96")
        print(" ")
      computer_dice = random.randint(1, 6)
      print(f"Computer got {computer_dice}")
      computer_score = computer_score + computer_dice
      #Same rules
      #Blue Ladders
      if computer_score == blue_ladder_18:
        computer_score = 7
        print(
            "Computer stepped on blue ladder. His score was changed from 18 to 7"
        )
        print(" ")
      elif computer_score == blue_ladder_67:
        computer_score = 46
        print(
            "Computer stepped on blue ladder. His score was changed from 67 to 46"
        )
        print(" ")
      elif computer_score == blue_ladder_74:
        computer_score = 63
        print(
            "Computer stepped on blue ladder. His score was changed from 74 to 63"
        )
        print(" ")
      elif computer_score == blue_ladder_80:
        computer_score = 69
        print(
            "Computer stepped on blue ladder. His score was changed from 80 to 69"
        )
        print(" ")
        #Red Ladders
      if computer_score == red_ladder_15:
        computer_score = 24
        print(
            "Computer stepped on red ladder. His score was changed from 15 to 24"
        )
        print(" ")
      elif computer_score == red_ladder_39:
        computer_score = 48
        print(
            "Computer stepped on red ladder. His score was changed from 39 to 48"
        )
        print(" ")
      elif computer_score == red_ladder_33:
        computer_score = 52
        print(
            "Computer stepped on red ladder. His score was changed from 33 to 52"
        )
        print(" ")
      elif computer_score == red_ladder_87:
        computer_score = 96
        print(
            "Computer stepped on red ladder. His score was changed from 87 to 96"
        )
        print(" ")
      else:
        print(" ")
        pass
    #If computers score more than 100 (or 100) then he wons
    if computer_score >= 100:
      print(f"Computer won with score {computer_score}")
      break
    #If your score more than 100 (or 100) then you won
    if player_score >= 100:
      print(f"You won with score {player_score}")
      break
    #If nobody got score of 100 in 25 rounds then its draw
  if round == 26:
    print("Draw!")
    print(
        f"Your score is {player_score} and Computer score is {computer_score}")
