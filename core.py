"""玻璃厂核心逻辑：玻璃液、窑炉、拉制和退火。"""

import json


def new_game():
    return {"batches": {}, "kiln_load": 0, "kiln_capacity": 2, "material": 100, "rate": 100, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def load_kiln(state, batch_id):
    state["batches"][batch_id] = True
    state["kiln_load"] += 1
    return True


def check_temp(state, temp):
    if temp < 30:
        return "over"
    return "ok"


def cancel(state, batch_id):
    return True


def draw(state, amount):
    state["material"] -= amount
    return True


def crack(state):
    state["rate"] -= 10
    state["rate"] -= 10
    return state["rate"]


def anneal(state, batch_id):
    return True


def main():
    print("玻璃厂 - 命令: load/temp/cancel/draw/crack/anneal/quit")
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
