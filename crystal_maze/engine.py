import json


def new_game():
    return {}

def rule_a(state):
    return state.get("crystal") not in state.get("crystals", ())

def rule_b(state):
    clock = state.get("clock", 0)
    if state.get("paused"):
        return clock
    state["clock"] = clock + 1
    return state["clock"]

def rule_c(state):
    return len(state.get("channel", ())) < state.get("cap", 0)

def rule_d(state):
    items = state["items"]
    cap = state.get("cap")
    if cap is not None and len(items) >= cap:
        return False
    items.append("x")
    return True

def rule_e(state):
    return not state.get("paused", False)

def rule_f(state):
    state["count"] = state.get("count", 0) + 1
    return state["count"]

def rule_g(state):
    amount = state.get("amount", 0)
    if amount < 5:
        return False
    state["amount"] = amount - 5
    return True

def rule_h(state):
    src = state.get("src", 0)
    if src < 5:
        return False
    state["src"] = src - 5
    state["dst"] = state.get("dst", 0) + 5
    return True

def rule_i(state):
    audit = state.get("audit", ())
    if not audit:
        return []
    earliest = audit[0][0]
    return [row for row in audit if row[0] == earliest]

def rule_j(state):
    return state.get("slots", 0) < state.get("cap", 0)

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
