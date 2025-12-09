
---

# 📘 **README.md — Elevator Control System (State Design Pattern)**

```markdown
# 🚟 Elevator Control System using State Design Pattern

این پروژه یک **سیستم کنترل آسانسور** را با استفاده از **الگوی طراحی State** پیاده‌سازی می‌کند.  
در این سیستم، آسانسور بسته به وضعیت فعلی خود (Idle, MovingUp, MovingDown) رفتار متفاوتی دارد.  
هدف اصلی این الگو **حذف شرط‌های تودرتو** و **انتقال رفتار حالت‌ها به کلاس‌های مستقل** است.

---

## 🎯 هدف پروژه

در طراحی سیستم‌های کنترلی مانند آسانسور، رفتار سیستم کاملاً وابسته به **وضعیت داخلی** آن است.  
مثلاً:

- اگر آسانسور در حالت *Idle* باشد:
  - با درخواست UP حرکت می‌کند
- اگر در حالت *MovingUp* باشد:
  - هر «تیک زمانی» یک طبقه بالا می‌رود
- اگر به طبقه آخر برسد:
  - باید خودکار حالت را تغییر دهد
- اگر در حالت *MovingDown* باشد:
  - نمی‌تواند ناگهانی جهت را عوض کند

الگوی طراحی **State** سبب می‌شود که:

- رفتار مربوط به هر حالت در کلاس مخصوص خود قرار گیرد  
- کلاس اصلی آسانسور تمیز، کوتاه و قابل‌توسعه بماند  
- بدون تغییر کد فعلی بتوان حالت‌های جدیدی اضافه کرد

---

## 🧩 ساختار پروژه

```

project/
│
├── states/
│   ├── ElevatorState.py       # رابط مشترک تمام حالت‌ها
│   ├── IdleState.py           # حالت توقف
│   ├── MovingUpState.py       # حالت حرکت به بالا
│   └── MovingDownState.py     # حالت حرکت به پایین
│
├── Elevator.py                # کلاس اصلی Context
├── main.py                    # اجرای نمونه
└── README.md

````

---

## 🧠 الگوی State چیست؟

الگوی **State** برای زمانی استفاده می‌شود که یک شیء در حالت‌های مختلف، رفتارهای متفاوتی داشته باشد.  

با این الگو:

- به جای if/else های بزرگ  
- یک **interface** برای حالت‌ها تعریف می‌کنیم  
- و برای هر حالت یک **کلاس مستقل** می‌سازیم

در نتیجه:

✔ کد تمیزتر  
✔ قابل‌توسعه‌تر  
✔ منطق وضعیت از هم جدا می‌شود  
✔ اصل *Single Responsibility* رعایت می‌شود  

---

## 🧱 پیاده‌سازی

### 1) Interface حالت‌ها

```python
from abc import ABC, abstractmethod

class ElevatorState(ABC):

    @abstractmethod
    def request_up(self, elevator):
        pass

    @abstractmethod
    def request_down(self, elevator):
        pass

    @abstractmethod
    def step(self, elevator):
        pass
````

---

### 2) کلاس اصلی Elevator (Context)

```python
class Elevator:
    def __init__(self, min_floor=0, max_floor=10):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = 0
        self.state = IdleState()   # حالت اولیه

    def set_state(self, new_state):
        print(f"[Elevator] تغییر حالت از {self.state} به {new_state}")
        self.state = new_state

    def press_up(self):
        self.state.request_up(self)

    def press_down(self):
        self.state.request_down(self)

    def step(self):
        self.state.step(self)
```

---

### 3) حالت Idle

```python
class IdleState(ElevatorState):
    def request_up(self, elevator):
        if elevator.current_floor >= elevator.max_floor:
            print("❗ در بالاترین طبقه هستیم.")
            return
        elevator.set_state(MovingUpState())

    def request_down(self, elevator):
        if elevator.current_floor <= elevator.min_floor:
            print("❗ در پایین‌ترین طبقه هستیم.")
            return
        elevator.set_state(MovingDownState())

    def step(self, elevator):
        print(f"[Idle] آسانسور در طبقه {elevator.current_floor} منتظر است.")
```

---

### 4) حالت حرکت به بالا

```python
class MovingUpState(ElevatorState):
    def request_up(self, elevator):
        print("[MovingUp] قبلاً در حال بالا رفتن هستیم.")

    def request_down(self, elevator):
        print("[MovingUp] امکان تغییر ناگهانی جهت نیست.")

    def step(self, elevator):
        if elevator.current_floor < elevator.max_floor:
            elevator.current_floor += 1
            print(f"[MovingUp] طبقه {elevator.current_floor}")
            if elevator.current_floor == elevator.max_floor:
                elevator.set_state(IdleState())
```

---

### 5) حالت حرکت به پایین

```python
class MovingDownState(ElevatorState):
    def request_up(self, elevator):
        print("[MovingDown] امکان تغییر ناگهانی جهت نیست.")

    def request_down(self, elevator):
        print("[MovingDown] قبلاً در حال پایین رفتن هستیم.")

    def step(self, elevator):
        if elevator.current_floor > elevator.min_floor:
            elevator.current_floor -= 1
            print(f"[MovingDown] طبقه {elevator.current_floor}")
            if elevator.current_floor == elevator.min_floor:
                elevator.set_state(IdleState())
```

---

## ▶️ اجرای مثال

```python
from Elevator import Elevator

e = Elevator(min_floor=0, max_floor=5)

e.step()
e.press_up()
for _ in range(6): e.step()
e.press_down()
for _ in range(6): e.step()
```

---

## 🟩 خروجی نمونه

```
[Idle] آسانسور در طبقه 0 منتظر است.
درخواست حرکت به بالا...
[Elevator] تغییر حالت از IdleState به MovingUpState
[MovingUp] طبقه 1
[MovingUp] طبقه 2
[MovingUp] طبقه 3
[MovingUp] طبقه 4
[MovingUp] طبقه 5
[Elevator] تغییر حالت از MovingUpState به IdleState
[Idle] آسانسور در طبقه 5 منتظر است.
...
```

---

## 🔍 چرا الگوی State؟

* رفتار آسانسور وابسته به وضعیت آن است
* کلاس آسانسور نباید پر از شرط باشد
* می‌توان حالت‌های جدید اضافه کرد بدون تغییر کد آسانسور
* منطق حالات از هم کاملاً جداست
* سیستم قابل‌تست‌تر و مقیاس‌پذیرتر می‌شود

---

## 🚀 توسعه‌های آینده

* اضافه کردن حالت `DoorOpen`
* اضافه کردن حالت `Overloaded` (اضافه‌بار)
* نگه‌داری صف درخواست‌ها (Queue System)
* ترکیب State + Observer برای اطلاع‌رسانی تغییر طبقه به UI

---

## 📜 لایسنس

MIT License © 2025


