from AutoComplete import *

magery_spells = {"Clumsy", "Create Food", "Feeblemind", "Heal", "Magic Arrow", "Night Sight", "Reactive Armor",
                 "Weaken", "Agility", "Cunning", "Cure", "Harm", "Magic Trap", "Magic Untrap", "Protection", "Strength",
                 "Bless", "Fireball", "Magic Lock", "Poison", "Telekinesis", "Teleport", "Unlock", "Wall of Stone",
                 "Arch Cure", "Arch Protection", "Curse", "Fire Field", "Greater Heal", "Lightning", "Mana Drain",
                 "Recall", "Blade Spirits", "Dispel Field", "Incognito", "Magic Reflection", "Mind Blast", "Paralyze",
                 "Poison Field", "Summon Creature", "Dispel", "Energy Bolt", "Explosion", "Invisibility", "Mark",
                 "Mass Curse", "Paralyze Field", "Reveal", "Chain Lightning", "Energy Field", "Flamestrike",
                 "Gate Travel", "Mana Vampire", "Mass Dispel", "Meteor Swarm", "Polymorph", "Earthquake",
                 "Energy Vortex", "Resurrection", "Summon Air Elemental", "Summon Daemon", "Summon Earth Elemental",
                 "Summon Fire Elemental", "Summon Water Elemental"}

chiv_spells = {"Close Wounds", "Remove Curse", "Cleanse by Fire", "Consecrate Weapon", "Sacred Journey", "Divine Fury",
               "Dispel Evil", "Enemy of One", "Holy Light", "Noble Sacrifice"}


def cast(spell, usetarg, target=None):
    if usetarg and Target.HasTarget:
        Target.Cancel()
    if spell in magery_spells:
        Spells.CastMagery(spell)
    elif spell in chiv_spells:
        Spells.CastChivalry(spell)
    if usetarg:
        Target.WaitForTarget(2000, True)
        if target is None:
            Target.Self()
        else:
            Target.TargetExecute(target)
