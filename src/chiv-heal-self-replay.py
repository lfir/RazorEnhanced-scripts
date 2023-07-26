while (Player.Hits < Player.HitsMax or Player.Poisoned):
    if Target.HasTarget: Target.Cancel()
    if Player.Poisoned:
        Spells.CastChivalry("Cleanse by Fire")
        Target.WaitForTarget(2000, True)
        Target.Self()
    else:
        Spells.CastChivalry("Close Wounds")
        Target.WaitForTarget(2000, True)
        Target.Self()
    Misc.Pause(1600)
