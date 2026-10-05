import json


def new_game():
    return {}

def state_a(state):
    return not state.get("closed", False)

def state_b(state):
    if state.get("_used_b"):
        return False
    state["_used_b"] = True
    return True

def state_c(state):
    return state.get("shelves", [])

def state_d(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def state_e(state):
    return len(state.get("items", [])) < state.get("cap", 0)

def state_f(state):
    if state.get("_used_f"):
        return False
    state["_used_f"] = True
    return True

def state_g(state):
    return state["queue"][0]

def state_h(state):
    return len(state["items"])

def state_i(state):
    return state["next_id"]

def state_j(state):
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] = state.get("dst", 0) + amount
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
