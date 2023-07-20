from Scripts.src.utils.utils import can_exec_wtg


while can_exec_wtg("discord-last-target.py"):
    Player.UseSkill("Discordance")
    Target.WaitForTarget(2000, True)
    Target.Last()
    Misc.Pause(8000)
