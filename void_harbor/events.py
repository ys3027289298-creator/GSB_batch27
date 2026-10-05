import json


def new_game():
    return {}

def event_a(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id

def event_b(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] += 10
    return True

def event_c(state):
    if state.get("closed"):
        return False
    return True

def event_d(state):
    events = state.setdefault("events", {})
    if "d" in events:
        return False
    events["d"] = True
    return True

def event_e(state):
    if not state.get("queue"):
        return False
    return True

def event_f(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def event_g(state):
    if len(state.get("items", [])) >= state.get("capacity", 0):
        return False
    return True

def event_h(state):
    if state.get("h_done"):
        return False
    state["h_done"] = True
    return True

def event_i(state):
    return state["queue"][0]

def event_j(state):
    return len(state["items"])

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
