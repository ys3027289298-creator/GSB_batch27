import json


def new_game():
    return {}

def state_a(state):
    queue = state.get("queue")
    if not queue:
        return None
    return queue[0]

def state_b(state):
    state["count"] = 0
    return True

def state_c(state):
    cost = 20
    if state.get("balance", 0) < cost:
        return False
    state["balance"] -= cost
    return True

def state_d(state):
    return state["accounts"].get("missing", 0)

def state_e(state):
    queue = state.get("queue")
    if not queue:
        return False
    queue.pop(0)
    return True

def state_f(state):
    events = state.get("events", {})
    if 1 not in events:
        return False
    del events[1]
    return True

def state_g(state):
    return state["cap"] - state["used"]

def state_h(state):
    if state.get("paused"):
        return False
    return bool(state.get("running"))

def state_i(state):
    node_id = 1
    removed = state["nodes"].pop(node_id, None)
    edges = state.get("edges", {})
    for edge in [key for key in edges if node_id in key]:
        del edges[edge]
    return removed is not None

def state_j(state):
    return None

def main():
    print("save 命令: run/quit")
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
