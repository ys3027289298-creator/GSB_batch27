import json


def new_game():
    return {}

def event_a(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def event_b(state):
    return len(state.get("crops", [])) < state.get("capacity", 0)

def event_c(state):
    if state.get("counted"):
        return False
    state["counted"] = True
    return True

def event_d(state):
    return state["queue"].pop(0)

def event_e(state):
    return len(state["items"])

def event_f(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id

def event_g(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] += 10
    return True

def event_h(state):
    return not state["closed"]

def event_i(state):
    if state.get("planted"):
        return False
    state["planted"] = True
    return True

def event_j(state):
    return bool(state.get("orders"))

def main():
    print("events 命令: run/quit")
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
