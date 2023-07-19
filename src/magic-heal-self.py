from Scripts.src.utils.utils import can_execute_wtg


if (Player.Hits < Player.HitsMax or Player.Poisoned) and can_execute_wtg("magic-heal-self.py"):
    if Player.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, True)
        Target.Self()
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, True)
        Target.Self()
