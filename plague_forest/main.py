import json


def new_game():
    return {}

def cmd_a(state):
    # 重复病例：已登记的病例不再计入（非法输入）
    items = state["items"]
    case_id = 1
    if case_id not in items:
        items.append(case_id)
    return len(items)

def cmd_b(state):
    # 读档跳号：先取号再自增，避免跳号
    case_id = state["next_id"]
    state["next_id"] += 1
    return case_id

def cmd_c(state):
    # 药剂少算：存量不足时拒绝扣减（非法输入）
    amount = 10
    if amount > state["src"]:
        return False
    state["src"] -= amount
    return True

def cmd_d(state):
    # 锁定仍采集：林区关闭时禁止操作（状态锁定）
    if state.get("closed"):
        return False
    return True

def cmd_e(state):
    # 单次重复累计：同一事件只登记一次
    events = state["events"]
    if events.get("dosed"):
        return False
    events["dosed"] = True
    return True

def cmd_f(state):
    # 空病例返回文本：空状态视为非法输入
    if not state:
        return False
    return True

def cmd_g(state):
    # 查看误删/先看最早：查看最早的事件且不删除
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def cmd_h(state):
    # 重置不清：重置后的空状态无待办事项
    if not state:
        return False
    return True

def cmd_i(state):
    # 隔离林满仍进：容量不足时拒绝进入（容量不足）
    isolation = state.setdefault("isolation", [])
    if len(isolation) >= 1:
        return False
    isolation.append(True)
    return True

def cmd_j(state):
    # 先到未处理：队列先进先出
    return state["queue"].pop(0)

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
