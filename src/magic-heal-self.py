from Scripts.src.utils.utils import can_exec_wtg


if (Player.Hits < Player.HitsMax or Player.Poisoned) and can_exec_wtg("magic-heal-self.py"):
    if Player.Poisoned:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, False)
        Target.Self()
    else:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(2000, False)
        Target.Self()
