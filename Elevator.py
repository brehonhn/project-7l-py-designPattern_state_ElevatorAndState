
# Elevator.py
from states.IdleState import IdleState
from states.MovingUpState import MovingUpState
from states.MovingDownState import MovingDownState

class Elevator:
    def __init__(self, min_floor=0, max_floor=5):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = 0

        # همه stateها اینجا ساخته می‌شن
        self.idle_state = IdleState()
        self.moving_up_state = MovingUpState()
        self.moving_down_state = MovingDownState()

        self.state = self.idle_state

    def set_state(self, new_state):
        print(f"[Elevator] تغییر حالت از {self.state} به {new_state}")
        self.state = new_state

    def press_up(self):
        self.state.request_up(self)

    def press_down(self):
        self.state.request_down(self)

    def step(self):
        self.state.step(self)
