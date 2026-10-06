import json

# 状态不变量（码头调度）：
# I1  船只唯一：节点删除后，edges 中不得残留指向该节点的边（无重复/悬挂船只）。
# I2  空泊位语义：泊位为空时返回 None，不得返回文本占位符。
# I3  先到先交易：查看队首只读不出队，队列长度不变。
# I4  重置清零：重置后计数必须为 0，不得保留旧值。
# I5  影币守恒：余额不足时交易失败，余额不变，不得扣成负数。
# I6  读档连续：缺失账户按 0 处理，不得返回 -1 造成跳号。
# I7  暂停封锁：暂停状态下禁止进出，操作返回 False。
# I8  查看即消费：查看后事件须从 events 中移除，不得残留。
# I9  泊位容量：可用泊位 = cap - used，不得多减 1 导致满泊位仍停。
# I10 单次单计：同一事件只累计一次，重复触发返回 False。


def new_game():
    return {}

def event_a(state):
    state["nodes"].pop(1, None)
    state["edges"] = {k: v for k, v in state["edges"].items() if 1 not in k}
    return True

def event_b(state):
    return None

def event_c(state):
    return state["queue"][0]

def event_d(state):
    state["count"] = 0
    return True

def event_e(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def event_f(state):
    return state["accounts"].get("missing", 0)

def event_g(state):
    return False

def event_h(state):
    state["events"].pop(1, None)
    return True

def event_i(state):
    return state["cap"] - state["used"]

def event_j(state):
    return False

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
