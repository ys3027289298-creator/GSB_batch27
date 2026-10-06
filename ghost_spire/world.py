import json


def new_game():
    return {}

def action_a(state):
    state["count"] = 0
    return True

def action_b(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def action_c(state):
    return state["accounts"].get("missing", 0)

def action_d(state):
    return False

def action_e(state):
    state["events"].clear()
    return True

def action_f(state):
    return state["cap"] - state["used"]

def action_g(state):
    return False

def action_h(state):
    node = state["nodes"].pop(1, None)
    if node is not None:
        state["edges"] = {
            edge: weight
            for edge, weight in state["edges"].items()
            if 1 not in edge
        }
    return True

def action_i(state):
    return None

def action_j(state):
    return state["queue"][0]

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
