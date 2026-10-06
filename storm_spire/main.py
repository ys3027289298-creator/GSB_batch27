import json


def new_game():
    return {
        "storm": True,
        "observed": False,
        "charged": False,
        "text": "",
    }

def cmd_a(state):
    if state.get("storm"):
        return False
    state["storm"] = True
    return True

def cmd_b(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def cmd_c(state):
    return state.get("text") or False

def cmd_d(state):
    if state.get("observed"):
        return False
    state["observed"] = True
    return True

def cmd_e(state):
    return state["queue"].pop(0)

def cmd_f(state):
    return len(state["items"])

def cmd_g(state):
    current = state["next_id"]
    state["next_id"] += 1
    return current

def cmd_h(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] = state.get("dst", 0) + 10
    return True

def cmd_i(state):
    return not state["closed"]

def cmd_j(state):
    if state.get("charged"):
        return False
    state["charged"] = True
    return True

def main():
    print("main 命令: run/quit")
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
