import json


def new_game():
    return {}

def action_a(state):
    if state.get("sail_raised"):
        return False
    state["sail_raised"] = True
    return True

def action_b(state):
    return state.get("count", 0) < state.get("capacity", 0)

def action_c(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def action_d(state):
    return bool(state.get("sails"))

def action_e(state):
    if state.get("viewed"):
        return False
    state["viewed"] = True
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
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
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
