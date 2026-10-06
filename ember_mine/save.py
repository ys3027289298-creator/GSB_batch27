import json


def new_game():
    return {}

def state_a(state):
    if state.get("mined"):
        return False
    state["mined"] = True
    return True

def state_b(state):
    return state["queue"].pop(0)

def state_c(state):
    return len(state["items"])

def state_d(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id

def state_e(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] += 10
    return True

def state_f(state):
    return not state.get("closed", False)

def state_g(state):
    events = state.setdefault("events", {})
    if events.get("counted"):
        return False
    events["counted"] = True
    return True

def state_h(state):
    return bool(state.get("ore"))

def state_i(state):
    return min(state["events"], key=lambda key: state["events"][key][0])

def state_j(state):
    return bool(state.get("running"))

def main():
    print("save 命令: run/quit")
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
