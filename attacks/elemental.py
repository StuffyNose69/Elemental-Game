# --- EARTH ABILITIES ---

class RockThrow:
    actionType = "Attack"
    actionElement = "Earth"
    basedmg = 0
    energycost = 5
    hitchance = 90

class Encase:
    actionType = "Heal"
    actionElement = "Earth"
    baseheal = 10
    energycost = 5
    hitchance = 90


# --- WATER ABILITIES ---

class Splash:
    actionType = "Attack"
    actionElement = "Water"
    basedmg = 0
    energycost = 5
    hitchance = 90

# --- FLAME ABILITIES ---

class Hellblaze:
    actionType = "Attack"
    actionElement = "Flame"
    basedmg = 0
    energycost = 5
    hitchance = 90

class Rekindle:
    actionType = "Heal"
    actionElement = "Flame"
    baseheal = 10
    energycost = 5
    hitchance = 75

class Detonation:
    actionType = "Attack"
    actionElement = "Flame"
    basedmg = 20
    energycost = 5
    hitchance = 20

class SunChop:
    actionType = "Attack"
    actionElement = "Flame"
    basedmg = 25
    energycost = 20
    hitchance = 66

class CrimsonMoon:
    actionType = "Mixed"
    actionElement = "Flame"
    basedmg = 25
    baseheal = 25
    energycost = 25
    hitchance = 85

# --- ELECTRIC ABILITIES ---

class Shock:
    actionType = "Attack"
    actionElement = "Electric"
    basedmg = 0
    energycost = 5
    hitchance = 90

class ChainLightning:
    actionType = "Attack"
    actionElement = "Electric"
    basedmg = 10
    energycost = 10
    hitchance = 80

class Railgun:
    actionType = "Attack"
    actionElement = "Electric"
    basedmg = 15
    energycost = 10
    hitchance = 66

class ElectronBarrier:
    actionType = "Heal" #possibly change later
    actionElement = "Electric"
    baseheal = 20
    energycost = 10
    hitchance = 100

class VoltaicSlash:
    actionType = "Attack"
    actionElement = "Electric"
    basedmg = 50
    energycost = 20
    hitchance = 60

# --- PRISM ABILITIES ---

class Lightbeam:
    actionType = "Attack"
    actionElement = "Prism"
    basedmg = 0
    energycost = 5
    hitchance = 90

class SpearsOfLight:
    actionType = "Attack"
    actionElement = "Prism"
    basedmg = 10
    energycost = 7
    hitchance = 75

class Cloak: # dodge ability, also boost mobility (immplement later)
    actionType = "Neither"
    actionElement = "Prism"
    energycost = 5
    hitchance = 100

class PiercingShadow:
    actionType = "Mixed"
    actionElement = "Prism"
    basedmg = 20
    baseheal = 10
    energycost = 15
    hitchance = 60

earthcall = {

}

watercall = {

}

flamecall = {

}

electriccall = {

}

prismcall = {

}