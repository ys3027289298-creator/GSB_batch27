import json


def new_game():
    return {}

def state_a(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def state_b(state):
    return bool(state.get("events"))

def state_c(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def state_d(state):
    if state.get("paused"):
        return False
    return True

def state_e(state):
    state["count"] += 1
    return state["count"]

def state_f(state):
    if state["amount"] < 5:
        return False
    state["amount"] -= 5
    return True

def state_g(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def state_h(state):
    rows = [row for row in state["audit"] if row[0] == "a"]
    state["audit"][:] = [row for row in state["audit"] if row[0] != "a"]
    return rows

def state_i(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def state_j(state):
    state.clear()
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
