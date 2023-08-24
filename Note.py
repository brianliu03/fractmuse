# Defines a Note with span and time
class Note:

    def __init__(self, time, dur, pitch, vel, chan=1, span=None, root=21):
        self.time = time
        self.dur = dur
        self.pitch = pitch
        self.vel = vel
        self.span = span
        self.chan = chan
        self.root = root

    def to_raws(self):
        if self.pitch is not None:
            temp = self.root + self.pitch
            if temp is not None:
                return [
                    Raw(self.time, True, self.chan, temp, self.vel),
                    Raw(self.time + self.dur, False, self.chan, temp, self.vel)
                    ]

        return []

class Raw:
    def __init__(self, time, onOff, chan, pitch, vel):
        self.time = time
        self.onOff = onOff
        self.chan = chan
        self.pitch = pitch
        self.vel = vel
    def to_message(self):
        c = 0x90 if self.onOff else 0x80
        return [c + self.chan - 1, self.pitch, self.vel]