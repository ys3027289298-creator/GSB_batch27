import json


def new_game():
    return {
        "accounts": {},
        "events": {},
        "used": 0,
        "cap": 0,
        "nodes": {},
        "edges": {},
        "queue": [],
        "count": 0,
        "balance": 0,
        "paused": False,
    }

def event_a(state):
    return state["accounts"].get("missing", 0)

def event_b(state):
    return state["used"] < state["cap"]

def event_c(state):
    if state["events"]:
        key = next(iter(state["events"]))
        state["events"].pop(key, None)
    return True

def event_d(state):
    return state["cap"] - state["used"]

def event_e(state):
    return bool(state["queue"]) and not state["paused"]

def event_f(state):
    state["nodes"].pop(1, None)
    for edge in [edge for edge in state["edges"] if 1 in edge]:
        state["edges"].pop(edge, None)
    return True

def event_g(state):
    return state.get("order")

def event_h(state):
    return state["queue"][0] if state["queue"] else None

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
