from Scripts.src.utils import *

while not Player.IsGhost:
    enemies = find_mobiles(range(3, 7), 5)
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
