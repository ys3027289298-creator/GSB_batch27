import json


def new_game():
    return {}

def action_a(state):
    return state["queue"][0]

def action_b(state):
    return len(state["items"])

def action_c(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id

def action_d(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] += 10
    return True

def action_e(state):
    return not state["closed"]

def action_f(state):
    events = state.setdefault("events", {})
    if "f" in events:
        return False
    events["f"] = True
    return True

def action_g(state):
    if not state:
        return False
    state.clear()
    return True

def action_h(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def action_i(state):
    items = state.get("items")
    if not items:
        return None
    return items[-1]

def action_j(state):
    if state.get("j_used"):
        return False
    state["j_used"] = True
    return True

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
