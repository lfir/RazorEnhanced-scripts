from AutoComplete import *

# Variables related to different characters
chr0 = {"fcrdelay": 0}
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
# Pet serial numbers
shadow_wyrm = 0x1DB18
naja = 0x0002FF2C
pets = [shadow_wyrm, naja]


def get_activepet():
    # Only one should be active at a time
    return next(filter(lambda p: p, map(Mobiles.FindBySerial, pets)))


def cast(spell, caster, target=None):
    if Player.Mana >= spells.get(spell):
        usetarg = target is not None
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
        cast("Cleanse by Fire", caster, target)
    else:
        cast("Close Wounds", caster, target)


def mag_heal(caster, target):
    if target.Poisoned:
        cast("Arch Cure", caster, target)
    else:
        cast("Greater Heal", caster, target)


def player_cursed():
    return any(map(Player.BuffsExist, curses))


def find_mobiles(notorieties, maxrange):
    # 1: blue; 2: green; 3: gray, neutral
    # 4: gray, criminal; 5: orange; 6: red
    mobilefilter = Mobiles.Filter()
    mobilefilter.RangeMax = maxrange
    for n in notorieties:
        mobilefilter.Notorieties.Add(n)
    mobilefilter.CheckIgnoreObject = True
    mobilefilter.CheckLineOfSight = True
    return Mobiles.ApplyFilter(mobilefilter)
