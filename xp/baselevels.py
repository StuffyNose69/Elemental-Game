class lvl0:
    skillTreeTokens = 0 #points given at this level to spend on base skill tree
    newEnemy = "" # enemy unlocked at this level
    enemyToRemove = "" # remove an enemy from the list at this level
    maxXP = 100 # xp amount needed to get past this level

class lvl1:
    skillTreeTokens = 2
    newEnemy = "Undead Lurker"
    enemyToRemove = ""
    maxXP = 100

class lvl2:
    skillTreeTokens = 1
    newEnemy = "Zombie Soldier"
    enemyToRemove = ""
    maxXP = 100

class lvl3:
    skillTreeTokens = 1
    newEnemy = "Skeleton Soldier"
    enemyToRemove = ""
    maxXP = 150

class lvl4:
    skillTreeTokens = 1
    newEnemy = ""
    enemyToRemove = "Undead Grunt"
    maxXP = 150

class lvl5:
    skillTreeTokens = 2
    newEnemy = "Reinforced Undead"
    enemyToRemove = ""
    maxXP = 150

class lvl6:
    skillTreeTokens = 1
    newEnemy = ""
    enemyToRemove = ""
    maxXP = 150

class lvl7:
    skillTreeTokens = 1
    newEnemy = "Haunted Soul"
    enemyToRemove = ""
    maxXP = 200

class lvl8:
    skillTreeTokens = 1
    newEnemy = ""
    enemyToRemove = "Undead Lurker"
    maxXP = 200

class lvl9:
    skillTreeTokens = 1
    newEnemy = ""
    enemyToRemove = ""
    maxXP = 200

class lvl10:
    skillTreeTokens = 2
    newEnemy = "Shadow Assassin"
    maxXP = 200

levelcall = {
    "lvl0": lvl0,
    "lvl1": lvl1,
    "lvl2": lvl2,
    "lvl3": lvl3,
    "lvl4": lvl4,
    "lvl5": lvl5,
    "lvl6": lvl6,
    "lvl7": lvl7,
    "lvl8": lvl8,
    "lvl9": lvl9,
    "lvl10": lvl10,
}