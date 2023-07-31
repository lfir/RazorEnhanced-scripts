from Scripts.src.utils import *

currchar = chr0
shadowWyrm = 0x1DB18
naja = 0x0002FF2C
healPet = Mobiles.FindBySerial(naja)

while is_hurt(healPet):
    mag_heal(currchar, healPet)
