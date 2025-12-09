from Elevator import Elevator

if __name__ == "__main__":
    elevator = Elevator(min_floor=0, max_floor=5)

    # در ابتدا: Idle در طبقه 0
    elevator.step()
    print("-" * 40)

    # درخواست برای بالا رفتن
    elevator.press_up()

    # چند گام حرکت
    for _ in range(6):
        elevator.step()
    print("-" * 40)

    # حالا در max_floor هستیم، اگر دوباره press_up بزنیم:
    elevator.press_up()
    elevator.step()
    print("-" * 40)

    # درخواست حرکت به پایین
    elevator.press_down()
    for _ in range(6):
        elevator.step()
