import json


def new_game():
    return {}

def action_a(state):
    if state.get("_sail_set"):
        return False
    state["_sail_set"] = True
    return True

def action_b(state):
    return False

def action_c(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def action_d(state):
    return False

def action_e(state):
    if state.get("_locked"):
        return False
    state["_locked"] = True
    return True

def action_f(state):
    return state["queue"].pop(0)

def action_g(state):
    return len(state["items"])

def action_h(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id

def action_i(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    return True

def action_j(state):
    return not state.get("closed", False)

def main():
    print("world 命令: run/quit")
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
