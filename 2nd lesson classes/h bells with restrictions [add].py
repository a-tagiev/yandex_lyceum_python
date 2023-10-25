class Bell:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print_info(self):
        ft = []
        na = sorted(self.kwargs.items(), key=lambda x: x[0])
        ns = ', '.join([f'{name}: {value}' for name, value in na])

        if ns:
            ft.append(ns)
        if self.args:
            ft.append(', '.join(self.args))
        print('; '.join(ft) if ft else '-')


class LittleBell(Bell):
    def sound(self):
        print("ding")


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ring = "ding"

    def sound(self):
        if self.ring == "ding":
            print(self.ring)
            self.ring = "dong"
            return 0
        else:
            print(self.ring)
            self.ring = "ding"


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")


Bell("бронзовый").print_info()
LittleBell("медный", нота="ля").print_info()
BigBell(название="Корноухий", вес="1275 пудов").print_info()
