import json


SANCTUM_CAPACITY = 2
DEFAULT_RELIC = 1
WITHDRAW_AMOUNT = 20


def new_game():
    return {
        "relics": {DEFAULT_RELIC},
        "sanctum": [],
        "slots": 0,
        "capacity": 0,
        "nodes": {},
        "edges": {},
        "queue": [],
        "count": 0,
        "balance": 0,
        "locked": False,
        "accounts": {},
        "events": {},
        "used": 0,
        "cap": 0,
    }


def cmd_a(state, relic_id=DEFAULT_RELIC):
    # 圣器已登记时拒绝重复供奉；重放同一条命令不会重复计数。
    relics = state["relics"]
    if relic_id in relics:
        return False
    relics.add(relic_id)
    return True


def cmd_b(state, node=1):
    # 先构造完整的新状态再提交，节点与关联边一并清除，避免删除中途失败留下残边。
    if node not in state["nodes"]:
        return False
    nodes = {n: value for n, value in state["nodes"].items() if n != node}
    edges = {
        edge: weight
        for edge, weight in state["edges"].items()
        if node not in edge
    }
    state["nodes"] = nodes
    state["edges"] = edges
    return True


def cmd_c(state):
    sanctum = state["sanctum"]
    if not sanctum:
        return None
    return sanctum[0]


def cmd_d(state):
    # 查看只取队首而不出队，重复查看（重放）得到同样结果且不改变队列。
    queue = state["queue"]
    if not queue:
        return None
    return queue[0]


def cmd_e(state):
    state["count"] = 0
    return True


def cmd_f(state, amount=WITHDRAW_AMOUNT):
    # 余额不足或圣所锁定时拒绝取出，先校验后扣款，失败时状态原样回滚。
    if state.get("locked", False) or state["balance"] < amount:
        return False
    state["balance"] -= amount
    return True


def cmd_g(state, account="missing"):
    # 首次到达视为新登记账户，余额按 0 落账而不是返回 -1。
    accounts = state["accounts"]
    if account not in accounts:
        accounts[account] = 0
    return accounts[account]


def cmd_h(state):
    if state["slots"] >= state["capacity"]:
        return False
    state["slots"] += 1
    return True


def cmd_i(state, event_id=1):
    # 撤销事件是幂等操作，重放不会抛出异常或累计副作用。
    state["events"].pop(event_id, None)
    return True


def cmd_j(state):
    return state["cap"] - state["used"]


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
