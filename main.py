import random
def game():
  # TIC TAC TOE
  print("Welcome to the Tic Tac Toe Game")

  board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   

  # Draws Board
  def DrawBoard():    
      print(" %c | %c | %c " % (board[1],board[2],board[3]))    
      print("___|___|___")    
      print(" %c | %c | %c " % (board[4],board[5],board[6]))    
      print("___|___|___")    
      print(" %c | %c | %c " % (board[7],board[8],board[9]))    
      print("   |   |   ")    


  # Initial Board
  DrawBoard()

  userChoice = 0
  AIChoice = 0

  # Game Loop
  while True:
      userChoice=int(input("Enter a number 1-9, where you want to mark:"))

      if(userChoice==1 and board[1]==' '):
        board[1] = 'X'
      elif(userChoice==2 and board[2]==' '):
        board[2] = 'X'
      elif(userChoice==3 and board[3]==' '):
        board[3] = 'X'
      elif(userChoice==4 and board[4]==' '):
        board[4] = 'X'
      elif(userChoice==5 and board[5]==' '):
        board[5] = 'X'
      elif(userChoice==6 and board[6]==' '):
        board[6] = 'X'
      elif(userChoice==7 and board[7]==' '):
        board[7] = 'X'
      elif(userChoice==8 and board[8]==' '):
        board[8] = 'X'
      elif(userChoice==9 and board[9]==' '):
        board[9] = 'X'
      else:
        print("Not a Valid Position")
        userChoice=int(input("Enter a number 1-9, where you want to mark:"))
        if(userChoice==1 and board[1]==' '):
          board[1] = 'X'
        elif(userChoice==2 and board[2]==' '):
          board[2] = 'X'
        elif(userChoice==3 and board[3]==' '):
          board[3] = 'X'
        elif(userChoice==4 and board[4]==' '):
          board[4] = 'X'
        elif(userChoice==5 and board[5]==' '):
          board[5] = 'X'
        elif(userChoice==6 and board[6]==' '):
          board[6] = 'X'
        elif(userChoice==7 and board[7]==' '):
          board[7] = 'X'
        elif(userChoice==8 and board[8]==' '):
          board[8] = 'X'
        elif(userChoice==9 and board[9]==' '):
          board[9] = 'X'

      AIChoice=random.randint(1,9)
      if(AIChoice==1 and board[1]==' '):
        board[1] = 'O'   
      elif(AIChoice==2 and board[2]==' '):
        board[2] = 'O'
      elif(AIChoice==3 and board[3]==' '):
        board[3] = 'O'
      elif(AIChoice==4 and board[4]==' '):
        board[4] = 'O'
      elif(AIChoice==5 and board[5]==' '):
        board[5] = 'O'
      elif(AIChoice==6 and board[6]==' '):
        board[6] = 'O'
      elif(AIChoice==7 and board[7]==' '):
        board[7] = 'O'
      elif(AIChoice==8 and board[8]==' '):
        board[8] = 'O'
      elif(AIChoice==9 and board[9]==' '):
        board[9] = 'O'
      else:
        AIChoice=random.randint(1,9)
        if(AIChoice==1 and board[1]==' '):
          board[1] = 'O'   
        elif(AIChoice==2 and board[2]==' '):
          board[2] = 'O'
        elif(AIChoice==3 and board[3]==' '):
          board[3] = 'O'
        elif(AIChoice==4 and board[4]==' '):
          board[4] = 'O'
        elif(AIChoice==5 and board[5]==' '):
          board[5] = 'O'
        elif(AIChoice==6 and board[6]==' '):
          board[6] = 'O'
        elif(AIChoice==7 and board[7]==' '):
          board[7] = 'O'
        elif(AIChoice==8 and board[8]==' '):
          board[8] = 'O'
        elif(AIChoice==9 and board[9]==' '):
          board[9] = 'O'
    
      DrawBoard()

      if(board[1]=='X' and board[2]=='X' and board[3]=='X'):
        print("You Won!")
        
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[4]=='X' and board[5]=='X' and board[6]=='X'):
        print("You Won")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[7]=='X' and board[8]=='X' and board[9]=='X'):
        print("You Won")
        
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[1]=='X' and board[5]=='X' and board[9]=='X'):
        print("You Won")
        
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[3]=='X' and board[5]=='X' and board[9]=='X'):
        print("You Won")
        
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[1]=='X' and board[4]=='X' and board[7]=='X'):
        print("You Won")
      
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[2]=='X' and board[5]=='X' and board[8]=='X'):
        print("You Won")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[3]=='X' and board[6]=='X' and board[9]=='X'):
        print("You Won")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;



      if(board[1]=='O' and board[2]=='O' and board[3]=='O'):
        print("Computer Won!")
        
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[4]=='O' and board[5]=='O' and board[6]=='O'):
        print("Computer Won!")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[7]=='O' and board[8]=='O' and board[9]=='O'):
        print("Computer Won!")
      
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      

      elif(board[1]=='O' and board[5]=='O' and board[9]=='O'):
        print("Computer Won!")
      
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[3]=='O' and board[5]=='O' and board[9]=='O'):
        print("Computer Won!")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[1]=='O' and board[4]=='O' and board[7]=='O'):
        print("Computer Won!")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[2]=='O' and board[5]=='O' and board[8]=='O'):
        print("Computer Won!")
        
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;

      elif(board[3]=='O' and board[6]=='O' and board[9]=='O'):
        print("Computer Won!")
       
        playagain=input("Do you want to Play again(y/n):")
        if(playagain=='y'):
          game()

        if(playagain=='n'):
          print("Thanks for Playing")
          break;
  else:
   print("It's a Tie")
      
      
game()
