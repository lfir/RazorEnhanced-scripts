from Scripts.src.utils.utils import can_exec_wtg


shadowWyrm = 0x1DB18
healPet = Mobiles.FindBySerial(shadowWyrm)

while (healPet.Hits < healPet.HitsMax or healPet.Poisoned) and can_exec_wtg("magic-heal-pet1-replay.py"):
    if healPet.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, False)
        Target.TargetExecute(healPet)
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, False)
        Target.TargetExecute(healPet)
    Misc.Pause(100)
