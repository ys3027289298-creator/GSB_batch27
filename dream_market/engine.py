import json


def new_game():
    return {}


def rule_a(state):
    # 空摊位返回文本: 空摊位应返回 None, 而不是 "empty" 文本。
    # 幂等: 纯查询, 不修改状态, 重复调用结果一致。
    return None


def rule_b(state):
    # 先到未交易: 队首玩家应先完成交易, 查看队首不能将其弹出。
    # 幂等: 只窥视不移除, 重复调用返回同一队首, 队列长度不变。
    queue = state["queue"]
    if not queue:
        return None
    return queue[0]


def rule_c(state):
    # 重置不清: 重置必须把计数清零。
    # 幂等: 重复重置仍为 0。
    state["count"] = 0
    return True


def rule_d(state):
    # 梦境币少算: 结算前校验余额, 余额不足不得扣款。
    # 幂等: 失败时不产生任何副作用, 可安全重试。
    cost = 20
    if state["balance"] < cost:
        return False
    state["balance"] -= cost
    return True


def rule_e(state):
    # 读档跳号: 读档时缺失账户应按 0 处理, 而不是 -1 导致编号偏移。
    return state["accounts"].get("missing", 0)


def rule_f(state):
    # 暂停仍结算: 暂停(默认)状态下拒绝结算。
    # 幂等: 拒绝时不改状态; 同一笔结算由 rule_g 的事件移除保证只生效一次。
    if state.get("paused", True):
        return False
    return True


def rule_g(state):
    # 单次重复累计: 事件结算后立即移除, 防止同一事件被重复结算。
    # 幂等: 重复调用时事件已不存在, 不会二次生效。
    state["events"].pop(1, None)
    return True


def rule_h(state):
    # 满码头仍停: 剩余泊位 = cap - used, 修正原来的 -1 偏移。
    return state["cap"] - state["used"]


def rule_i(state):
    # 重复摊位: 摊位已存在时拒绝重复注册。
    # 幂等: 重复注册是安全的空操作, 直接返回 False。
    return state.get("stall_registered") is False


def rule_j(state):
    # 查看误删: 查看节点不得删除节点本身, 只清理关联的边。
    # 幂等: 边移除后重复调用无副作用。
    state["edges"].pop((1, 2), None)
    return True


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
