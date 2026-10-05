import json


def new_game():
    return {}

def event_a(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def event_b(state):
    return bool(state.get("orders"))

def event_c(state):
    if state.get("c_counted"):
        return False
    state["c_counted"] = True
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
    state["dst"] = state.get("dst", 0) + 10
    return True

def event_h(state):
    return not state.get("closed", False)

def event_i(state):
    if state.get("i_viewed"):
        return False
    state["i_viewed"] = True
    return True

def event_j(state):
    crops = state.get("crops", [])
    return len(crops) != len(set(crops))

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
