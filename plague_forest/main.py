import json


def new_game():
    return {}

def cmd_a(state):
    state["items"].append(len(state["items"]))
    return len(state["items"]) - 1

def cmd_b(state):
    case_id = state["next_id"]
    state["next_id"] += 1
    return case_id

def cmd_c(state):
    if state["src"] < 10:
        return False
    state["src"] -= 10
    state["dst"] += 10
    return True

def cmd_d(state):
    if state["closed"]:
        return False
    return True

def cmd_e(state):
    if state["events"]:
        return False
    state["events"]["collect"] = True
    return True

def cmd_f(state):
    if not state:
        return False
    return True

def cmd_g(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def cmd_h(state):
    if not state:
        return False
    state.clear()
    return True

def cmd_i(state):
    if state.get("occupied"):
        return False
    state["occupied"] = True
    return True

def cmd_j(state):
    return state["queue"][0]

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
