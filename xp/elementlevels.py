class lvl0:
    energyBuff = 0
    intelBuff = 0
    def newAction(faction):
        return ["", ""]
        # this return is ["thing-to-put-in-actionsbank", "thing-to-put-in-actions"]
    maxXP = 50

class lvl1:
    energyBuff = 0
    intelBuff = 0
    def newAction(faction):
        if faction == "Earth":
            return ["Rock Throw", "Rock Throw - Costs 5 Energy"]
        if faction == "Water":
            return ["Splash", "Splash - Costs 5 Energy"]
        if faction == "Flame":
            return ["Hellblaze", "Hellblaze - Costs 5 Energy"]
        if faction == "Electric":
            return ["Shock", "Shock - Costs 5 Energy"]
        if faction == "Prism":
            return ["Lightbeam", "Lightbeam - Costs 5 Energy"]
    maxXP = 100
        
levelcall = {
    "lvl0": lvl0,
    "lvl1": lvl1
}