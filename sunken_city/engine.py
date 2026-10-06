import json


def new_game():
    return {}

def rule_a(state):
    section = state.get("section")
    return section is not None and section in state.get("sections", [])

def rule_b(state):
    cabin = state.setdefault("cabin", [])
    if len(cabin) >= state.get("capacity", 1):
        return False
    cabin.append(state.get("occupant"))
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
    return True

def rule_g(state):
    return not state.get("closed", False)

def rule_h(state):
    events = state.setdefault("events", {})
    if "counted" in events:
        return False
    events["counted"] = True
    return True

def rule_i(state):
    if not state:
        return False
    state.clear()
    return True

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
