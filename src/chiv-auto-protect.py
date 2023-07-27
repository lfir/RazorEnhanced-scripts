from Scripts.src.utils import *

curses = {"Bload Oath", "Clumsy", "Corpse Skin", "Curse", "Evil Omen", "Feeble Mind", "Mind Rot", "Mortal Strike",
               "Paralyze", "Strangle", "Weaken"}
fcr_delay = 1600

while not Player.IsGhost:
    if Player.Poisoned and (Player.Mana >= 10):
        cast("Cleanse by Fire", True)
        Misc.Pause(fcr_delay)
    if Player.Poisoned: continue
    if (Player.Hits <= 100) and (Player.Mana >= 10):
        cast("Close Wounds", True)
        Misc.Pause(fcr_delay)
    if any(map(Player.BuffsExist, curses)) and (Player.Mana >= 20):
        cast("Remove Curse", True)
        Misc.Pause(fcr_delay)
    if (not Player.BuffsExist("Consecrate Weapon")) and (Player.Mana >= 10):
        cast("Consecrate Weapon", False)
        Misc.Pause(fcr_delay)
    if (not Player.BuffsExist("Divine Fury")) and (Player.Mana >= 10):
        cast("Divine Fury", False)
        Misc.Pause(fcr_delay)
    Misc.Pause(500)
