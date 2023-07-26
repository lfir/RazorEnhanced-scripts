from AutoComplete import *

if Target.HasTarget: Target.Cancel()
Spells.CastMagery("Recall")
Target.WaitForTarget(2000, True)
Target.TargetExecute(0x408CAD30)
