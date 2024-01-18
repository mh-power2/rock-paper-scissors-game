import random
def main_menu ():
    print("1.start the game\n")
    print("2.exit\n")
    x=int(input())
    
    if x ==1 :
        start_game()
    elif x==2 :
        exit_program()
    else :
        print("sorry choose again")
        main_menu()

        
        
def start_game():
    choice_list=["rock","paper","scissors"]
    score_user=0
    score_computer=0
   
    while True:
          
           print("1.rock \n")
           print("2.paper \n")
           print("3.scissors \n")
           print("4.return to main menu \n")
           print("5.exit the game")
           z= int(input("choose number \n"))
           
           y=random.choice(choice_list)
           if z==1 and y=="paper":
               score_computer+=1
               print("cpu win\n")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==3 and y=="paper":
               score_user+=1
               print("you win")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==1 and y=="scissors":
               score_user+=1
               print("you win")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==2 and y=="scissors":
               score_computer+=1
               print("cpu win")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==2 and y=="rock":
               score_user+=1
               print("you win")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==3 and y=="rock":
               score_computer+=1
               print("cpu win")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==1 and y=="rock":
               print("draw")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==2 and y=="paper":
               print("draw")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==3 and y=="scissors":
               print("draw")
               print(f"computer:{score_computer}  you:{score_user}")
           elif z==4 :
               main_menu()
           elif z==5 :
               exit_program()
           else :
               print("choose again")
               start_game() 
   
  
    
        
        
        
def exit_program():
    print("Exiting the program...")
    sys.exit(0)


while True:
    main_menu()