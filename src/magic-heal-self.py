from Scripts.src.utils import *

if (Player.Hits < Player.HitsMax) or Player.Poisoned:
    if Player.Poisoned:
        cast("Arch Cure", True)
    else:
        cast("Greater Heal", True)
