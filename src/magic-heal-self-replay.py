from AutoComplete import *

while (Player.Hits < Player.HitsMax) or Player.Poisoned:
    if Target.HasTarget: Target.Cancel()
    if Player.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, True)
        Target.Self()
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, True)
        Target.Self()
    Misc.Pause(100)
