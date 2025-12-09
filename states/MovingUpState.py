# states/moving_up_state.py
from states.ElevatorState import ElevatorState

class MovingUpState(ElevatorState):
    def request_up(self, elevator):
        print("[MovingUp] قبلاً در حال بالا رفتن هستیم.")

    def request_down(self, elevator):
        print("[MovingUp] فعلاً جهت را عوض نمی‌کنیم.")

    def step(self, elevator):
        if elevator.current_floor < elevator.max_floor:
            elevator.current_floor += 1
            print(f"[MovingUp] طبقه {elevator.current_floor}")
            if elevator.current_floor == elevator.max_floor:
                print("[MovingUp] رسیدیم به آخر، رفتن به Idle.")
                elevator.set_state(elevator.idle_state)
        else:
            elevator.set_state(elevator.idle_state)
