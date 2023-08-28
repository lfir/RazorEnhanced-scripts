from Scripts.src.utils import *

while not Player.IsGhost:
    enemies = find_mobiles(range(3, 7), 5)
    enemies_by_dist = sorted(enemies, key=lambda e: Player.DistanceTo(e))
    for enemy in enemies_by_dist:
        target = Mobiles.FindBySerial(enemy.Serial)
        while target and Player.InRangeMobile(target, 2):
            if Player.BuffsExist(curses[0]):
                continue
            Player.Attack(target)
            Misc.Pause(500)
            target = Mobiles.FindBySerial(enemy.Serial)
    Misc.Pause(500)
