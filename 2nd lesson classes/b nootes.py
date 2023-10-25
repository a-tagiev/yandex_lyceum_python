class Note:
    def __init__(self, height, long=False):
        self.height = height
        self.long = long

    def __str__(self):
        if not self.long:
            return self.height
        if self.height == "до":
            return "до-о"
        if self.height == "ре":
            return "ре-э"
        if self.height == "ми":
            return "ми-и"
        if self.height == "фа":
            return "фа-а"
        if self.height == "соль":
            return "со-оль"
        if self.height == "ля":
            return "ля-а"
        if self.height == "си":
            return "си-и"
