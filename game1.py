 
import random
game_element = ("stone","paper","scissor") 

 

for x in game_element: 
    print("You can choose between ", x) 

 

first_player = str(input("Choose what is in your mind ").lower())  

print("First player choice: ", first_player) 

second_player = random.choice(game_element) 

print("Second player choice: ", second_player) 

 

while first_player not in game_element: 
        print("First player choice is not between ",game_element) 
        break
         
def stonePaperSissior():
     if ((first_player =="stone" and second_player == "scissor")or\
           (first_player == "scissor" and second_player == "paper")or \
        (first_player == "paper" and second_player == "stone")): 
         print("First Player win") 

     elif first_player == second_player: 
         print("Game Draw") 

     else: 
        print("Second player win") 

stonePaperSissior() 