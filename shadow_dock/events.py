import json


# 状态不变量（任何事件执行前后都必须成立）：
#   I1  船只唯一: queue 与 berths 中的船只 id 不重复。
#   I2  泊位不溢: 0 <= used <= cap。
#   I3  空泊位查询返回 None，不返回文本，且不修改状态。
#   I4  队列先到先服务: 查看/交易都从 queue[0] 取；查看不改状态。
#   I5  暂停时禁止进出港。
#   I6  查询类操作不删除任何数据。
#   I7  影币余额恒为非负，余额不足则交易整体失败、不扣款。
#   I8  一次性事件只计一次，处理后即从 events 移除。
#   I9  重置必须清零累计计数。
#   I10 边只能连接存在的节点；删除节点必须同时删除关联边。
#   I11 存档读档后 next_id 单调，不跳号、不复用。


def new_game():
    return {
        "nodes": {},
        "edges": {},
        "queue": [],
        "count": 0,
        "balance": 0,
        "accounts": {},
        "events": {},
        "used": 0,
        "cap": 0,
        "paused": False,
        "berths": {},
        "next_id": 1,
    }


def check_invariants(state):
    """校验状态不变量，违例时抛出 AssertionError。"""
    used = state.get("used", 0)
    cap = state.get("cap", 0)
    assert 0 <= used <= cap, "I2: 泊位占用越界"

    queue = state.get("queue", [])
    assert len(queue) == len(set(queue)), "I1: 等待队列存在重复船只"

    berths = state.get("berths", {})
    assert len(berths) == len(set(berths.values())), "I1: 泊位存在重复船只"
    assert not (set(queue) & set(berths.values())), "I1: 船只同时在队列与泊位中"

    assert state.get("balance", 0) >= 0, "I7: 影币余额为负"

    for a, b in state.get("edges", {}):
        assert a in state.get("nodes", {}) and b in state.get("nodes", {}), "I10: 悬挂边"
    return True


def event_a(state):
    """移除节点 1，并同步删除其所有关联边（I10）。"""
    state["nodes"].pop(1, None)
    state["edges"] = {
        edge: weight
        for edge, weight in state["edges"].items()
        if 1 not in edge
    }
    return True


def event_b(state):
    """空泊位查询：无船时返回 None（I3）。"""
    berth = state.get("berths", {})
    if not berth:
        return None
    return next(iter(berth.values()))


def event_c(state):
    """查看队首船只但不移除（I4/I6，先到先服务）。"""
    if not state["queue"]:
        return None
    return state["queue"][0]


def event_d(state):
    """重置累计计数为 0（I9）。"""
    state["count"] = 0
    return True


def event_e(state):
    """支付 20 影币：余额不足则失败且不扣款（I7）。"""
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True


def event_f(state):
    """查询账户余额，缺失账户按 0 计，不返回负数占位（I7）。"""
    return state["accounts"].get("missing", 0)


def event_g(state):
    """进港：暂停或泊位已满时拒绝（I2/I5）。"""
    if state.get("paused", False):
        return False
    if state["used"] >= state["cap"]:
        return False
    state["used"] += 1
    return True


def event_h(state):
    """处理一次性事件：处理后移除，避免重复累计（I8）。"""
    state["events"].pop(1, None)
    return True


def event_i(state):
    """返回剩余空泊位数（I2：cap - used，无差一错误）。"""
    return state["cap"] - state["used"]


def event_j(state):
    """出港：暂停或队列（泊位）为空时拒绝（I4/I5）。"""
    if state.get("paused", False):
        return False
    if state["used"] <= 0:
        return False
    state["used"] -= 1
    return True


def main():
    print("events 命令: run/quit")
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
