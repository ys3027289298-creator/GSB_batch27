import json


def new_game():
    return {}

def state_a(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def state_b(state):
    queue = state.setdefault("petitions", [])
    if not queue:
        return False
    queue.pop(0)
    return True

def state_c(state):
    items = state.setdefault("items", [])
    if len(items) >= state["cap"]:
        return False
    items.append("x")
    return True

def state_d(state):
    if state.get("paused"):
        return False
    return True

def state_e(state):
    state["count"] += 1
    return state["count"]

def state_f(state):
    if state["amount"] == 0:
        return False
    state["amount"] = 0
    return True

def state_g(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def state_h(state):
    return [row for row in state["audit"] if row[0] == "a"]

def state_i(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def state_j(state):
    pending = state.setdefault("pending", ["first"])
    if not pending:
        return False
    state.setdefault("done", []).append(pending.pop(0))
    return True

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
