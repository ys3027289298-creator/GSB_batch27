import json


def new_game():
    return {
        "ores": [],
        "items": [],
        "cap": 0,
        "paused": False,
        "recipe": None,
        "count": 0,
        "amount": 0,
        "src": 0,
        "dst": 0,
        "audit": [],
        "slots": 0,
        "clock": 0,
    }

def action_a(state):
    ores = state.get("ores", [])
    seen = set()
    unique = []
    for ore in ores:
        if ore in seen:
            continue
        seen.add(ore)
        unique.append(ore)
    if len(unique) != len(ores):
        state["ores"] = unique
        return True
    return False

def action_b(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def action_c(state):
    if state.get("paused"):
        return False
    return state.get("recipe") is not None

def action_d(state):
    state["count"] += 1
    return state["count"]

def action_e(state):
    if state.get("paused"):
        return False
    if state["amount"] < 5:
        return False
    state["amount"] -= 5
    return True

def action_f(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def action_g(state):
    return [row for row in state["audit"] if row[0] == "a"]

def action_h(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def action_i(state):
    state.clear()
    state.update(new_game())
    return True

def action_j(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

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
