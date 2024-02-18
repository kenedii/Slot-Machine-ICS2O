
#             culminatingtask_slotmachine ICS2O
#             Final Programming Assignment
#            Created on: January 14, 2020
#         Last Modified on: January 17, 2020
#
#    A slot machine game that rolls the slots with different odds for each. The user starts out with $100 and spends $5 per roll. There is a very small chance of winning the jackpot of $1 million (increases by $5 each roll).
# -Costs $5 instead of $20 so the user can play more games (odds are set so the house still wins in the end)
#Uses the following modules to improve the program

#random is used to roll a random number which is assigned to a symbol
import random
#time is used to make a delay between each roll
import time
#replit is used to clear screen after each replay/when the user is done.
import replit
#v  used to make coloured text  v
from termcolor import colored


#clears the screen to get rid of the import text when importing colored for the first time
replit.clear()


#Initial jackpot value, increases by $1.5 every time the user loses (other $3.5 goes to house)
jackpot = 1000000

#Starts the user out with $100 balance
balance = 100

#Kills the game if the user does not want to play again (if the user selects no, it does Kill = True and will cancel the loop)
kill = False


#prints the instructions
print ("Welcome to the Million Dollar Jackpot Slots Game!")
print ("You will start out with $100 to play with on us!")
print ("Each game costs $5.")
print ("To win, you will need to match 3 of the same symbol.")
print ("If you get a money bag, you will win $50. If you get a triple money bag, you win the jackpot of $1,000,000!")
print ("")
print (colored("_________________________________________________", 'green'))
print ("")
print ("[ 🍉  ]          [ 🔔  ]          [ 🍒  ]")
print ("[ 🍉  ]  = $20   [ 🔔  ]  = $40   [ 🍒  ] = $60")
print ("[ 🍉  ]          [ 🔔  ]          [ 🍒  ]")
print (colored("_________________________________________________", 'green'))
print ("")
print ("         [ 💎  ]          [ 💰  ]")
print ("         [ 💎  ] = $100   [ 💰  ] = JACKPOT!!!")
print ("         [ 💎  ]          [ 💰  ]")
print (colored("_________________________________________________", 'green'))

print ("")
#asks user to press any key to start the game.
readytoplay = input("Press Enter to play.")
#clears the welcome message and just shows the info message.
replit.clear()

#Loop to allow user to re play game.
while balance >= 5 and kill == False:
  replit.clear()
  #repeats instructions without the $100 starting thing and "press any key." message
  print ("Each game costs $5.")
  print ("To win, you will need to match 3 of the same symbol.")
  print ("If you get a money bag, you will win $50. If you get a triple money bag, you win the jackpot of $1,000,000!")
  print ("")
  print (colored("_________________________________________________", 'green'))
  print ("")
  print ("[ 🍉  ]          [ 🔔  ]          [ 🍒  ]")
  print ("[ 🍉  ]  = $20   [ 🔔  ]  = $40   [ 🍒  ] = $60")
  print ("[ 🍉  ]          [ 🔔  ]          [ 🍒  ]")
  print (colored("_________________________________________________", 'green'))
  print ("")
  print ("         [ 💎  ]          [ 💰  ]")
  print ("         [ 💎  ] = $100   [ 💰  ] = JACKPOT!!!")
  print ("         [ 💎  ]          [ 💰  ]")
  print (colored("_________________________________________________", 'green'))

  print ("")
  print ("")
  #       Prints the player's balance
  print ("Your balance is $"+ str(balance))
  #               Prints the jackpot
  print ("The jackpot is $"+ str(jackpot))
  #     Only accepts Enter key as input or it gets mad at you
  play1 = input("Press the >Enter< key to roll the slots!")
  print ("")



  # Rolls a random symbol with different odds for each symbol (1/100 odds for moneybag)
  if play1 == (""):
    balance = (balance-5)
    jackpot = (jackpot+1.50)
  #waits 1.5 secs before roll
    time.sleep(1.5)
    roll1 = random.randint(1,100)
    #40% chance of watermelon
    if roll1 <= 40:
      #changes the variable roll1 to a simpler number to make it easier to determine if a user won or not.
      roll1=1
      print ("[ 🍉  ]")
    #40% chance of bell
    if roll1 <= 70 and roll1 > 40:
      roll1=2
      print ("[ 🔔  ]")
    #30% chance of cherry
    if roll1 <= 90 and roll1 > 70:
      roll1=3
      print ("[ 🍒  ]")
    #9% chance on diamond
    if roll1 < 100 and roll1 > 90:
      roll1=4
      print ("[ 💎  ]")
    #1% chance of money bag
    if roll1 == 100:
      roll1=5
      print ("[ 💰  ]")

    #waits 1.5 secs before next roll
    time.sleep(1.5)

    # Rolls a random symbol with different odds for each symbol (1/1000 odds for moneybag)
    roll2 = random.randint(1,1000)
    #40% chance of watermelon
    if roll2 <= 400:
      roll2=1
      print ("[ 🍉  ]")
    #40% chance of bell
    if roll2 <= 700 and roll2 > 400:
      roll2=2
      print ("[ 🔔  ]")
    #30% chance of cherry
    if roll2 <= 900 and roll2 > 700:
      roll2=3
      print ("[ 🍒  ]")
    #9% chance on diamond
    if roll2 < 1000 and roll2 > 900:
      roll2=4
      print ("[ 💎  ]")
    #1/1000 chance on money bag
    if roll2 == 1000:
      roll2=5
      print ("[ 💰  ]")
    
    #waits 1.5 secs before next roll
    time.sleep(1.5)

    # Rolls a random symbol with different odds for each symbol (1/10000 odds for moneybag)
    roll3 = random.randint(1,10000)
    #40% chance of watermelon
    if roll3 <= 4000:
      roll3=1
      print ("[ 🍉  ]")
    #40% chance of bell
    if roll3 <= 7000 and roll3 > 4000:
      roll3=2
      print ("[ 🔔  ]")
    #30% chance of cherry
    if roll3 <= 9000 and roll3 > 7000:
      roll3=3
      print ("[ 🍒  ]")
    #9% chance on diamond
    if roll3 < 10000 and roll3 > 9000:
      roll3=4
      print ("[ 💎  ]")
    #1/10000 chance on bag
    if roll3 == 10000:
      roll3=5
      print ("[ 💰  ]")

#if user gets 3 cherrys they get $20
    if roll1 == 1 and roll2 == 1 and roll3 == 1:
      print (colored("Congratulations! You win $20!", 'green'))
      #adds $20 to balance
      balance = balance+20
      #prints balance
      print ("Your balance is $"+ str(balance)+".")
      #asks user if they would like to play again
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        #if they select N then kill=true. this makes it so the loop wont activate again.
        kill = True

#if user gets 3 bells they get $40
    elif roll1 == 2 and roll2 == 2 and roll3 == 2:
      print (colored("Congratulations! You win $40!", 'green'))
      balance = balance+40
      print ("Your balance is $"+ str(balance)+".")
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        kill = True

#if user gets 3 cherries they get $60
    elif roll1 == 3 and roll2 == 3 and roll3 == 3:
      print (colored("Congratulations! You win $60!", 'green'))
      balance = balance+60
      print ("Your balance is $"+ str(balance)+".")
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        kill = True
      
# if user gets 3 diamonds they get $100
    elif roll1 == 4 and roll2 == 4 and roll3 == 4:
      print (colored("Congratulations! You win $100!",'green'))
      balance = balance+60
      print ("Your balance is $"+ str(balance)+".")
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        kill = True
    

#jackpot roll ( triple money bag)
    elif roll1 == 5 and roll2 == 5 and roll3 == 5:
      print ("🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
      #prints the jackpot amount as prize winnings
      print (colored("Congratulations! You win the jackpot!! of $"+str(jackpot)+"!", 'green'))
      print ("🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
      #adds jackpot amount to their balance
      balance = balance+jackpot
      print ("Your balance is $"+ str(balance)+".")
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        kill = True

        
      # single/double money bag prizes
    elif roll1 == 5 or roll2 == 5 or roll3 == 5:
      #gives them 50 per money bag if roll1 and roll2 are money bags
      if roll1 == 5 and roll2 ==5:
        #the prize they win from money bags
        prize = 100
      #gives them 50 per money bag if roll1 and roll3 are money bags
      elif roll1 == 5 and roll3 == 5:
        prize = 100
      #gives them 50 per money bag if roll2 and roll3 are money bags
      elif roll2 == 5 and roll3 == 5:
        prize = 100
      #if they didnt get one of the combinations above then they only got 1 money bag, gives them 50$
      else:
        prize = 50

      print ("")
      print (colored("💰💰 You won a money bag! 💰💰", 'green'))
      print ("")
      print (colored("$50 has been added to your balance.", 'green'))
      #adds the prize value from above to their balance
      balance = balance+prize
      print("")
      #prints their balance
      print ("Your balance is $"+ str(balance)+".")
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        kill = True      

    #if the user does not win, it will tell them they lost
    else:
      print ("")
      print (colored("Sorry! You lost this game. 😢", 'red'))
      print (colored("Better luck next time!", 'red'))
      print ("")
      print ("You have $"+ str(balance),"left.")
      print ("")
      playagain = input("Would you like to play again? Y/N ")
      if playagain == "Y".lower():
        continue
      if playagain == "N".lower():
        kill = True

  else:
    print ("")
    print ("")
    print ("Incorrect input!")
    continue


#clears the screen to tell user they lost
replit.clear()



print ("Thank you for playing the Million Dollar Jackpot Slots Game! ")

#if they have a balance over 0, it tells the user their balance they finished with
if balance > 0:
  print ("You finished with a balance of $"+str(balance))

#if their balance is 0, it gives them a different message that they lost all their money
if balance == 0:
  print ("You lost all your money! Try again next time.")