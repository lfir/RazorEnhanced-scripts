from Scripts.src.utils.utils import can_exec_wtg


if (not Player.Poisoned) and can_exec_wtg("magic-invisibility-self.py"):
    Spells.CastMagery("Invisibility")
    Target.WaitForTarget(2000, False)
    Target.Self()
