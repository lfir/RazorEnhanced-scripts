from Scripts.src.utils import *

currchar = chr1

while not Player.IsGhost:
    if is_hurt(Player, 30):
        chiv_heal(currchar, playermob)
    if Player.BuffsExist(curses[0]):
        Player.HeadMessage(40, "Blood Oath! RUN!")
        Player.SetWarMode(False)
    if Player.Poisoned:
        continue
    if player_cursed():
        cast("Remove Curse", currchar, playermob)
    if not Player.BuffsExist("Consecrate Weapon"):
        cast("Consecrate Weapon", currchar)
    if currchar.get("usesdf") and (not Player.BuffsExist("Divine Fury")):
        cast("Divine Fury", currchar)
    Misc.Pause(500)
