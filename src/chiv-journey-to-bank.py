from os.path import basename
from pathlib import Path
from Scripts.src.utils.utils import can_exec_wtg

    
if can_exec_wtg("chiv-journey-to-bank.py"):
    Spells.CastChivalry("Sacred Journey")
    Target.WaitForTarget(2000, True)
    Target.TargetExecute(0x400D0A9B) # Runebook
