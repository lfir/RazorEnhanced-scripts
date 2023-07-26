shadowWyrm = 0x1DB18
naja = 0x0002FF2C
healPet = Mobiles.FindBySerial(naja)

while (healPet.Hits < healPet.HitsMax or healPet.Poisoned):
    if Target.HasTarget: Target.Cancel()
    if healPet.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(healPet)
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(healPet)
    Misc.Pause(100)
