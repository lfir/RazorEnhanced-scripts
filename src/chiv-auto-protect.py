from Scripts.src.utils import *

currchar = chr1

while not Player.IsGhost:
    if is_hurt(Player, 30):
        chiv_heal(currchar, playermob)
    if Player.BuffsExist(curses[0]):
        Player.HeadMessage(40, "Blood Oath! RUN!")
        Player.SetWarMode(False)
        Misc.Pause(100)
    if Player.Poisoned:
        continue
    if player_cursed():
        chiv_rmcurse(currchar, playermob)
    if not Player.BuffsExist("Consecrate Weapon"):
        cast("Consecrate Weapon", currchar, False)
    if not Player.BuffsExist("Divine Fury"):
        cast("Divine Fury", currchar, False)
    Misc.Pause(500)
