import time
import os

sleep = time.sleep
def clear():
  os.system("cls")

def factionInfoScript():
  factionSelect = input("1: Earth\n2: Water\n3: Flame\n4: Electric\n5: Prism\n\nSelect what faction you want to see information on: ")
  clear()
  if factionSelect == "1": #earth
    print("EARTH FACTION:\n")
    sleep(1)
    # basic description
    print("Members of the Earth faction have the ability to control the land in many ways to their benefit. This makes members of the Earth faction incredibly versatile fighters.")
    sleep(1)
    # sub classes
    print("SUBCLASSES:\n- Air (50%)\n- Sand (20%)")
    sleep(1)
    # attacks
    print("")
  if factionSelect == "2": #water
    print("WATER FACTION:")
    sleep(1)
    print("Members of the Water faction have the ability to control any and all forms of liquid. They are highly intelligent and have great healing ability, but that doesn't mean they are pacifists.")
    sleep(1)
    print("SUBCLASSES:\n- Ice (50%)\n- Blood (10%)")
  if factionSelect == "3": #flame
    print("FLAME FACTION:")
    sleep(1)
    print("The fiery Flame faction are a very proud people. They possess immense physical prowess, being able to move quickly and land highly damaging physical blows. They are, however, described by the other factions as, quote, 'very dumb'.")
    sleep(1)
    print("SUBCLASSES:\n- Lava (25%)")
  if factionSelect == "4": #electric
    print("ELECTRIC FACTION:")
    sleep(1)
    print("Electric faction members are known and feared throughout the land as fierce, energetic fighters that never seem to lose pace and can strike fear into their enemies with incredibly flashy attacks. They are, however, quite mortal.")
    sleep(1)
    print("SUBCLASSES:\n- Plasma (50%)\n- Gamma (10%)")
  if factionSelect == "5": #prism
    print("PRISM FACTION:")
    sleep(1)
    print("Prism faction members are perfectly content to wait in the shadows for a perfect moment to strike. They manipulate both light and dark energy to win their fights. Watch where you step, or they might end up watching it for you.")
    sleep(1)
    print("SUBCLASSES:\nThe Prism faction has no subclasses, but in exchange, everyone in the faction has the ability to master both of the factions energies.")