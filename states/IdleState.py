# states/idle_state.py
from states.ElevatorState import ElevatorState

class IdleState(ElevatorState):
    def request_up(self, elevator):
        if elevator.current_floor >= elevator.max_floor:
            print("❗ در بالاترین طبقه هستیم.")
            return
        print("درخواست حرکت به بالا در حالت Idle.")
        elevator.set_state(elevator.moving_up_state)

    def request_down(self, elevator):
        if elevator.current_floor <= elevator.min_floor:
            print("❗ در پایین‌ترین طبقه هستیم.")
            return
        print("درخواست حرکت به پایین در حالت Idle.")
        elevator.set_state(elevator.moving_down_state)

    def step(self, elevator):
        print(f"[Idle] آسانسور در طبقه {elevator.current_floor} منتظر است.")
