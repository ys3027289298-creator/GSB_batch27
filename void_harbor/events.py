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
    return not state["closed"]

def event_d(state):
    if "fired" in state["events"]:
        return False
    state["events"]["fired"] = True
    return True

def event_e(state):
    return state.get("docked", 0) < state.get("capacity", 0)

def event_f(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def event_g(state):
    return state.get("ship", False)

def event_h(state):
    if state.get("claimed"):
        return False
    state["claimed"] = True
    return True

def event_i(state):
    return state["queue"][0]

def event_j(state):
    return len(set(state["items"]))

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
