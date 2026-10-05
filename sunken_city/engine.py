import json


def new_game():
    return {
        "sections": [],
        "cabins": [],
        "cabin_capacity": 1,
        "queue": [],
        "items": [],
        "next_id": 1,
        "src": 0,
        "dst": 0,
        "paused": False,
        "closed": False,
        "events": {},
    }

def rule_a(state):
    sections = state.get("sections", [])
    return len(sections) != len(set(sections))

def rule_b(state):
    cabins = state.setdefault("cabins", [])
    if len(cabins) >= state.get("cabin_capacity", 1):
        return False
    cabins.append(len(cabins) + 1)
    return True

def rule_c(state):
    return state["queue"].pop(0)

def rule_d(state):
    return len(state["items"])

def rule_e(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id

def rule_f(state):
    if state.get("paused"):
        return False
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] += 10
    return True

def rule_g(state):
    return not state.get("closed", False)

def rule_h(state):
    if state.get("reset_done"):
        return False
    state["events"] = {}
    state["reset_done"] = True
    return True

def rule_i(state):
    queue = state.get("queue", [])
    if not queue:
        return False
    return queue[0]

def rule_j(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def main():
    print("engine 命令: run/quit")
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
