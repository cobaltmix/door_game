import random
inv = []
shards = 0
health= 0
class_selected= 0
gob_attack= 0
gob_defense= 0
strength= 0
defense = 0
gob_health = 0
skel_defense=0 
skel_health=0 
skel_attack=0

def select_class(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    print("READ BEFORE PLAYING GAME: To progress through scenarios, press enter or type in the answer to the prompt given.")
    print("Please select the class you will be playing with throughout your journey.")
    while True:
        class_selected = input("Warrior, Palladin, Mage: ").lower()
        if class_selected == "warrior":
            strength = 15
            defense = 15
            health = 100
            print("Good choice!")
        elif class_selected == "palladin":
            strength = 10
            defense = 20
            health = 125
            print("Excellent idea!")
        elif class_selected == "mage":
            strength = 25
            defense = 15
            health = 90
            print("Wise decision!")
        else:
            print("Invalid choice. Please choose again.")

        break
    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)

def start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    print("You are in a dark, damp room.")
    print("There are three doors in front of you. One is red, one is blue, and one is green.")
    print("Which door do you choose? (red/blue/green)")

    while True:
        choice = input("Red, Blue, or Green: ").lower()
        if choice == "red":
            red_room(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
            break
        elif choice == "blue":
            blue_room(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
            break
        elif choice == "green":
            green_room(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
            break
        else:
            print("Invalid choice. Please choose again.")

def red_room(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):

    rand_seed = random.randint(0, 2)
    
    if rand_seed == 0:
        input("As you enter the room, you feel the heat of many flames in the room.")
        input("There is a shard on a table in the middle of the room.")

        while True:
            choice = input("What will you do? (take shard/leave)").lower()
            if choice == "take shard":
                input("You run through the flames, viciously burning.")
                print(f"Your health: {health - 8}")
                health = health -8
                input("As you take the magical shard, a ghostly voice whispers, 'You must find all 5 shards and return to the green room in order to escape this dungeon'.")
                shards += 1
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            elif choice == "leave":
                print("You decide to leave the room.")
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            else:
                print("Invalid choice. Please choose again.")
    if rand_seed == 1:
        print("Your skin fills with goosebumps as you enter the room, full of carcasses and human skulls.")
        print("A goblin, ears perked, hears the sound of you entering and looks directly at you.")
        gob_health = random.randint(40, 60)
        gob_defense = random.randint(5, 10)
        gob_attack = random.randint(20, 25)
        while True:
            choice = input("What will you do? (attack/run)").lower()
            if choice == "attack":
                attack_gob(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)  
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            elif choice == "run":
                input("The goblin throws a dagger as you leave the room, grazing your chest.")
                input(f"Your health: {health-5}")
                health = health - 5
                if health <= 0:
                    game_over()

                print("You decide to leave the room.")
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            else:
                print("Invalid choice. Please choose again.")

    if rand_seed == 2:
        print("The sound of bones rattling fills the room as you enter.")
        print("A skeleton, equipped with a bow, stands between you and a shard.")
        skel_health = random.randint(40, 60)
        skel_defense = random.randint(5, 10)
        skel_attack = random.randint(20, 25)
        while True:
            choice = input("What will you do? (attack/run)").lower()
            if choice == "attack":
                attack_skel(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)  
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                
                break
            elif choice == "run":
                input("The skeleton gets one last shot off as you leave the room.")
                input(f"Your health: {health-5}")
                health = health - 5
                if health <= 0:
                    game_over()

                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            else:
                print("Invalid choice. Please choose again.")

def blue_room(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    rand_seed = random.randint(0, 2)
    
    if rand_seed == 0:
        print("A buzzing sound echoes around the chambers of the dungeon.")
        print("An oversized dragonsfly, guards a shard.")
        gob_health = random.randint(40, 60)
        gob_defense = random.randint(5, 10)
        skel_attack = random.randint(20, 25)
        while True:
            choice = input("What will you do? (attack/run)").lower()
            if choice == "attack":
                attack_drag(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)  
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                
                break
            elif choice == "run":
                input("The dragonfly nearly hits your neck as you leave the room.")
                input(f"Your health: {health-5}")
                health = health - 5
                
                if health <= 0:
                    game_over()

                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            else:
                print("Invalid choice. Please choose again.")

    if rand_seed == 1:
        input("As you enter the room, you see the room is flooded, teeming with crocodiles. .")
        input("A shard, peculiarly placed, is sitting on afloating raft.")

        while True:
            choice = input("What will you do? (take shard/leave)").lower()
            if choice == "take shard":
                input("You swim through the waters, getting bit by many crocodiles.")
                print(f"Your health: {health - 8}")
                health = health -8
                if health <= 0:
                    game_over()

                shards += 1
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            elif choice == "leave":
                print("You decide to leave the room.")
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            else:
                print("Invalid choice. Please choose again.")

    if rand_seed == 2:
        print("'Welcome,' a phantomly voice whispers, 'This is the coin flip. If it lands on heads, you lose 8 health, if it lands on tails, you will gain a shard. Are you up for the task?")
        while True:
            choice = input("What will you do? (flip/leave)").lower()
            if choice == "flip":
                num = random.randint(0, 1)
                if num == 0:
                    input("Heads")
                    print("You lost 8 health.")
                    health = health - 8
                    input(f"Your health: {health}.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break
                elif num == 1:
                    input("Tails!")
                    print("You gained a shard!")
                    shards += 1
                    input(f"Your shards: {shards}.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break
            elif choice == "leave":
                print("You decide to leave the room.")
                start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                break
            else:
                print("Invalid choice. Please choose again.")
        

def green_room(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    if shards >= 5:
       pass
    else:
        input("The door doesn't open without 5 shards being placed in its lock.")
        start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)

    input(f"'So you have passed all of my tests, I guess I must let you out at this time. Goodbye {class_selected}.'")
    input("As you leave the cursed dungeon, your memory becomes hazy, your eyes blurry, and your head dizzy.")
    input("You wake up in your room, woken up in cold sweat.")
    input("Was it a dream all along?.")
    game_win()

def attack_gob(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    
    if class_selected == "warrior":
        while True:
            input("You land a deadly blow with your sword!")
            print(f"{strength-gob_defense} damage!")
            input(f"The goblin, enraged, claws at you nearly missing your face!")
            print(f"{gob_attack-defense} damage!")

            health = health - (gob_attack-defense)
            gob_health = gob_health - (strength-gob_defense)

            if health <= 0:
                game_over()
                break

            if gob_health <= 0:
                print("Good job, you killed the goblin and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The Goblin's health: {gob_health}")

            
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break
                elif choice == "run":
                    input("The goblin throws a dagger as you leave the room, grazing your chest.")
                    input(f"Your health: {health-5}")
                    health = health - 5
                    print("You decide to leave the room.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break
                    
                else:
                    print("Invalid choice. Please choose again.")
                    
            

    if class_selected == "mage":
        while True:    
            input("You cast a giant fireball at the goblin!")
            print(f"{strength-gob_defense} damage!")
            input(f"The goblin, enraged, claws at you nearly missing your face!")
            print(f"{gob_attack-defense} damage!")

            health = health - (gob_attack-defense)
            gob_health = gob_health - (strength-gob_defense)

            if health <= 0:
                game_over()
                break

            if gob_health <= 0:
                print("Good job, you killed the goblin and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The Goblin's health: {gob_health}")

            
            while True:    
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break
                elif choice == "run":
                    input("The goblin throws a dagger as you leave the room, grazing your chest.")
                    input(f"Your health: {health-5}")
                    health = health - 5
                    print("You decide to leave the room.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break
                else:
                    print("Invalid choice. Please choose again.")
            
                
    
    if class_selected == "palldin":
        while True:
            input("You land a deadly blow with your hammer!")
            print(f"{strength-gob_defense} damage!")
            input(f"The goblin, enraged, claws at you nearly missing your face!")
            print(f"{gob_attack-defense} damage!")

            health = health - (gob_attack-defense)
            gob_health = gob_health - (strength-gob_defense)

            if health <= 0:
                game_over()
                break

            if gob_health <= 0:
                print("Good job, you killed the goblin and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The Goblin's health: {gob_health}")

            
            while True: 
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break
                elif choice == "run":
                    input("The goblin throws a dagger as you leave the room, grazing your chest.")
                    input(f"Your health: {health-5}")
                    health = health - 5
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break
                else:
                    print("Invalid choice. Please choose again.")

            
        
                    

def attack_skel(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    
    if class_selected == "warrior":
        while True:
            input("You run over to the skeleton!")
            
            input(f"The skeleton, shooting with perfect precision, hits your shoulder!")
            print(f"{skel_attack-defense} damage!")

            health = health - (skel_attack-defense)
            

            if health <= 0:
                game_over()
                break

            
            print(f"Your health: {health}")
            print(f"The Skeleton's health: {skel_health}")

            
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    input("You land a devastating blow the skeleton!")
                    print(f"{strength - skel_defense} damage!")
                    skel_health = skel_health - (skel_defense - strength) 
                    input(f"The skeleton, shooting with perfect precision, hits your shoulder!")
                    print(f"{skel_attack-defense} damage!")

                    health = health - (skel_attack-defense)
                    
                    if health <= 0:
                        game_over()
                        break
                    if skel_health <= 0:
                        print("Good job, you killed the skeleton and received 1 shard!")
                        shards = shards + 1
                        break
                    break
                elif choice == "run":
                    input("The skeleton gets one last shot off as you leave the room.")
                    input(f"Your health: {health-5}")
                    health = health - 5
                    
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break
                else:
                    print("Invalid choice. Please choose again.")

            
        
            
    if class_selected == "mage":
        while True:
            input("You cast an ice spell at the skeleton!")
            print(f"{strength-skel_defense} damage!")
            input(f"The skeleton, shooting with perfect precision, hits your shoulder!")
            print(f"{skel_attack-defense} damage!")
            skel_health = skel_health - (strength - skel_defense)
            health = health - (skel_attack-defense)
            

            if health <= 0:
                game_over()
                break
            if skel_health <= 0:
                print("Good job, you killed the skeleton and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The Skeleton's health: {skel_health}")
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break

                elif choice == "run":
                    input("The skeleton gets one last shot off as you leave the room.")
                    input(f"Your health: {health-5}")
                    health = health - 5
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break

                else:
                    print("Invalid choice. Please choose again.")
            
        
                    
                    
                    
                
    
    if class_selected == "palldin":
        while True:
            input("You run over to the skeleton!")
            
            input(f"The skeleton, shooting with perfect precision, hits your shoulder!")
            print(f"{skel_attack-defense} damage!")

            health = health - (skel_attack-defense)
            

            if health <= 0:
                game_over()
                break

            
            print(f"Your health: {health}")
            print(f"The Skeleton's health: {skel_health}")
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    input("You land a devastating blow the skeleton!")
                
                    input(f"The skeleton, shooting with perfect precision, hits your shoulder!")
                    print(f"{skel_attack-defense} damage!")

                    health = health - (skel_attack-defense)
                    if health <= 0:
                        game_over()
                        break
                    if skel_health <= 0:
                        print("Good job, you killed the skeleton and received 1 shard!")
                        shards = shards + 1
                        break

                elif choice == "run":
                    input("The skeleton gets one last shot off as you leave the room.")
                    input(f"Your health: {health-5}")
                    health = health - 5
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break

def attack_drag(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack):
    
    if class_selected == "warrior":
        while True:
            input("You tear through the insect with your sword!")
            print(f"{strength-gob_defense} damage!")
            input(f"The dragonfly, buzzing around you, spits a venomous liquid at your chest!")
            print(f"{defense - gob_attack} damage!")

            health = health + (defense - gob_attack)
            gob_health = gob_health - (strength-gob_defense)

            if health <= 0:
                game_over()
                break

            if gob_health <= 0:
                print("Good job, you killed the dragonfly and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The dragonfly's health: {gob_health}")

            
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break
                elif choice == "run":
                    input("The dragonfly flys towards you, just before you leave the room.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break

                else:
                    print("Invalid choice. Please choose again.")
            
                   
            

    if class_selected == "mage":
        while True:
            input("You cast a fierce ice bolt against the dragonfly!")
            print(f"{strength-gob_defense} damage!")
            input(f"The dragonfly, buzzing around you, spits a venomous liquid at your chest!")
            print(f"{defense - gob_attack} damage!")

            health = health + (defense - gob_attack)
            gob_health = gob_health - (strength-gob_defense)

            if health <= 0:
                game_over()
                break

            if gob_health <= 0:
                print("Good job, you killed the dragonfly and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The dragonfly's health: {gob_health}")

            
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break
                elif choice == "run":
                    input("The dragonfly flys towards you, just before you leave the room.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break

                else:
                    print("Invalid choice. Please choose again.")
            
           
            
                
    
    if class_selected == "palladin":
        while True:
            input("You smash the insect with your hammer!")
            print(f"{strength-gob_defense} damage!")
            input(f"The dragonfly, buzzing around you, spits a venomous liquid at your chest!")
            print(f"{defense - gob_attack} damage!")

            health = health + (defense - gob_attack)
            gob_health = gob_health - (strength-gob_defense)

            if health <= 0:
                game_over()
                break

            if gob_health <= 0:
                print("Good job, you killed the dragonfly and received 1 shard!")
                shards = shards + 1
                break
            
            print(f"Your health: {health}")
            print(f"The dragonfly's health: {gob_health}")

            
            while True:
                choice = input("What will you do? (attack/run)").lower()
                if choice == "attack":
                    break
                elif choice == "run":
                    input("The dragonfly flys towards you, just before you leave the room.")
                    start_game(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)
                    break

                else:
                    print("Invalid choice. Please choose again.")
            
           
                    
def game_over():
    print("You Died! Game Over!")

def game_win():
    print("Good Job! You escaped the dungeon!")
    print("Thank you for playing!")

select_class(health, class_selected, gob_attack, gob_defense, strength, defense, shards, gob_health, skel_defense, skel_health, skel_attack)