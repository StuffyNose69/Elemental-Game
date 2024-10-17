import time
import os

from misc import colors

color = colors.bcolors
sleep = time.sleep
def clear():
  os.system("cls")

def earthFactionStartPrint(hp, mobility, energy):
  print("     ╔═════════════════════════╗     ")
  print("╔════╣      EARTH FACTION      ╠════╗")
  print("╠════╩═════════════════════════╩════╣")
  print("║    Members of the Earth faction   ║")
  print("║    have the ability to control    ║")
  print("║    both the land and the air.     ║")
  print("║    This makes members of the      ║")
  print("║    Earth faction incredibly       ║")
  print("║    versatile fighters.            ║")
  print("╠═══════════════════════════════════╣")
  print("║           STAT CHANGES:           ║")
  print(f"║         HP: {hp} ===> {hp + 25}          ║")
  print(f"║         MOB: {mobility} ===> {mobility + 5}           ║")
  print(f"║         ENG: {energy} ===> {energy - 5}           ║")
  print("╚═══════════════════════════════════╝\n")

def waterFactionStartPrint(hp, intelligence, strength):
  print("     ╔═════════════════════════╗     ")
  print("╔════╣      WATER FACTION      ╠════╗")
  print("╠════╩═════════════════════════╩════╣")
  print("║    Members of the Water faction   ║")
  print("║    have the ability to control    ║")
  print("║    any and all forms of liquid.   ║")
  print("║    They are highly intelligent    ║")
  print("║    and have great healing         ║")
  print("║    ability, but that doesn't      ║")
  print("║    mean they are pacifists.       ║")
  print("╠═══════════════════════════════════╣")
  print("║           STAT CHANGES:           ║")
  print(f"║         HP: {hp} ===> {hp + 25}          ║")
  print(f"║         INT: {intelligence} ===> {intelligence + 5}           ║")
  print(f"║         STR: {strength} ===> {strength - 5}           ║")
  print("╚═══════════════════════════════════╝\n")

def flameFactionStartPrint(strength, mobility, intelligence):
  print("     ╔═════════════════════════╗     ")
  print("╔════╣      FLAME FACTION      ╠════╗")
  print("╠════╩═════════════════════════╩════╣")
  print("║    The fiery Flame faction are    ║")
  print("║    a very proud people. They      ║")
  print("║    possess immense physical       ║")
  print("║    prowess, being able to move    ║")
  print("║    quickly and land highly        ║")
  print("║    damaging physical blows.       ║")
  print("║    They are, however, described   ║")
  print("║    by the other factions as,      ║")
  print("║    quote, 'very dumb'.            ║")
  print("╠═══════════════════════════════════╣")
  print("║           STAT CHANGES:           ║")
  print(f"║         STR: {strength} ===> {strength + 5}           ║")
  print(f"║         MOB: {mobility} ===> {mobility + 5}           ║")
  print(f"║         INT: {intelligence} ===> {intelligence - 5}           ║")
  print("╚═══════════════════════════════════╝\n")

def electricFactionStartPrint(energy, mobility, hp):
  print("     ╔═════════════════════════╗     ")
  print("╔════╣     ELECTRIC FACTION    ╠════╗")
  print("╠════╩═════════════════════════╩════╣")
  print("║    Electric faction members are   ║")
  print("║    known and feared thoughout     ║")
  print("║    the land as fierce, energetic  ║")
  print("║    fighters that never seem to    ║")
  print("║    lose pace and can strike       ║")
  print("║    fear into their enemies with   ║")
  print("║    incrediblely flashy attacks.   ║")
  print("║    They are, however, quite       ║")
  print("║    mortal.                        ║")
  print("╠═══════════════════════════════════╣")
  print("║           STAT CHANGES:           ║")
  print(f"║         ENG: {energy} ===> {energy + 5}           ║")
  print(f"║         MOB: {mobility} ===> {mobility + 5}           ║")
  print(f"║         HP: {hp} ===> {hp - 25}           ║")
  print("╚═══════════════════════════════════╝\n")

def prismFactionStartPrint(energy, strength, hp):
  print("     ╔═════════════════════════╗     ")
  print("╔════╣      PRISM FACTION      ╠════╗")
  print("╠════╩═════════════════════════╩════╣")
  print("║    Prism faction members are      ║")
  print("║    perfectly content to wait in   ║")
  print("║    the shadows for a perfect      ║")
  print("║    moment to strike. They         ║")
  print("║    manipulate both light and      ║")
  print("║    dark energy to win their       ║")
  print("║    fights. Watch where you step,  ║")
  print("║    or they might end up watching  ║")
  print("║    it for you.                    ║")
  print("╠═══════════════════════════════════╣")
  print("║           STAT CHANGES:           ║")
  print(f"║         ENG: {energy} ===> {energy + 5}           ║")
  print(f"║         STR: {strength} ===> {strength + 5}           ║")
  print(f"║         HP: {hp} ===> {hp - 25}           ║")
  print("╚═══════════════════════════════════╝\n")

def mainMenu():
  print("        ╔═══════════════════╗        ")
  print("        ║     MAIN MENU     ║        ")
  print("╔═══════╩═══════════════════╩═══════╗")
  print("║   1: BATTLE       2: SKILL TREE   ║")
  print("║   3: YOUR STATS   4: GAME INFO    ║")
  print("╠═══════════════════════════════════╣")
  print("║    SELECT AN OPTION FROM ABOVE:   ║")
  print("╚═══════════════════════════════════╝\n")

def BaseXPBarDisplay(xp, xplvl, xpl, xpbar):
  if len(str(xplvl)) == 1:
    xpformat = "  "
  if len(str(xplvl)) >= 2:
    xpformat = " "
  print(f"XP GAINED: {color.green}{xp}{color.end}")
  print(f"XP LEVEL: {color.green}{xplvl}{color.end}")
  print(f"XP LEFT UNTIL NEXT LEVEL: {color.green}{xpl - xp}{color.end}")
  print(f"\nXP BAR:\n  ╔═══════════════════════╗  \n{color.bold}{xplvl}{color.end}:{xpformat}{color.lightgreen}{xpbar}{color.end}   :{color.bold}{xplvl + 1}{color.end}\n  ╚═══════════════════════╝  \n")

def ElementXPBarDisplay(xp, xplvl, xpl, xpbar):
  if len(str(xplvl)) == 1:
    xpformat = "  "
  if len(str(xplvl)) >= 2:
    xpformat = " "
  print(f"XP GAINED: {color.pink}{xp}{color.end}")
  print(f"XP LEVEL: {color.pink}{xplvl}{color.end}")
  print(f"XP LEFT UNTIL NEXT LEVEL: {color.pink}{xpl - xp}{color.end}")
  print(f"\nXP BAR:\n  ╔═══════════════════════╗  \n{color.bold}{xplvl}{color.end}:{xpformat}{color.pink}{xpbar}{color.end}   :{color.bold}{xplvl + 1}{color.end}\n  ╚═══════════════════════╝  \n")