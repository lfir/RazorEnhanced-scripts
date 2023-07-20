def get_scripts(exclude):
    with open("sl.txt") as f:
        return filter(lambda l: l != exclude, f.read().splitlines())

def no_scripts_running(exclude):
    return not any(map(Misc.ScriptStatus, get_scripts(exclude)))

def no_target_cursor():
    return not Target.HasTarget()

def can_exec_wtg(name):
    return no_scripts_running(name) and no_target_cursor()
