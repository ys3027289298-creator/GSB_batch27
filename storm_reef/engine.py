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
    state["edges"] = {
        edge: cost
        for edge, cost in state["edges"].items()
        if 1 not in edge
    }
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

RULES = {
    "a": rule_a,
    "b": rule_b,
    "c": rule_c,
    "d": rule_d,
    "e": rule_e,
    "f": rule_f,
    "g": rule_g,
    "h": rule_h,
    "i": rule_i,
    "j": rule_j,
}

def invariants(state):
    problems = []
    used = state.get("used")
    cap = state.get("cap")
    if used is not None and cap is not None and not 0 <= used <= cap:
        problems.append("used 超出 [0, cap]")
    balance = state.get("balance")
    if balance is not None and balance < 0:
        problems.append("balance 为负")
    count = state.get("count")
    if count is not None and count < 0:
        problems.append("count 为负")
    queue = state.get("queue")
    if queue is not None and not isinstance(queue, list):
        problems.append("queue 不是列表")
    nodes = state.get("nodes")
    edges = state.get("edges")
    if nodes is not None and edges is not None:
        for edge in edges:
            if edge[0] not in nodes or edge[1] not in nodes:
                problems.append("边 %r 指向不存在的节点" % (edge,))
    return problems

def replay(state, actions):
    problems = invariants(state)
    if problems:
        raise AssertionError("初始状态违反不变量: %s" % problems)
    for step, name in enumerate(actions):
        RULES[name](state)
        problems = invariants(state)
        if problems:
            raise AssertionError(
                "重放第 %d 步 (%s) 后违反不变量: %s" % (step, name, problems)
            )
    return state

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
