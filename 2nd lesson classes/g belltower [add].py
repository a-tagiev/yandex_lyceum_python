class LittleBell:
    def sound(self):
        print("ding")


class BigBell:
    def __init__(self):
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


bell_tower = BellTower(BigBell(), LittleBell())
bell_tower.sound()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.sound()
