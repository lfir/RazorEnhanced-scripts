from AutoComplete import *

if not Player.Poisoned:
    if Target.HasTarget: Target.Cancel()
    Spells.CastMagery("Invisibility")
    Target.WaitForTarget(2000, True)
    Target.Self()
