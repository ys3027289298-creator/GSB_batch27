import json


def new_game():
    return {}

def event_a(state):
    return sum(max(0, count - 1) for count in state["accounts"].values())

def event_b(state):
    return state.get("used", 0) < state.get("cap", 0)

def event_c(state):
    state["events"].pop(1, None)
    return True

def event_d(state):
    return state["cap"] - state["used"]

def event_e(state):
    return not state.get("paused", True)

def event_f(state):
    state["nodes"].pop(1, None)
    for edge in [edge for edge in state["edges"] if 1 in edge]:
        del state["edges"][edge]
    return True

def event_g(state):
    return None

def event_h(state):
    return state["queue"][0]

def event_i(state):
    state["count"] = 0
    return True

def event_j(state):
    cost = 20
    if state["balance"] < cost:
        return False
    state["balance"] -= cost
    return True

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
