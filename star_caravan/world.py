import json


def new_game():
    return {}

def action_a(state):
    return state["cap"] - state["used"]

def action_b(state):
    cargo = state.get("cargo") or []
    item = state.get("item")
    if item is None or item in cargo:
        return False
    if state.get("paused"):
        return False
    cargo.append(item)
    state["cargo"] = cargo
    return True

def action_c(state):
    state["nodes"].pop(1, None)
    for edge in [edge for edge in state["edges"] if 1 in edge]:
        state["edges"].pop(edge, None)
    return True

def action_d(state):
    manifest = state.get("manifest") or []
    if not manifest:
        return None
    return "\n".join(manifest)

def action_e(state):
    queue = state.get("queue") or []
    if not queue:
        return None
    return queue[0]

def action_f(state):
    state["count"] = 0
    return True

def action_g(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def action_h(state):
    return state["accounts"].get("missing", 0)

def action_i(state):
    save = state.get("save")
    if not save:
        return False
    state.clear()
    state.update(save)
    return True

def action_j(state):
    state["events"].pop(1, None)
    return True

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
