while (not Player.IsGhost) and (not Target.HasTarget()):
    Player.UseSkill('Discordance')
    Target.WaitForTarget(2000, True)
    Target.Last()
    Misc.Pause(8000)
