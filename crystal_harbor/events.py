import json


def new_game():
    return {
        "slots": 0,
        "cap": 2,
        "paused": False,
        "clock": 0,
        "items": [],
        "count": 0,
        "amount": 0,
        "src": 0,
        "dst": 0,
        "audit": [],
        "ship": "a",
    }

def event_a(state):
    return state["slots"] < state["cap"]

def event_b(state):
    return True

def event_c(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def event_d(state):
    return False

def event_e(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def event_f(state):
    return not state.get("paused", False)

def event_g(state):
    state["count"] += 1
    return state["count"]

def event_h(state):
    if state["amount"] < 5:
        return False
    state["amount"] -= 5
    return True

def event_i(state):
    if state["src"] < 5:
        return False
    state["src"] -= 5
    state["dst"] += 5
    return True

def event_j(state):
    return [row for row in state["audit"] if row[0] == state["ship"]]

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
