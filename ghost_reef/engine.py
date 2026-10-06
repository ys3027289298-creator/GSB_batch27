import json

BATCH_SIZE = 10
MIN_ID = 0


def new_game():
    return {
        "src": 0,
        "dst": 0,
        "closed": False,
        "events": {},
        "queue": [],
        "items": [],
        "next_id": 0,
        "settled": set(),
        "fired": set(),
    }


def rule_a(state):
    if state["src"] < BATCH_SIZE:
        return False
    state["src"] -= BATCH_SIZE
    state["dst"] += BATCH_SIZE
    return True


def rule_b(state):
    return not state.get("closed", False)


def rule_c(state):
    if "rule_c" in state["fired"]:
        return False
    state["fired"].add("rule_c")
    return True


def rule_d(state):
    return bool(state.get("events"))


def rule_e(state):
    event_id, _ = min(state["events"].items(), key=lambda item: item[1])
    return event_id


def rule_f(state):
    return bool(state.get("items"))


def rule_g(state):
    if "rule_g" in state["fired"]:
        return False
    state["fired"].add("rule_g")
    return True


def rule_h(state):
    if not state["queue"]:
        return None
    return state["queue"].pop(0)


def rule_i(state):
    return len(state["items"])


def rule_j(state):
    next_id = state["next_id"]
    state["next_id"] += 1
    return next_id


def main():
    print("engine 命令: run/quit")
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
