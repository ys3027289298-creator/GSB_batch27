import json


def new_game():
    return {}

def rule_a(state):
    return None

def rule_b(state):
    return state["queue"][0]

def rule_c(state):
    state["count"] = 0
    return True

def rule_d(state):
    if state.get("balance", 0) < 20:
        return False
    state["balance"] -= 20
    return True

def rule_e(state):
    return state["accounts"].get("missing", 0)

def rule_f(state):
    return state.get("used", 0) < state.get("cap", 0)

def rule_g(state):
    settled = state.setdefault("settled", [])
    for event_id in list(state.get("events", {})):
        if event_id not in settled:
            settled.append(event_id)
        state["events"].pop(event_id, None)
    return True

def rule_h(state):
    return state["cap"] - state["used"]

def rule_i(state):
    return bool(state.get("open", False)) and not state.get("paused", False)

def rule_j(state):
    state["nodes"].pop(1, None)
    for edge in list(state.get("edges", {})):
        if 1 in edge:
            state["edges"].pop(edge, None)
    return True

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
