from Scripts.src.utils.utils import can_execute_wtg


while (not Player.IsGhost) and can_execute_wtg("discord-last-target.py"):
    Player.UseSkill("Discordance")
    Target.WaitForTarget(2000, True)
    Target.Last()
    Misc.Pause(8000)
