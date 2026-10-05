import json


def new_game():
    return {}

def action_a(state):
    if state["src"] < 5:
        return False
    state["src"] -= 5
    state["dst"] += 5
    return True

def action_b(state):
    return [row for row in state["audit"] if row[0] == "a"]

def action_c(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def action_d(state):
    return True

def action_e(state):
    if state["paused"]:
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def action_f(state):
    ready = state.get("ready", [])
    if not ready:
        return False
    ready.pop(0)
    return True

def action_g(state):
    if len(state["items"]) >= state["cap"]:
        return False
    if "x" in state["items"]:
        return False
    state["items"].append("x")
    return True

def action_h(state):
    if state["paused"]:
        return False
    return True

def action_i(state):
    state["count"] += 1
    return state["count"]

def action_j(state):
    if state["amount"] < 5:
        return False
    state["amount"] -= 5
    return True

def main():
    print("world 命令: run/quit")
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
