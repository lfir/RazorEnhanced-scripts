from Scripts.src.utils import *

fcr_delay = 1600
while (Player.Hits < Player.HitsMax) or Player.Poisoned:
    if Player.Poisoned:
        cast("Cleanse by Fire", True)
    else:
        cast("Close Wounds", True)
    Misc.Pause(fcr_delay)
