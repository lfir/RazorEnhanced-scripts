from os.path import basename
from pathlib import Path
from Scripts.src.utils.utils import can_exec_wtg

    
if can_exec_wtg("recall-to-bank.py"):
    Spells.CastMagery("Recall")
    Target.WaitForTarget(2000, True)
    Target.TargetExecute(0x408CAD30)
