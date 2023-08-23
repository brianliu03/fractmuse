
# express the idea of the following choices:
# major scale? if so , root? ('major', <root>)
# melodic minor? if so, root? ('melodic minor', <root>)
# chromatic? ('chromatic', None)

class NoteScale:

    def __init__(self, time, dur, pitch, vel, chan=1, span=None, scale=('chromatic', 60)):
        self.time = time
        self.dur = dur
        self.pitch = pitch
        self.vel = vel
        self.span = span
        self.chan = chan
        self.scale = scale

    def to_raws(self):
        if self.pitch is not None:
            scale_type, param = self.scale
            if scale_type == 'chromatic':
                temp = self.pitch + param
            elif scale_type == 'major':
                temp = self.major_scale(self.pitch, param)
            elif scale_type == 'melodic':
                temp = self.melodic_minor_scale(self.pitch, param)

            return [
                Raw(self.time, True, self.chan, temp, self.vel),
                Raw(self.time + self.dur, False, self.chan, temp, self.vel)
                ]

        return []
    
    def major_scale(self, degree, root_note):
        major_to_midi = [0, 2, 4, 5, 7, 9, 11]
        return (major_to_midi[degree % 7]) + root_note + (degree // 7) * 12

    def melodic_minor_scale(self, degree, root_note):
        melodic_to_midi = [0, 2, 3, 5, 7, 9, 11]
        return (melodic_to_midi[degree % 7]) + root_note + (degree // 7) * 12

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