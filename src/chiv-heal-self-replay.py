from Scripts.src.utils import *

currchar = chr1
params = (currchar, playermob)

while is_hurt(Player):
    chiv_heal(*params)
if player_cursed():
    chiv_rmcurse(*params)
