from AutoComplete import *


def cast(spell, usetarg, target=None):
    if usetarg and Target.HasTarget():
        Target.Cancel()
    Spells.Cast(spell)
    if usetarg:
        Target.WaitForTarget(2000, True)
        if target is None:
            Target.Self()
        else:
            Target.TargetExecute(target)
