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


class Melody:
    def __init__(self, notes=None):
        self.notes = notes if notes is not None else []

    def __str__(self):
        if not self.notes:
            return ""
        return ', '.join(str(note) for note in self.notes).capitalize()

    def append(self, note):
        self.notes.append(note)

    def replace_last(self, note):
        if self.notes:
            self.notes[-1] = note

    def remove_last(self):
        if self.notes:
            self.notes.pop()

    def clear(self):
        self.notes = []

    def __len__(self):
        return len(self.notes)

    def transpose(self, interval):
        transposed_notes = []
        for note in self.notes:
            transposed_note = self.transpose_note(note, interval)
            if transposed_note is None:
                return Melody(list(self.notes))
            transposed_notes.append(transposed_note)
        return Melody(transposed_notes)

    def transpose_note(self, note, interval):
        pitch_index = PITCHES.index(note.height)
        new_pitch_index = pitch_index + interval
        if 0 <= new_pitch_index < N:
            return Note(PITCHES[new_pitch_index], note.long)
        return None

    def __rshift__(self, steps):
        transposed = self.transpose(steps)
        if len(transposed) == len(self):
            return transposed
        return self

    def __lshift__(self, steps):
        transposed = self.transpose(-steps)
        if len(transposed) == len(self):
            return transposed
        return self


N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
melody = Melody([Note('ля'), Note('соль'), Note('ми'), Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)
