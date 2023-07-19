def get_scripts(exclude):
    with open("sl.txt") as f:
        return filter(lambda l: l != exclude, f.read().splitlines())

def no_scripts_running(exclude):
    return not any(map(Misc.ScriptStatus, get_scripts(exclude)))

def no_active_target():
    return not Target.HasTarget()

def can_execute_wtg(name):
    return no_scripts_running(name) and no_active_target()
