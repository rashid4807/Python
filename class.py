options = ['kivi','sakset','paperi']
options_quit =['Quit','end', 'skip','e','x']


while True:
   while True:
        player_option = input('kivi','sakset','paperi')
        if player_option in options:
            break
        if player_option in options_quit:
            player_option = None
            break
 
 