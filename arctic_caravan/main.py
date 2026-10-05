import json


def new_game():
    return {
        "balance": 100,
        "accounts": {},
        "events": {},
        "used": 0,
        "cap": 10,
        "nodes": {},
        "edges": {},
        "queue": [],
        "count": 0,
        "paused": False,
    }


def cmd_a(state):
    if state.get("paused"):
        return False
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True


def cmd_b(state):
    return state["accounts"].get("missing", 0)


def cmd_c(state):
    return False


def cmd_d(state):
    state["events"].pop(1, None)
    return True


def cmd_e(state):
    return state["cap"] - state["used"]


def cmd_f(state):
    return False


def cmd_g(state):
    state["nodes"].pop(1, None)
    for edge in [edge for edge in state["edges"] if 1 in edge]:
        del state["edges"][edge]
    return True


def cmd_h(state):
    return None


def cmd_i(state):
    if not state["queue"]:
        return None
    return state["queue"][0]


def cmd_j(state):
    state["count"] = 0
    return True


COMMANDS = {
    "a": cmd_a,
    "b": cmd_b,
    "c": cmd_c,
    "d": cmd_d,
    "e": cmd_e,
    "f": cmd_f,
    "g": cmd_g,
    "h": cmd_h,
    "i": cmd_i,
    "j": cmd_j,
}


def main():
    state = new_game()
    print("main 命令: a-j/reset/status/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        if raw == "reset":
            state = new_game()
            print("ok")
            continue
        if raw == "status":
            print(json.dumps(state, sort_keys=True, default=list))
            continue
        func = COMMANDS.get(raw)
        if func is None:
            print("unknown")
            continue
        print(repr(func(state)))


if __name__ == "__main__":
    main()
