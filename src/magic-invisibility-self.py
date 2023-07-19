from Scripts.src.utils.utils import can_execute_wtg


if (not Player.Poisoned) and can_execute_wtg("magic-invisibility-self.py"):
    Spells.CastMagery("Invisibility")
    Target.WaitForTarget(2000, True)
    Target.Self()
