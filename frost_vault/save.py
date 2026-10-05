import json


def new_game():
    return {}

def state_a(state):
    amount = state.get("amount", 0)
    if amount < 5:
        return False
    state["amount"] = amount - 5
    return True

def state_b(state):
    src = state.get("src", 0)
    if src < 5:
        return False
    state["src"] = src - 5
    state["dst"] = state.get("dst", 0) + 5
    return True

def state_c(state):
    rows = state.get("audit", [])
    if not rows:
        return []
    first = rows[0][0]
    return [row for row in rows if row[0] == first]

def state_d(state):
    if state.get("slots", 0) >= state.get("cap", 0):
        return False
    state["slots"] += 1
    return True

def state_e(state):
    return state.get("message", "宝库是空的")

def state_f(state):
    if state.get("paused"):
        return state.get("clock", 0)
    state["clock"] = state.get("clock", 0) + 1
    return state["clock"]

def state_g(state):
    return bool(state.get("key"))

def state_h(state):
    items = state.get("items", [])
    if len(items) >= state.get("cap", 0):
        return False
    items.append("x")
    return True

def state_i(state):
    if state.get("paused"):
        return False
    return True

def state_j(state):
    state["count"] = state.get("count", 0) + 1
    return state["count"]

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