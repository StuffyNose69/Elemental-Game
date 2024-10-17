import random
import time
import os

sleep = time.sleep
def clear():
  os.system("cls")

firstnames = ["Geralt", "Fartass", "Yinlyn", "Tarco", "Yom", "Tobin", "Seanathon", "Tryfic", "Josh", "Tyler", "Jack", "Nate", "Ryln", "Kyng", "Jakub", "Elias", "Brynnon", "Lee", "Mikal", "Antemi", "Bo", "Joel", "Alforvonquavious", "Turken", "Hyatt", "Viktal", "Sigmagoon", "Byght", "Fallyn", "Daustin"]
lastnames = ["Goofyahhlastname", "Emerson", "Leifern", "Axelstone", "Voughn", "Conah", "Systhertyto", "Jogoat", "Moulton", "Poitras", "Grysthorn", "Salisston", "Aquanil", "Borgetti", "Obama", "Thornton", "Beregton", "Stasi", "Strantion", "Freakens", "Lawford", "Arizonamangotea", "Washington", "Forgetti", "Eichel", "Rose", "Whitterson", "Gigglesworth"]

def ArenaDuel():
  enemyFaction = random.choice(["Earth", "Water", "Flame", "Electric", "Prism"])
  