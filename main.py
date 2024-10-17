import random
import time
import os

# file paths for imports: from [folder].[file] import [variable or file]
from misc import colors, prints
from attacks.physical import physicalcall
from attacks.elemental import earthcall, watercall, flamecall, electriccall, prismcall
from attacks.eattacks import eattackcall
from gamemodes import battle, faction_information
from enemies import campaign
from xp import baselevels, elementlevels

color = colors.bcolors
sleep = time.sleep
def clear():
  os.system("cls")

clear()

hp = 100  # health, no abbr
strength = 20  # physical damage, abbr: str
stamina = 50  # physical stamina, abbr: stam/stamina
intelligence = 20  # elemental damage, abbr: int
energy = 25  # elemental stamina, abbr: eng
mobility = 10  # dodge, abbr: mob
poise = 10  # crit chance out of 100, no abbr
wisdom = 1.1  # crit damage, no abbr

basexp = 0
basexplvl = 0
elementxp = 0
elementxplvl = 0

tankLevel = 0
berserkLevel = 0
conditionLevel = 0

skillTreeTokens = 0

physicalActions = []
physicalActionsBank = []
elementActions = []
elementActionsBank = []

elementalCall = earthcall

admin = False

name = input("What is your name?: ")

factions = ["Earth", "Water", "Flame", "Electric", "Prism"]
faction = random.choice(factions)

clear()
print("You have been born into the...")
sleep(1.5)

if faction == "Earth":
  prints.earthFactionStartPrint(hp, mobility, energy)
  hp += 25
  mobility += 5
  energy -= 5
  elementalCall = earthcall
elif faction == "Water":
  prints.waterFactionStartPrint(hp, intelligence, strength)
  hp += 25
  intelligence += 5
  strength -= 5
  elementalCall = watercall
elif faction == "Flame":
  prints.flameFactionStartPrint(strength, mobility, intelligence)
  strength += 5
  mobility += 5
  intelligence -= 5
  elementalCall = flamecall
elif faction == "Electric":
  prints.electricFactionStartPrint(energy, mobility, hp)
  energy += 5
  mobility += 5
  hp -= 25
  elementalCall = electriccall
elif faction == "Prism":
  prints.prismFactionStartPrint(energy, strength, hp)
  energy += 5
  strength += 5
  hp -= 25
  elementalCall = prismcall

physicalActions.append("Quick Jab - Costs 5 Stamina")
physicalActionsBank.append("Quick Jab")

maxhp = hp
maxstr = strength
maxstam = stamina
maxenergy = energy
maxintel = intelligence

enemylist = ["Undead Grunt"]

while True:

  if len(str(basexplvl)) == 1:
    if len(str(basexplvl + 1)) == 2:
      xpupspace = "                                  "
    else:
      xpupspace = "                                   "
  if len(str(basexplvl)) == 2:
    xpupspace = "                                 "

  def BaseXPLvlUp():
    print("╔══════════════════════════════════════════╗")
    print(f"║  {color.green}Base XP Level Upgrade{color.end}                   ║")
    print(f"║  {color.green}{basexplvl} » {basexplvl + 1}{color.end}{xpupspace}║")
    print("╚══════════════════════════════════════════╝\n")

  xpLevelID = f"lvl{basexplvl}"
  x = baselevels.levelcall[xpLevelID]

  if basexp >= x.maxXP:
    BaseXPLvlUp()
    basexplvl += 1
    basexp = 0
    nx = baselevels.levelcall[f"lvl{basexplvl}"]
    skillTreeTokens += nx.skillTreeTokens
    if nx.newEnemy == "":
      continue
    else:
      enemylist.append(nx.newEnemy)
    if nx.enemyToRemove == "":
      continue
    else:
      enemylist.remove(nx.enemyToRemove)
    if nx.skillTreeTokens > 0:
      print(f"You have gained {nx.skillTreeTokens} Skill Tree Tokens for a new total of {skillTreeTokens}! You can use these tokens by inputting '2' in the main menu.\n")

  x = baselevels.levelcall[f"lvl{basexplvl}"]
  xpl = x.maxXP

  if basexp < (xpl * .1):
    basexpbar = "█                   "
  if basexp >= (xpl * .1):
    basexpbar = "███                 "
  if basexp >= (xpl * .2):
    basexpbar = "█████               "
  if basexp >= (xpl * .25):
    basexpbar = "██████              "
  if basexp >= (xpl * .3):
    basexpbar = "███████             "
  if basexp >= (xpl * .4):
    basexpbar = "█████████           "
  if basexp >= (xpl * .5):
    basexpbar = "███████████         "
  if basexp >= (xpl * .6):
    basexpbar = "█████████████       "
  if basexp >= (xpl * .7):
    basexpbar = "███████████████     "
  if basexp >= (xpl * .75):
    basexpbar = "████████████████    "
  if basexp >= (xpl * .8):
    basexpbar = "█████████████████   "
  if basexp >= (xpl * .9):
    basexpbar = "███████████████████ "

  if len(str(elementxplvl)) == 1:
    if len(str(elementxplvl + 1)) == 2:
      expupspace = "                                  "
    else:
      expupspace = "                                   "
  if len(str(elementxplvl)) == 2:
    expupspace = "                                 "

  def ElementalXPLvlUp():
    print("╔══════════════════════════════════════════╗")
    print(f"║  {color.pink}Elemental XP Level Upgrade{color.end}              ║")
    print(f"║  {color.pink}{elementxplvl} » {elementxplvl + 1}{color.end}{expupspace}║")
    print("╚══════════════════════════════════════════╝\n")

  expLevelID = f"lvl{elementxplvl}"
  ex = elementlevels.levelcall[expLevelID]

  if elementxp >= ex.maxXP:
    ElementalXPLvlUp()
    elementxplvl += 1
    elementxp = 0
    nex = elementlevels.levelcall[f"lvl{elementxplvl}"]
    maxenergy += nex.energyBuff
    maxintel += nex.intelBuff
    actionToAdd = nex.newAction(faction)
    if actionToAdd[0] == "":
      continue
    else:
      elementActionsBank.append(actionToAdd[0])
      elementActions.append(actionToAdd[1])

  ex = elementlevels.levelcall[f"lvl{elementxplvl}"]
  expl = ex.maxXP

  if elementxp < (expl * .1):
    elementxpbar = "█                   "
  if elementxp >= (expl * .1):
    elementxpbar = "███                 "
  if elementxp >= (expl * .2):
    elementxpbar = "█████               "
  if elementxp >= (expl * .25):
    elementxpbar = "██████              "
  if elementxp >= (expl * .3):
    elementxpbar = "███████             "
  if elementxp >= (expl * .4):
    elementxpbar = "█████████           "
  if elementxp >= (expl * .5):
    elementxpbar = "███████████         "
  if elementxp >= (expl * .6):
    elementxpbar = "█████████████       "
  if elementxp >= (expl * .7):
    elementxpbar = "███████████████     "
  if elementxp >= (expl * .75):
    elementxpbar = "████████████████    "
  if elementxp >= (expl * .8):
    elementxpbar = "█████████████████   "
  if elementxp >= (expl * .9):
    elementxpbar = "███████████████████ "

  prints.mainMenu()
  menu = input("")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  if menu == "1": # battle gamemode
    clear()
    battleInput = input("BATTLE TYPES:\n\n1: Campaign\n2: Arena\n\nSelect an option from above: ")
    if battleInput == "1": #campaign
      clear()

      hp = maxhp
      strength = maxstr
      stamina = maxstam
      energy = maxenergy
      intelligence = maxintel

      enemy = random.choice(enemylist)
      enemyAttributes = campaign.enemycall[enemy]

      ehp = enemyAttributes.enemyHP
      edmg = enemyAttributes.enemyDmg
      eattacks = enemyAttributes.enemyActions
      efaction = enemyAttributes.enemyFaction

      print(f"You enter battle with a(n) {enemy}.\n")

      sleep(1)

      battleEnabled = True
      
      while battleEnabled == True:
        print(f"Your HP: {hp}\nYour Stamina: {stamina}\nYour Energy: {energy}\n\nEnemy HP: {ehp}\nEnemy Strength: {edmg}\n")
        playerActionType = int(input("ACTION TYPES:\n\n1: Physical\n2: Elemental\n\nWhat type of action would you like to do?: "))

        if playerActionType == 1: # physical attack
          clear()
          print("Select from the below actions:\n")
          i = 1
          for action in physicalActions:
            print(f"{i}: {action}")
            i += 1
          action = int(input("\n"))
          clear()

          actionName = physicalActionsBank[action - 1]
          actionAttributes = physicalcall[actionName]

          hitRoll = random.randint(1, 100)
          if hitRoll > actionAttributes.hitchance:
            print("You attempt to attack the enemy, but you miss.\n")
          else:
            critd = 1
            critRoll = random.randint(1,100)
            if critRoll <= poise:
              print("You land a critical!\n")
              critd = wisdom
              sleep(1)

            if actionAttributes.actionType == "Attack":
              ehp -= (strength + actionAttributes.basedmg) * critd
              print(f"You deal {(strength + actionAttributes.basedmg) * critd} damage.")
            elif actionAttributes.actionType == "Heal":
              hp += (strength + actionAttributes.baseheal) * critd
              print(f"You heal for {(strength + actionAttributes.baseheal) * critd} hp.")
            elif actionAttributes.actionType == "Mixed":
              ehp -= (strength + actionAttributes.basedmg) * critd
              hp += (strength + actionAttributes.baseheal) * critd
              print(f"You deal {(strength + actionAttributes.basedmg) * critd} damage and heal for {(strength + actionAttributes.baseheal) * critd} hp.")
            else:
              continue # immplement later

        elif playerActionType == 2: # elemental attack
          clear()
          print("Select from the below actions:\n")
          i = 1
          for action in elementActions:
            print(f"{i}: {action}")
            i += 1
          action = int(input("\n"))
          clear()

          actionName = elementActionsBank[action - 1]
          actionAttributes = elementalCall[actionName]

          stamina -= actionAttributes.staminacost

          hitRoll = random.randint(1, 100)
          if hitRoll > actionAttributes.hitchance:
            print("You attempt to attack the enemy, but you miss.\n")
          else:
            critd = 1
            critRoll = random.randint(1,100)
            if critRoll <= poise:
              print("You land a critical!\n")
              critd = wisdom
              sleep(1)

            if actionAttributes.actionType == "Attack":
              ehp -= (intelligence + actionAttributes.basedmg) * critd
              print(f"You deal {(intelligence + actionAttributes.basedmg) * critd} damage.")
            elif actionAttributes.actionType == "Heal":
              hp += (intelligence + actionAttributes.baseheal) * critd
              print(f"You heal for {(intelligence + actionAttributes.baseheal) * critd} hp.")
            elif actionAttributes.actionType == "Mixed":
              ehp -= (intelligence + actionAttributes.basedmg) * critd
              hp += (intelligence + actionAttributes.baseheal) * critd
              print(f"You deal {(intelligence + actionAttributes.basedmg) * critd} damage and heal for {(intelligence + actionAttributes.baseheal) * critd} hp.")
            else:
              continue # immplement later

        sleep(1)
        
        if ehp <= 0:
          clear()
          print("You win!\n")
          gainedXP = random.randint(enemyAttributes.enemyMinXP, enemyAttributes.enemyMaxXp)
          basexp += gainedXP
          elementxp += enemyAttributes.elementalXP
          battleEnabled = False
          sleep(1)

        else:
          clear()

          eaction = random.choice(eattacks)
          actionAttributes = eattackcall[eaction]

          hitRoll = random.randint(1, 100)
          dodgeRoll = random.randint(1, 100)
          if hitRoll > actionAttributes.hitchance:
            if actionAttributes.actionType == "Attack" or actionAttributes.actionType == "Mixed":
              print("The enemy attempts to attack you, but they miss.\n")
            else:
              print("The enemy attempts to take action, but fails.\n")
          else:
            if dodgeRoll <= mobility:
              if actionAttributes.actionType == "Attack" or actionAttributes.actionType == "Mixed":
                print("The enemy attempts to attack you, but you dodge it.\n")
              else:
                print("The enemy attempts to take action, but you prevent it with your mobility.\n")
            else:

              if actionAttributes.actionType == "Attack":
                hp -= (edmg + actionAttributes.basedmg)
                print(f"Your enemy deals {(edmg + actionAttributes.basedmg)} damage.")
              elif actionAttributes.actionType == "Heal":
                ehp += (edmg + actionAttributes.baseheal)
                print(f"Your enemy heals for {(edmg + actionAttributes.baseheal)} hp.")
              elif actionAttributes.actionType == "Mixed":
                hp -= (edmg + actionAttributes.basedmg)
                ehp += (edmg + actionAttributes.baseheal)
                print(f"Your enemy deals {(edmg + actionAttributes.basedmg)} damage and heals for {(edmg + actionAttributes.baseheal)} hp.")
              else:
                continue # immplement later
            
            sleep(1)
            clear()

    elif battleInput == "2":
      clear()
      arenaInput = input("ARENA TYPES:\n\n1: Duel\n2: Tournament\n\nSelect an option from above: ")
      clear()
      if arenaInput == "1": # arena duel
        firstnames = ["Geralt", "Fartass", "Yinlyn", "Tarco", "Yom", "Tobin", "Seanathon", "Tryfic", "Josh", "Tyler", "Jack", "Nate", "Ryln", "Kyng", "Jakub", "Elias", "Brynnon", "Lee", "Mikal", "Antemi", "Bo", "Joel", "Alforvonquavious", "Turken", "Hyatt", "Viktal", "Sigmagoon", "Byght", "Fallyn", "Daustin"]
        lastnames = ["Goofyahhlastname", "Emerson", "Leifern", "Axelstone", "Voughn", "Conah", "Systhertyto", "Jogoat", "Moulton", "Poitras", "Grysthorn", "Salisston", "Aquanil", "Borgetti", "Obama", "Thornton", "Beregton", "Stasi", "Strantion", "Freakens", "Lawford", "Arizonamangotea", "Washington", "Forgetti", "Eichel", "Rose", "Whitterson", "Gigglesworth"]
        enemyFaction = random.choice(factions)
        enemyName = random.choice(firstnames) + " " + random.choice(lastnames)
        print(enemyName)


      elif arenaInput == "2":
        print("tourney (not coming soon lmao)\n")

      else:
        print("That is not an available option.\n")
    else:
      print("That is not an available option.\n")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  if menu == "2": # skill tree
    clear()
    print(f"1: Tank Level: {tankLevel}\nNext Upgrade: +15 HP\n\n2: Berserk Level: {berserkLevel}\nNext Upgrade: +5 STR AND +2 POISE AND +.1 WISDOM\n\n3: Condition Level: {conditionLevel}\nNext Upgrade: +5 STAM AND +2 MOB\n\nAvailable Skill Tree Tokens: {skillTreeTokens}.\n")
    treeInput = input("Select what branch you want to upgrade (all upgrades cost 1 token): ")
    clear()
    if skillTreeTokens == 0:
      print("You do not have enough Skill Tree Tokens to upgrade your skill tree.\n")
    else:
      skillTreeTokens -= 1
      if treeInput == "1":
        maxhp += 15
        tankLevel += 1
        print(f"Upgraded your TANK LEVEL to level {tankLevel}!\nUPGRADES:\nHP: {hp - 15} ===> {hp}\n")
      elif treeInput == "2":
        maxstr += 5
        poise += 2
        wisdom += .1
        wisdom = round(wisdom, 1)
        berserkLevel += 1
        print(f"Upgraded your BERSERK LEVEL to level {berserkLevel}!\nUPGRADES:\nSTR: {strength - 5} ===> {strength}\nPOISE: {poise - 2} ===> {poise}\nWISDOM: {wisdom - .1} ===> {wisdom}\n")
      elif treeInput == "3":
        maxstam += 5
        mobility += 2
        conditionLevel += 1
        print(f"Upgraded your CONDITION LEVEL to level {conditionLevel}!\nUPGRADES:\nSTAM: {stamina - 5} ===> {stamina}\nMOB: {mobility - 2} ===> {mobility}\n")
      else:
        print("That is not an available option. Your skill tree token has been refunded.\n")
        skillTreeTokens += 1

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  if menu == "3": # stat display
    clear()
    statsInput = input("1: Stats\n2: Base XP\n3: Elemental XP\n\nSelect an option from above: ")
    clear()
    if statsInput == "1": #base stats
      print(f"HP: {hp}\nSTRENGTH (STR): {strength}\nSTAMINA (STAM): {stamina}\nINTELLIGNECE (INT): {intelligence}\nENERGY (ENG): {energy}\nPOISE: {poise}\nWISDOM: {wisdom}\n\n")
    elif statsInput == "2": #base xp
      prints.BaseXPBarDisplay(basexp, basexplvl, xpl, basexpbar)
    elif statsInput == "3": #elemental xp
      prints.ElementXPBarDisplay(elementxp, elementxplvl, expl, elementxpbar)
    else:
      print("That is not an available option.\n")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  if menu == "4": # game info display
    clear()
    display = input("1: Game Information\n2: Credits\n3: Faction Information\n\nSelect what info you want to see: ")
    clear()
    if display == "1":
      print(f"GAME NAME: Elemental Battle Game\nGAME VERSION: v0.1.1 ALPHA\nPLAYER NAME: {name}\nFACTION: {faction}\nADMIN ENABLED: {admin}\n\n")
    if display == "2":
      print("This game was solo coded by Josh. This game takes inspiration from the following works:\n- Fire Force\n- Jujutsu Kaisen (the main inspiration)\n- Pokemon\n- Avatar: The Last Airbender\n")
      print("FOLLOW ME ON MY SOCIALS:\n- TWITTER: @StuffyNose69\n- YOUTUBE: @StuffyDev\n\n")
    if display == "3":
      faction_information.factionInfoScript()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------