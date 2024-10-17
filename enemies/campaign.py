import random

class UndeadGrunt:
    enemyFaction = "Earth"
    enemyDmg = 15
    enemyHP = 75
    enemyActions = ["Punch"]
    enemyMinXP = 20
    enemyMaxXp = 40
    elementalXP = 2

class UndeadLurker:
    enemyFaction = "Earth"
    enemyDmg = 20
    enemyHP = 100
    enemyActions = ["Punch", "Bone Throw", "Rot"]
    enemyMinXP = 20
    enemyMaxXp = 40
    elementalXP = 2

class ZombieSoldier:
    enemyFaction = "Earth"
    enemyDmg = 20
    enemyHP = 150
    enemyActions = ["Punch", "Slash", "Rot"]
    enemyMinXP = 25
    enemyMaxXp = 50
    elementalXP = 4

class SkeletonSoldier:
    enemyFaction = "Earth"
    enemyDmg = 35
    enemyHP = 100
    enemyActions = ["Punch", "Bone Throw", "Snipe"]
    enemyMinXP = 25
    enemyMaxXp = 50
    elementalXP = 5

class ReinforcedUndead:
    enemyFaction = "Earth"
    enemyDmg = 20
    enemyHP = 175
    enemyActions = ["Punch", "Reinforce"]
    enemyMinXP = 20
    enemyMaxXp = 40
    elementalXP = 5

class HauntedSoul:
    enemyFaction = "Prism"
    enemyDmg = 60
    enemyHP = 75
    enemyActions = ["Scream", "Haunt", "Fracture"]
    enemyMinXP = 25
    enemyMaxXp = 50
    elementalXP = 5

class ShadowAssassin:
    enemyFaction = "Prism"
    enemyDmg = 50
    enemyHP = 250
    enemyActions = ["Punch", "Slash", "Fracture", "Shadows Fury"]
    enemyMinXP = 50
    enemyMaxXp = 100
    elementalXP = 10

enemycall = {
    "Undead Grunt": UndeadGrunt,
    "Undead Lurker": UndeadLurker,
    "Zombie Soldier": ZombieSoldier,
    "Skeleton Soldier": SkeletonSoldier,
    "Reinforced Undead": ReinforcedUndead,
    "Haunted Soul": HauntedSoul,
    "Shadow Assassin": ShadowAssassin,
}