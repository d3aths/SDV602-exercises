def play_game():
    
    items = []
    choice = input('You wake up and find yourself inside a house. You look around. To your north, there is a door, west there is a fireplace, east there is a table. Which direction will you go? > ')
    if choice == 'north':
        print('You walk north to the door, opening it and stepping outside. The door slams behind you and locks. A green rolling plain meets you, the distant song of birds reaching your ears from a forest far to the west. To the north lies a great mountain range. East you see the hear a faint call of seagulls. > ')       
        choice = input('') 
    elif choice == 'west':
        print('You walk over to the fireplace, the coals are cold signalling no recent signs of use. You pick a few up and put them in your pocket. You spot a box of matches on top of the fireplace ledge which you take as well. > ')
        items.append('coal')
        items.append('matches')
        choice = input('') 
        if choice == 'east':
            print('You walk to the table. On it lays a knife, which you pick up and take. > ')
            items.append('knife')       
            choice = input('') 
        if choice == 'north':
            print('You walk north to the door, opening it and stepping outside. The door slams behind you and locks. A green rolling plain meets you, the distant song of birds reaching your ears from a forest far to the west. To the north lies a great mountain range. East you see the hear a faint call of seagulls. > ')                
            choice = input('') 
    elif choice == 'east':
        print('You walk to the table. On it lays a knife, which you pick up and take. > ')
        items.append('knife')
        choice = input('') 
        if choice == 'west':
            print('You walk over to the fireplace, the coals are cold signalling no recent signs of use. You pick a few up and put them in your pocket. You spot a box of matches on top of the fireplace ledge which you take as well. > ')
            items.append('coal')
            items.append('matches')
            choice = input('') 
        if choice == 'north':
            print('You walk north to the door, opening it and stepping outside. The door slams behind you and locks. A green rolling plain meets you, the distant song of birds reaching your ears from a forest far to the west. To the north lies a great mountain range. East you see the hear a faint call of seagulls. > ')      
            choice = input('') 
        if choice == 'north':
            print('You start towards the mountain range. There is a fair bit of distance to cover before nightfall. Gradually the air gets colder and the sky gets darker. You decide to set up camp at a rocky outcrop at the base of the mountains to pass the night. Light a fire? > ')
            choice = input('') 
            if 'coal' and 'matches' not in items and choice == 'yes' or choice == 'no':
                print('You don\'t have anything to light a fire with, so you curl up and go to sleep. The mountain air is deathly chilly, and you do not make it through the night. You freeze to death.')
                choice = input('') 
            if 'coal' and 'matches' in items and choice == 'yes':
                print('You light a fire and curl up warmly beside it. During the night, you awaken to growling and grunting coming from the darkness surrounding you. A goblin ambush! Do you get up and fight, or run away into the mountains? > ')
                choice = input('') 
                if choice == 'fight' and 'knife' not in items:
                    print ('You jump to your feet and start swinging your fists at the goblins. They have you surrounded and outnumber you. The first goblin spears you through the chest, and the others pile on top of you bringing you down. The goblins sharp claws start ripping at your flesh, pulling out your organs while you can do nothing but watch on in sickening horror. Thankfully, one of the goblins pulls your eyes out so you dont have to watch the rest of what they do to you. You have died.')
                    choice = input('') 
                elif choice == 'run':
                    print('You stumble to your feet and start running towards the mountains. The goblins dont follow, evidently they only wanted your fire. You carry on into the mountains when you start to hear howls very closeby. Your heart starts to beat and you break out into a run. Unfortunately for you, the wolves smell fear and have your scent. You dont manage to get very far before the pack is on you and have their jaws wrapped around your throat. You have died.')
                    choice = input('')  
                    print(choice)
                elif choice == 'fight' and 'knife' in items:
                    print('You jump to your feet and grab the knife out of your pocket, slashing wildly, you manage to kill the goblins as they rush towards you. After you\'re sure they\'re all dead, you loot the bodies and find a spear, some coins, and a helmet. You go back to sleep and wake up at dawn, heading further into the mountains. Do you take the valley path or trek up the mountain towards its peak? > ')
                    choice = input('') 
    else:
        print('Input not valid')

if __name__ == "__main__":
    format(play_game())