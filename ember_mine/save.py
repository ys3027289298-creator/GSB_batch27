import json


def new_game():
    return {
        "ores": set(),
        "queue": [],
        "items": [],
        "next_id": 1,
        "src": 0,
        "dst": 0,
        "closed": False,
        "events": {},
        "claimed": set(),
        "layer": [],
        "cargo": ["ore", "ore"],
        "capacity": 2,
    }

def state_a(state):
    ore = state.get("pending_ore")
    if ore in state["ores"]:
        return False
    state["ores"].add(ore)
    return True

def state_b(state):
    return state["queue"].pop(0)

def state_c(state):
    return len(state["items"])

def state_d(state):
    current = state["next_id"]
    state["next_id"] = current + 1
    return current

def state_e(state):
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def state_f(state):
    return not state["closed"]

def state_g(state):
    event = state.get("pending_event")
    if event in state["claimed"]:
        return False
    state["claimed"].add(event)
    return True

def state_h(state):
    return len(state["cargo"]) < state["capacity"]

def state_i(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def state_j(state):
    return bool(state["layer"])

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
