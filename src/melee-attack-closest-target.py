from Scripts.src.utils import *

mobs = Mobiles.Filter()
mobs.Enabled = True
mobs.RangeMax = 5
mobs.Notorieties.Add(3)  # gray, neutral
mobs.Notorieties.Add(4)  # gray, criminal
mobs.Notorieties.Add(5)  # orange
mobs.Notorieties.Add(6)  # red

while not Player.IsGhost:
    enemies = Mobiles.ApplyFilter(mobs)
    Mobiles.Select(enemies, "Nearest")
    for enemy in enemies:
        target = Mobiles.FindBySerial(enemy.Serial)
        while target and Player.InRangeMobile(target, 2):
            if Player.BuffsExist(curses[0]):
                continue
            Player.Attack(target)
            Misc.Pause(500)
            target = Mobiles.FindBySerial(enemy.Serial)
    Misc.Pause(500)
