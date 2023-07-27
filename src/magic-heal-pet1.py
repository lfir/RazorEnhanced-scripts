from Scripts.src.utils import *

shadowWyrm = 0x1DB18
naja = 0x0002FF2C
healPet = Mobiles.FindBySerial(naja)

if (healPet.Hits < healPet.HitsMax) or healPet.Poisoned:
    if healPet.Poisoned:
        cast("Arch Cure", True, healPet)
    else:
        cast("Greater Heal", True, healPet)
