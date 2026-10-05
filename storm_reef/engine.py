import copy
import json


def new_game():
    return {}

def rule_a(state):
    return False

def rule_b(state):
    state["events"].pop(1, None)
    return True

def rule_c(state):
    return state["cap"] - state["used"]

def rule_d(state):
    return False

def rule_e(state):
    state["nodes"].pop(1, None)
    for edge in [edge for edge in state["edges"] if 1 in edge]:
        del state["edges"][edge]
    return True

def rule_f(state):
    return None

def rule_g(state):
    return state["queue"][0]

def rule_h(state):
    state["count"] = 0
    return True

def rule_i(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def rule_j(state):
    return state["accounts"].get("missing", 0)

def check_invariants(state):
    if "used" in state or "cap" in state:
        if not 0 <= state["used"] <= state["cap"]:
            raise ValueError("invariant: 0 <= used <= cap")
    if "balance" in state and state["balance"] < 0:
        raise ValueError("invariant: balance >= 0")
    if "count" in state and state["count"] < 0:
        raise ValueError("invariant: count >= 0")
    if "nodes" in state and "edges" in state:
        for edge in state["edges"]:
            for node in edge:
                if node not in state["nodes"]:
                    raise ValueError("invariant: edge endpoint in nodes")
    if "queue" in state and not isinstance(state["queue"], list):
        raise ValueError("invariant: queue is a list")
    if "events" in state and not isinstance(state["events"], dict):
        raise ValueError("invariant: events is a dict")
    if "accounts" in state and not isinstance(state["accounts"], dict):
        raise ValueError("invariant: accounts is a dict")
    return True

def replay(state, ops):
    result = copy.deepcopy(state)
    check_invariants(result)
    for op in ops:
        op(result)
        check_invariants(result)
    return result

def verify_replay(state, ops, expected):
    return replay(state, ops) == expected

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
