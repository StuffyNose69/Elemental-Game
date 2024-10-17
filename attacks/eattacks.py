class Punch:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 0
    hitchance = 90

class BoneThrow:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 10
    hitchance = 70

class Rot:
    actionType = "Attack"
    actionElement = "Earth"
    basedmg = 20
    hitchance = 75

class Slash:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 20
    hitchance = 90

class Snipe:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 25
    hitchance = 70

class Reinforce:
    actionType = "Heal"
    actionElement = "None"
    baseheal = 30
    hitchance = 100

class Scream:
    actionType = "Attack"
    actionElement = "None"
    basedmg = 0
    hitchance = 100

class Haunt:
    actionType = "Mixed"
    actionElement = "None"
    basedmg = 0
    baseheal = 0
    hitchance = 60

class Fracture:
    actionType = "Attack"
    actionElement = "Prism"
    basedmg = 25
    hitchance = 50

class ShadowsFury:
    actionType = "Mixed"
    actionElement = "Prism"
    basedmg = 0
    baseheal = 0
    hitchance = 75

eattackcall = {
    "Punch": Punch,
    "Bone Throw": BoneThrow,
    "Rot": Rot,
    "Slash": Slash,
    "Snipe": Snipe,
    "Reinforce": Reinforce,
    "Scream": Scream,
    "Haunt": Haunt,
    "Fracture": Fracture,
    "Shadows Fury": ShadowsFury,
}