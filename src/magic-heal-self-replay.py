from Scripts.src.utils import *

fcr_delay = 100
while (Player.Hits < Player.HitsMax) or Player.Poisoned:
    if Player.Poisoned:
        cast("Arch Cure", True)
    else:
        cast("Greater Heal", True)
    Misc.Pause(fcr_delay)
