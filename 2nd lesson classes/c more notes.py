class Note:
    def __init__(self, height, is_long=False):
        self.height = height
        self.is_long = is_long
        if is_long:
            if self.height == "до":
                self.height = "до-о"
            if self.height == "ре":
                self.height = "ре-э"
            if self.height == "ми":
                self.height = "ми-и"
            if self.height == "фа":
                self.height = "фа-а"
            if self.height == "соль":
                self.height = "со-оль"
            if self.height == "ля":
                self.height = "ля-а"
            if self.height == "си":
                self.height = "си-и"

    def __str__(self):
        return self.height


class LoudNote(Note):
    def __init__(self, height, is_long=False):
        super().__init__(height, is_long)

    def __str__(self):
        return self.height.upper()


class DefaultNote(Note):
    def __init__(self, height="до", is_long=False):
        super().__init__(height, is_long)

    def __str__(self):
        return self.height


class NoteWithOctave(Note):
    def __init__(self, height, octave, is_long=False):
        super().__init__(height, is_long)
        self.octave = octave

    def __str__(self):
        return f"{self.height} ({self.octave})"


PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
