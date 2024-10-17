class QuickJab:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 0
    baseheal = 0
    staminacost = 5
    hitchance = 95

class Uppercut:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 5
    baseheal = 0
    staminacost = 5
    hitchance = 85

class Blitz:  #guarentee hit no matter the defensive barriers or other defensive factors, only available past a certain mobility
    actionType = "Attack"
    actionElement = "None"
    basedmg = 5
    baseheal = 0
    staminacost = 20
    hitchance = 200

class BlackFlash:  #make hard to hit, but in turn replenish almost every stat
    actionType = "Mixed"
    actionElement = "None"
    basedmg = 10
    baseheal = 25
    staminacost = 33
    hitchance = 25

class RapidPunch:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 20
    baseheal = 0
    staminacost = 25
    hitchance = 60

class DoubleKick:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 10
    baseheal = 0
    staminacost = 10
    hitchance = 65

physicalcall = {
    "Quick Jab": QuickJab,
    "Uppercut": Uppercut,
    "Blitz": Blitz,
    "Black Flash": BlackFlash,
    "Rapid Punch": RapidPunch,
    "Double Kick": DoubleKick,
}