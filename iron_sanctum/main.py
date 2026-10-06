import json


def new_game():
    return {}

def cmd_a(state):
    relics = state.get("relics", set())
    if not relics:
        return False
    relic = next(iter(relics))
    state["relics"] = relics - {relic}
    return True

def cmd_b(state):
    state["nodes"].pop(1, None)
    state["edges"] = {
        edge: weight
        for edge, weight in state["edges"].items()
        if 1 not in edge
    }
    return True

def cmd_c(state):
    return None

def cmd_d(state):
    return state["queue"][0]

def cmd_e(state):
    state["count"] = 0
    return True

def cmd_f(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def cmd_g(state):
    return state["accounts"].get("missing", 0)

def cmd_h(state):
    if state.get("occupants", 0) >= state.get("capacity", 0):
        return False
    state["occupants"] = state.get("occupants", 0) + 1
    return True

def cmd_i(state):
    state["events"].pop(1, None)
    return True

def cmd_j(state):
    return state["cap"] - state["used"]

def main():
    print("main 命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")

if __name__ == "__main__":
    main()
