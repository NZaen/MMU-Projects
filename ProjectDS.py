import time
import os
import random



#All bonfires
Death = 0
bonfire1 = False
bonfire1 = False
bonfire1 = False

#All Weapons
IronSword = False

#Base Character Stats
p_Damage = int(10)
p_Stamina= int(10)
p_Health = int(100)
p_Souls = int(0)
p_Level = int(1)
p_Name = "Zaen"
p_FullHealth = int(100)

#Death Script
def Dead1():
  global p_Health
  if (p_Health <= 0):
    time.sleep(1)
    print("""
 ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝
    """)
    time.sleep(2)
    print("You respawned at the nearest bonfire. The only way to to now is to reconquer the forces you've beaten")
    time.sleep(2)
    p_Health = p_FullHealth
    asylum2()

    
#weapon damages
d_Fist = p_Damage
d_IronSword = (p_Damage + 30)\

#enemy stats
fh_GiantDemon = int(300)
h_GiantDemon = int(300)
d_GiantDemon = int(60)



#Title Screen
def v_title():
  print("""
 ____  _____   ___     __ _________________  ____   ____
 |  _ \|  _ \ / _ \    | | ____/ ___|_   _| |  _ \/ ___| 
 | |_) | |_) | | | |_  | |  _|| |     | |   | | | \___ \ 
 |  __/|  _ <| |_| | |_| | |__| |___  | |   | |_| |___) |
 |_|   |_| \_\\___/ \____/|_____\____| |_|   |____/|____ /                               
 1. Start Game
 2. Quit Game      
""")
  titlechoice = int(input(""))
  if (titlechoice == 1):
      jail_scene()
  elif (titlechoice == 2):
      exit()




#Inventory Script
inventory = []
def inv():
  print(inventory)
weapon = []
  
#Asylum 2 Turn 2 Script
def asylum2turn2():
  Dead1()
  global h_GiantDemon
  global p_Health
  as2t2 = int(input(f"""
            (((())                 |      
           ((()))))                |   The demon returns your blow with an attack. How would you like to respond?
         /(`   O  ')\     |  |     |   
         ' ... . ...`     |  |     |   
       '. .. . . . . .`   |  |     |  
     (  . . . . . ... . __| _|     |          1. Offensive dodge (High Risk, High Reward)
    / (  . . .  . . .  .  __|)     |          2. Defensive Dodge (Low Risk, Low Reward)
   / (  .   .. . . .    ).|_|      |          
  / ( .`---'. ..  .----'..)        |          
 ( /(____-------------____)        |         
  | (                     )        |        
  |  \                   /         |                 
 _|_   \   -_______-   /           |                
|/ \|    \           /             |                 
 ---      \    |    /              |             
           \___|___/               |              
            \  |  /                |            
            (/\|/\)                |
                                   |
      Giant Demon                  |                    Player
    Health : {h_GiantDemon}/{fh_GiantDemon}                             Health : {p_Health}/{p_FullHealth}
    """))
   
  if (as2t2 == 1 and random.randint(0,100) < 40):
     print("You managed to dodge the enemy's attack!")
     print(f"You dealt double {d_Fist} damage to the enemy")
     time.sleep(1)
     h_GiantDemon = (h_GiantDemon - (d_Fist * 2))  
     asylum2turn3()
  elif (as2t2 == 1 and random.randint(0,100) < 20):
     print("You managed to dodge the enemy's attack!")
     time.sleep(1)
     asylum2turn3()
  elif (as2t2 == 1 and random.randint(0,100) < 40):
    print("Your dodge fails and you recieves {d_GiantDemon} damage ")
    time.sleep(1)
    p_Health = (p_Health - d_GiantDemon)
    asylum2turn3()

  if (as2t2 == 2 and random.randint(0,100) < 80):
     print("You managed to dodge the enemy's attack!")  
     time.sleep(1)
     asylum2turn3()
  elif (as2t2 == 2 and random.randint(0,100) < 20):
    print(f"Your dodge fails and you recieve1 {d_GiantDemon} damage ")
    time.sleep(1)
    p_Health = (p_Health - d_GiantDemon)
    asylum2turn3()



#Asylum 2 Turn 3 Script
def asylum2turn3():
  Dead1()
  global h_GiantDemon
  global p_Health
  as2t3 = int(input(f"""
            (((())                 |      
           ((()))))                |   The demon's attack leaves him vulnerable for an attack. What do you do?
       '. .. . . . . .`   |  |     |  
     (  . . . . . ... . __| _|     |          1. Fight it
    / (  . . .  . . .  .  __|)     |          2. Try to find a way past it
   / (  .   .. . . .    ).|_|      |          3. Run back
  / ( .`---'. ..  .----'..)        |          
 ( /(____-------------____)        |         
  | (                     )        |        
  |  \                   /         |                 
 _|_   \   -_______-   /           |                
|/ \|    \           /                              
 ---      \    |    /              |             
           \___|___/                             
            \  |  /                |            
            (/\|/\)                |
                                   |
      Giant Demon                  |                    Player
    Health : {h_GiantDemon}/{fh_GiantDemon}                             Health : {p_Health}/{p_FullHealth}
          
    """))
  if (as2t3 == 1):
    as2t21 = int(input("""Using which weapon?
    1. Fists
    """))
    if (as2t21 == 1):
      print(f"You dealt {d_Fist} damage to the enemy")
      time.sleep(1)
      h_GiantDemon = (h_GiantDemon - d_Fist)   
      asylum2turn2()
      
      
  elif (as2t3 == 2):
    print("You find a small doorway towards the far left of the area. With a bit of luck, you manage to dodge")  

  elif (as2t3 == 3):
    print("You try your hardest to run back,  but you find that the door is sealed shut. When you look back, the demon swings a terrifying blow right into your face ")
    print(f"You recieve {d_GiantDemon} damage ")
    time.sleep(1)
    p_Health = (p_Health - d_GiantDemon)
    asylum2turn2()


#Asylum 2 Turn 1 script
def asylum2():
  Dead1()
  print("""
You open the huge door with ease. On the other side of the door is a huge, rectangular room with a grand brick roof. The place seemed old and abandoned by the damage dealt to the walls and  dust covering the floors.
Suddenly, a huge monster falls down from the roof. You manage to avoid the crumbling of the ceiling 1but the creature awaits your fight """)
  global h_GiantDemon
  global p_Health
  
  as2 = int(input(f"""
            (((())                 |      
           ((()))))                |   The demon slowly approaches you and unsheathes
           | -   - |       /\      |   his blade and mace from his side. The ends of the old 
         /(`   O  ')\     |  |     |   sword seems blunt, but the sheer force of it
         ' ... . ...`     |  |     |   would send you flying back. What do you do?
       '. .. . . . . .`   |  |     |  
     (  . . . . . ... . __| _|     |          1. Fight it
    / (  . . .  . . .  .  __|)     |          
   / (  .   .. . . .    ).|_|      |          3. Run back
  / ( .`---'. ..  .----'..)        |          
 ( /(____-------------____)        |         
  | (                     )        |        
  |  \                   /         |                 
 _|_   \   -_______-   /           |                
|/ \|    \           /                              
 ---      \    |    /              |             
           \___|___/                             
            \  |  /                |            
            (/\|/\)                |
                                   |
      Giant Demon                  |                    Player
    Health : {h_GiantDemon}/{fh_GiantDemon}                             Health : {p_Health}/{p_FullHealth}
          
    """))
  if (as2 == 1):
    as21 = int(input("""Using which weapon?
    1. Fists
    """))
    if (as21 == 1):
      print(f"You dealt {d_Fist} damage to the enemy")
      time.sleep(1)
      h_GiantDemon = (fh_GiantDemon - d_Fist)   
      asylum2turn2()
      
  elif (as2 == 2):
    print("You find a small doorway towards the far left of the area. With a bit of luck, you manage to dodge") 
   
   

  elif (as2 == 3):
    print("You try your hardest to run back,  but you find that the door is sealed shut. When you look back, the demon swings a terrifying blow right into your face ")
    print(f"You recieve {d_GiantDemon} damage ")
    time.sleep(1)
    p_Health = (p_FullHealth - d_GiantDemon)
    asylum2turn2()

#Jail Scene 
def jail_scene():
  jail1 = int(input("""-----------------------------------------------------------------------------
You awake in a jail cell with nothing but a small hole at the ceiling, a tease of the rich sunlight and freedom of the outside. Confused, you try to recall what brought you here but nothing comes to mind. 
1. Tug at the door to see if it can be opened
2. Sit back and wait for help

\n"""))
  if (jail1 == 1):
    print ("""--------------------------------------------------------------------
You slam endlessly at the door, but it doesn't even budge.  With all hope lost,   you decide to wait out your days. If the rats don't get you first, starvation will do the rest. Suddenly a mysterious armored man drops a key from the small hole. Relieved, you quickly go for the key to unlock the door

Jail key Obtained!

\n""")
    
    inventory.append("Rusted Door Key")
    
  else:
    print("""----------------------------------------------------------------------
With all hope lost, you decide to wait out your days. If the rats don't get you first, starvation will do the rest. Suddenly, you hear footsteps approaching nearby, only it came from upstairs. From the hole, you see a mysterious armored man kneeling down and dropping a key from the small hole. Relieved, you quickly go for the key to unlock the door

Jail Key Obtained!
 
\n""")
    inventory.append("Rusted Door Key")
    


def asylum1():
  as1 = int(input("""-----------------------------------------------------------------------------
Beyond the door was a long corridor filled with multiple cells filled with not other prisoners but rather, the undead. As you pass each door, the undead slammed the doors loudly, alerting all of them towards your presense. 

However loud and angry they are, their cells prevented them from getting to you.
As such, you walk past them to the other end with ease. Finally, you find a ladder with an obvious exit to the outside. 

The climb up was a long and tiring one. Yet, you finally arrive to the comfort of sunlight. You find yourself in a courtyard with a huge door on the opposite side. In the middle, interestingly, was a bonfire. 

1. Approach the bonfire
2. Head straight to the big door

\n"""))
  if (as1 == 1):
    print("""----------------------------------------------------------------------------
You feel an odd comfort as you get closer to the bonfire. You decide to it up. Its fires brightens into a great, beautiful flame. 


██████╗  ██████╗ ███╗   ██╗███████╗██╗██████╗ ███████╗    ██╗  ██╗██╗███╗   ██╗██████╗ ██╗     ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗  ██║██╔════╝██║██╔══██╗██╔════╝    ██║ ██╔╝██║████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗
██████╔╝██║   ██║██╔██╗ ██║█████╗  ██║██████╔╝█████╗      █████╔╝ ██║██╔██╗ ██║██║  ██║██║     █████╗  ██║  ██║
██╔══██╗██║   ██║██║╚██╗██║██╔══╝  ██║██╔══██╗██╔══╝      ██╔═██╗ ██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██║  ██║
██████╔╝╚██████╔╝██║ ╚████║██║     ██║██║  ██║███████╗    ██║  ██╗██║██║ ╚████║██████╔╝███████╗███████╗██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═════╝ 

    """)
    time.sleep(2)
    print("After a while, you finally decide to enter the door")

    global bonfire1
    bonfire1 = True
    
    asylum2()
  else:
    asylum2()
 



  #bonfire1()
    
    
 
    
    




#Stats Screen
def stats():
  print(f"""          
       ________         
      /  ______|                   |    
      |  |_' \'|                    |   Knight {p_Name}
      (   _) -`|                   |   
       \ '-.-- /                   |    With your memory lost, you now travel the
 ______/`--'--<                    |    world seeking answers that may not exist.
 |    |`-.  ,;/``--._              |    Will you be the brave hero who overcame
 |    |-. _///     ,'`\            |    their challenges, or be the one forgotten
 |    |`-Y;'/     /  ,-'\          |    by time?
 |    | // <_    / ,'  ,-'\        |     
 '----'// -- `-./,' ,-'  \/        |    Health  : {p_Health}
  |   //[==]     \,' \_.,-\        |    Stamina : {p_Stamina}
  |  //      `  -- | \__.,-'       |    Souls   : {p_Souls}
    // -[==]_      |   ____\       |    Level   : {p_Level}
   //          `-- |--' |   \      |    Damage  : {p_Damage}        
       ___...____/                 | 
            """)


#death script 


#Game Launch
v_title()
asylum1()









  




