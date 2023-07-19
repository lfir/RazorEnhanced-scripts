if (not Player.Poisoned) and (not Target.HasTarget()):
    Spells.CastMagery('Invisibility')
    Target.WaitForTarget(2000, True)
    Target.Self()
