print("Would you like to learn about our science unit?")
Topic =  ["Heterotrophs and autotrophs", "Prokaryotes and eukaryotes", "Key words", ]
Info = ["Autotrophs convert radiant energy from the sun, and turn it into chemical energy. Heterotrophs eat other organisms for energy. Autotrophs and heterotrophs have mitochondria in their cells, breaking down the energy they get into ATP. Some examples of autotrophs are a Cedar Tree, a Sunflower, and Euglena. Some examples of heterotrophs are Lions, Tigers, Bears, Crickets, and humans.","Prokaryotic cells have no nucleus and are less complex. Eukaryotic cells have a nucleus and are more complex. Prokaryotes are only unicellular, while eukaryotes are unicellular and multicellular. For eukaryotes, Genetic material is contained in the nucleus but for prokaryotes, genetic material is contained in the mitochondria. Some organelles in prokaryotic cells are flagellum, cytoplasm, cytoskeleton, mitochondria, and cell wall. Some organelles in eukaryotic cells are cytoplasm, cytoskeleton, nucleus, cell membrane, golgi apparatus, and endoplasmic reticulum", "Unicellular: one cell\nMulticellular: two or more cells\nAsexual reproduction: reproducing with one parent\nSexual reproduction: reproductions with 2 parents\nStimuli: factors in life that living things react to\nDevelop: when cell division occurs and creates more cells\nEvolution:gradual change of organisms over time"]
YorN = input("Type y or n: ")
while YorN != "y" and YorN != "n":
  print("That is not a valid answer")
  YorN = input("Type y or n: ")
turn = 1
counter = 0
score1 = 0
score2 = 0
score3 = 0
choose = 0
if YorN == ("y"):
  print("Great!")
else:
  print("That's too bad, you are learning anyway.")
print("Where do you want to start?")
print(Topic)
Topic2 = input("Pick a number from 1 to 3: ")
while Topic2 != "1" and Topic2 != "2" and Topic2 != "3":
  print("That is not a valid answer")
  Topic2 = input("Pick a number from 1 to 3: ")
print("Are you sure you want to choose", Topic2)
YorN = input("Type y or n: ")
while YorN == "n":
  Topic2 = input("Pick a number from 1 to 3: ")
while YorN != "y" and YorN != "n":
  print("That is not a valid answer")
  YorN = input("Type y or n: ")
  while Topic2 != "1" and Topic2 != "2" and Topic2 != "3":
    print("That is not a valid answer")
    Topic2 = input("Pick a number from 1 to 3: ")
  print("Are you sure you want to choose", Topic2)
  YorN = input("Type y or n: ")
  while YorN != "y" and YorN != "n":
    print("That is not a valid answer")
    YorN = input("Type y or n: ")
while int(Topic2) != 4:
  print(Info[int(Topic2) - 1])
  print("What do you want to do next?")
  Topic2 = input("Pick a number from 1 to 3, type 4 to end:")
  while Topic2 != "1" and Topic2 != "2" and Topic2 != "3" and Topic2 != "4":
    print("That is not a valid answer")
    Topic2 = input("Pick a number from 1 to 3, type 4 to end: ")
  print("Are you sure you want to choose", Topic2)
  YorN = input("Type y or n:")
  while YorN == "n":
    Topic2 = input("Pick a number from 1 to 3, type 4 to end:")
    print("Are you sure you want to choose", Topic2)
    YorN = input("Type y or n:")
  while YorN != "y" and YorN != "n":
    print("That is not a valid answer")
    YorN = input("Type y or n: ")
print("\nIt's game time!")
print("You start of with 0 points, and you can pick how much points you can win from the question before you look at the question. You can't pick more then 10 points each question. If you get the question wrong though, you lose 3 times as many points as you chose. There will be 3 players, and whoever has the most points at the end will win.")
print("\nType A, B, C, or D as your answer(all of the answer choices will not be always included.)")

choose = input("How much points do you want to pick, player 1:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("\nWhich type of cell contains nucleus?\n A.Eukaryotic cells\nB.Prokaryotic cells\n ")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "A" or Topic2 == "a":
  print("Great job")
  score1 += int(choose)
else:
  print("Better luck next time")
  score1 -= int(choose) * 3
choose = input("How much points do you want to pick, player 2:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("Which type of organism can only be unicellular?\n A.Eukaryotes\n B.Prokaryotes\n ")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "B" or Topic2 == "b":
  print("Great job")
  score2 += int(choose)
else:
  score2 -= int(choose) * 3
  print("Better luck next time")
choose = input("How much points do you want to pick, player 3:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("How do heterotrophs gather energy?\n A.They get energy from the sun \n B.They eat nothing and get energy\n C.They don't get energy\n D.They eat other organisms for energy\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c" and Topic2 != "D" and Topic2 != "d":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "D" or Topic2 == "d":
  print("Great job")
  score3 += int(choose)
else:
  print("Better luck next time")
  score3 -= int(choose) * 3
choose = input("How much points do you want to pick, player 1:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("How do autotrophs gather energy?\n A.They get energy from the sun \n B.They eat nothing and get energy\n C.They don't get energy\n D.They eat other organisms for energy\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c" and Topic2 != "D" and Topic2 != "d":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "A" or Topic2 == "a":
  print("Great job")
  score1 += int(choose)
else:
  print("Better luck next time")
  score1 -= int(choose) * 3
choose = input("How much points do you want to pick, player 2:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("What do mitochondria do in cells?\n A.They get energy from the sun \n B.They break down energy to make it into ATP\n C.They don't contain genetic material in a prokaryotic cell\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "B" or Topic2 == "b":
  print("Great job")
  score2 += int(choose)
else:
  print("Better luck next time")
  score2 -= int(choose) * 3
choose = input("How much points do you want to pick, player 3:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("What are the two different types of cells?\n A.Prokaryotes and eukaryotes \n B.Cell membrane and cell wall\n C.Cytoplasm and chloroplast\n D.Mitochondia and Nucleus\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c" and Topic2 != "D" and Topic2 != "d":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "A" or Topic2 == "a":
  print("Great job")
  score3 += int(choose)
else:
  print("Better luck next time")
  score3 -= int(choose) * 3
choose = input("How much points do you want to pick, player 1:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input(" What type of energy do autotrophs turn into chemical energy?\n A.Radiant energy \n B.Cell energy\n C.ATP\n D.Chemical energy\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c" and Topic2 != "D" and Topic2 != "d":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "A" or Topic2 == "a":
  print("Great job")
  score1 += int(choose)
else:
  print("Better luck next time")
  score1 -= int(choose) * 3
choose = input("How much points do you want to pick, player 2:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("Why do cells have a cell wall?\n A.to keep the nucleus warm\n B.No reason\n C.It protects the cell\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "C" or Topic2 == "c":
  print("Great job")
  score2 += int(choose)
else:
  print("Better luck next time")
  score2 -= int(choose) * 3
choose = input("How much points do you want to pick, player 3:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("Which is not a difference between a prokaryote and a eukaryote?\n A.Prokaryotes can only be a unicellular organism, but a eukaryotes can be both multicellular and unicellular\n B.Prokaryotes are less complex, and eukaryotes are more complex\n C.Eukaryotic cells carry genetic material in the mitochondria and prokaryotes contain genetic material in the nucleus\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "C" or Topic2 == "c":
  print("Great job")
  score3 += int(choose)
else:
  print("Better luck next time")
  score3 -= int(choose) * 3
choose = input("How much points do you want to pick, player 1:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
print("These next ones are tough questions, you get double th points!")
Topic2 = input("Where can you find archaea?\n A.All around the world\n B.Inside the plant cell\n C.In extreme evironments\n D.In fresh water\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c" and Topic2 != "D" and Topic2 != "d":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "C" or Topic2 == "c":
  print("Great job")
  score1 += int(choose) * 2
else:
  score1 -= int(choose) * 3
choose = input("How much points do you want to pick, player 2:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("What domain is euglena?\n A.Eubacteria\n B.Protista\n C.Archaea\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "B" or Topic2 == "b":
  print("Great job")
  score2 += int(choose) * 2
else:
  score2 -= int(choose) * 3
choose = input("How much points do you want to pick, player 3:")
while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6" and choose != "7" and choose != "8" and choose != "9" and choose != "10":
  print("That is not a valid answer")
  choose = input("Choose a valid amount please:")
Topic2 = input("?Which animal kingdom follows these properties:\n Has two parents\n Can reproduce sexually\n Hunt for their food\n Are eukaryotes\n A.Plantae\n B.Protista\n C.Anamalia\n D.Archaeabacteria\n")
while Topic2 != "A" and Topic2 != "B" and Topic2 != "a" and Topic2 != "b" and Topic2 != "C" and Topic2 != "c" and Topic2 != "D" and Topic2 != "d":
  print("That is not a valid answer.")
  Topic2 = input("Please type a correct answer:")
if Topic2 == "C" or Topic2 == "c":
  print("Great job")
  score3 += int(choose) * 2
else:
  score3 -= int(choose) * 3
  print("Better luck next time")
print("Player 1 got a score of", score1)
print("Player 2 got a score of", score2)
print("Player 3 got a score of", score3)
if score1 > score2 and score1 > score3:
  print("Player 1 won!")
elif score2 > score1 and score2 > score3:
  print("Player 2 won!")
elif score3 > score2 and score3 > score1:
  print("Player 3 won!")
else:
  print("It was a tie!")