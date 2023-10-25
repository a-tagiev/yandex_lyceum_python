class Note:
    def __init__(self, height, long=False):
        self.long = long
        self.height = height

    def __rshift__(self, steps):
        current_index = PITCHES.index(self.height)
        new_index = (current_index + steps) % N
        return Note(PITCHES[new_index], self.long)

    def __lshift__(self, steps):
        current_index = PITCHES.index(self.height)
        new_index = (current_index - steps) % N
        return Note(PITCHES[new_index], self.long)

    def get_interval(self, other_note):
        otn = other_note
        difference = abs(PITCHES.index(self.height) - PITCHES.index(otn.height))
        return INTERVALS[difference]

    def __le__(self, other):
        return PITCHES.index(self.height) <= PITCHES.index(other.height)

    def __ge__(self, other):
        return PITCHES.index(self.height) >= PITCHES.index(other.height)

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return PITCHES.index(self.height) < PITCHES.index(other.height)

    def __str__(self):
        if not self.long:
            return self.height
        else:
            long_pitch_index = PITCHES.index(self.height)
            return LONG_PITCHES[long_pitch_index]

    def __gt__(self, other):
        if not self.long:
            return PITCHES.index(self.height) > PITCHES.index(other.height)
        else:
            return PITCHES.index(self.height) > PITCHES.index(other.height)


N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
