from AutoComplete import *


def find_mobile():
    mobilefilter = Mobiles.Filter()
    mobilefilter.RangeMax = 2
    mobilefilter.Notorieties.Add(1)  # 1: blue
    mobilefilter.Notorieties.Add(2)  # 2: green
    mobilefilter.Notorieties.Add(3)  # 3: gray, neutral
    mobilefilter.Notorieties.Add(4)  # 4: gray, criminal
    mobilefilter.CheckIgnoreObject = True
    mobilefilter.CheckLineOfSight = True
    mobiles = Mobiles.ApplyFilter(mobilefilter)
    return Mobiles.Select(mobiles, "Nearest")


Journal.Clear()
while not Player.IsGhost:
    if Journal.SearchByType("You must wait a few moments to use another skill.", "System"):
        break
    if Target.HasTarget:
        Target.Cancel()
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget(2000, True)
    Target.TargetExecute(find_mobile())
    Misc.Pause(100)
