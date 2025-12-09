# states/moving_down_state.py
from states.ElevatorState import ElevatorState

class MovingDownState(ElevatorState):
    def request_up(self, elevator):
        print("[MovingDown] فعلاً جهت را عوض نمی‌کنیم.")

    def request_down(self, elevator):
        print("[MovingDown] قبلاً در حال پایین رفتن هستیم.")

    def step(self, elevator):
        if elevator.current_floor > elevator.min_floor:
            elevator.current_floor -= 1
            print(f"[MovingDown] طبقه {elevator.current_floor}")
            if elevator.current_floor == elevator.min_floor:
                print("[MovingDown] رسیدیم به پایین، رفتن به Idle.")
                elevator.set_state(elevator.idle_state)
        else:
            elevator.set_state(elevator.idle_state)
