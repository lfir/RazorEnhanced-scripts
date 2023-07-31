from AutoComplete import *

# Variables related to different characters
chr0 = {"fcrdelay": 100}
chr1 = {"fcrdelay": 1600}
playermob = Mobiles.FindBySerial(Player.Serial)
# Spell mana costs
spells = {
    # Fourth Circle
    "Arch Cure": 11,
    "Greater Heal": 11,
    "Recall": 11,
    # Sixth Circle
    "Invisibility": 20,
    # Chivalry
    "Close Wounds": 10,
    "Cleanse by Fire": 10,
    "Consecrate Weapon": 10,
    "Divine Fury": 10,
    "Remove Curse": 20,
    "Sacred Journey": 20
}
curses = ["Bload Oath (curse)", "Clumsy", "Corpse Skin", "Curse", "Evil Omen", "Feeble Mind", "Mind Rot",
          "Mortal Strike", "Paralyze", "Strangle", "Weaken"]


def cast(spell, caster, usetarg, target=None):
    if Player.Mana >= spells.get(spell):
        if usetarg and Target.HasTarget():
            Target.Cancel()
        Spells.Cast(spell)
        if usetarg:
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(target)
        Misc.Pause(caster.get('fcrdelay'))


def is_hurt(target, hpdiff=0):
    return (target.Hits < (target.HitsMax - hpdiff)) or target.Poisoned


def chiv_heal(caster, target):
    if target.Poisoned:
        cast("Cleanse by Fire", caster, True, target)
    else:
        cast("Close Wounds", caster, True, target)


def mag_heal(caster, target):
    if target.Poisoned:
        cast("Arch Cure", caster, True, target)
    else:
        cast("Greater Heal", caster, True, target)


def player_cursed():
    return any(map(Player.BuffsExist, curses))


def chiv_rmcurse(caster, target):
    cast("Remove Curse", caster, True, target)
