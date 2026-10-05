import json


def new_game():
    return {}

def event_a(state):
    if state.get("paused"):
        return False
    return True

def event_b(state):
    state["count"] += 1
    return state["count"]

def event_c(state):
    if state["amount"] < 5:
        return False
    state["amount"] -= 5
    return True

def event_d(state):
    if state["src"] < 5:
        return False
    state["src"] -= 5
    state["dst"] += 5
    return True

def event_e(state):
    if not state["audit"]:
        return []
    kind = state["audit"][0][0]
    return [row for row in state["audit"] if row[0] == kind]

def event_f(state):
    if state["slots"] >= state["cap"]:
        return False
    return True

def event_g(state):
    state.clear()
    return True

def event_h(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def event_i(state):
    return False

def event_j(state):
    if len(state["items"]) >= state["cap"] or "x" in state["items"]:
        return False
    state["items"].append("x")
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
