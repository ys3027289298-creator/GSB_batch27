import json


WRECK_TRANSFER = 10


def new_game():
    return {}

def rule_a(state):
    if state["src"] < WRECK_TRANSFER:
        return False
    state["src"] -= WRECK_TRANSFER
    state["dst"] += WRECK_TRANSFER
    return True

def rule_b(state):
    return not state.get("closed", False)

def rule_c(state):
    if state.get("events", {}).get("wreck"):
        return False
    state.setdefault("events", {})["wreck"] = True
    return True

def rule_d(state):
    if not state.get("wrecks"):
        return False
    return True

def rule_e(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def rule_f(state):
    if state.get("paused", True):
        return False
    return True

def rule_g(state):
    if state.get("reset_done", False):
        return False
    state["reset_done"] = True
    return True

def rule_h(state):
    return state["queue"].pop(0)

def rule_i(state):
    return len(state["items"])

def rule_j(state):
    new_id = state["next_id"]
    state["next_id"] += 1
    return new_id

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
