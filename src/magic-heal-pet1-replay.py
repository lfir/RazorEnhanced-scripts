shadowWyrm = 0x1DB18
healPet = Mobiles.FindBySerial(shadowWyrm)

while (healPet.Hits < healPet.HitsMax or healPet.Poisoned) and (not Target.HasTarget()):
    if healPet.Poisoned:
        Spells.CastMagery('Arch Cure')
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(healPet)
    else:
        Spells.CastMagery('Greater Heal')
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(healPet)
    Misc.Pause(100)
