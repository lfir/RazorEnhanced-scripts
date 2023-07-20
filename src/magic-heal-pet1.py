from Scripts.src.utils.utils import can_exec_wtg


shadowWyrm = 0x1DB18
healPet = Mobiles.FindBySerial(shadowWyrm)

if (healPet.Hits < healPet.HitsMax or healPet.Poisoned) and can_exec_wtg("magic-heal-pet1.py"):
    if healPet.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(healPet)
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(healPet)
