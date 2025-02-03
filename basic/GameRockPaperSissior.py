import random

game_element=("stone","paper","scissor")

rules ={
    "stone":{"stone":"Draw","paper": "lose","scissor":"win"},
    "paper":{"paper": "Draw","scissor":"lose","stone":"win"},
    "scissor":{"paper": "lose","scissor":"Draw","stone":"loose"}
}

print("You can choose between",",".join(game_element))
#print("you can choose between",game_element)

firstplayer = input("Choose an element  ").lower()
print("First player chooses ",firstplayer)


secondPlayer = random.choice(game_element)
print("Second player chooses ",secondPlayer)

if firstplayer not in game_element:
    print("invalid input ")
else:
    result = rules[firstplayer][secondPlayer]
    if result == "win":
     print("first player win")
    if result == "lose":
       print("second Player lose ")
    else:
       print("It is a Draw")
       

