if Target.HasTarget: Target.Cancel()
Spells.CastChivalry("Sacred Journey")
Target.WaitForTarget(2000, True)
Target.TargetExecute(0x400D0A9B) # Runebook
