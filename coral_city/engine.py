import json


def new_game():
    return {}

def rule_a(state):
    state["count"] += 1
    return state["count"]

def rule_b(state):
    if state["amount"] < 5:
        return False
    state["amount"] -= 5
    return True

def rule_c(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def rule_d(state):
    return [row for row in state["audit"] if row[0] == "a"]

def rule_e(state):
    return state["slots"] < state["cap"]

def rule_f(state):
    sections = state.get("sections", [])
    return len(sections) == len(set(sections))

def rule_g(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def rule_h(state):
    return bool(state.get("sections"))

def rule_i(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def rule_j(state):
    return not state.get("paused", False)

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
