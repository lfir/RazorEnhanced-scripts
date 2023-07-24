from Scripts.src.utils.utils import can_exec_wtg


while (Player.Hits < Player.HitsMax or Player.Poisoned) and can_exec_wtg("chiv-heal-self-replay.py"):
    if Player.Poisoned:
        Spells.CastChivalry("Cleanse by Fire")
        Target.WaitForTarget(2000, True)
        Target.Self()
    else:
        Spells.CastChivalry("Close Wounds")
        Target.WaitForTarget(2000, True)
        Target.Self()
    Misc.Pause(1600)
