import rtmidi
import time
from algo import snotes_to_notes, snotes_to_notes_2

class Interface:

    def __init__(self, possible_names):
        self.midiout = rtmidi.MidiOut()
        self.number = None
        print(self.midiout.get_ports())
        for i, name in enumerate(self.midiout.get_ports()):
            print('name: ', name)
            if name in possible_names:
                self.number = i
                break
        if self.number is None:
            raise Exception("can't find any port named" + str(possible_names))
        self.midiout.open_port(self.number)

    def play_raw(self, raws_in):
        raws = sorted(raws_in, key=lambda r: r.time)
        curr_time = 0.0
        for r in raws:
            t = r.time
            if t > curr_time:
                time.sleep(t-curr_time)
                curr_time = t
            self.midiout.send_message(r.to_message())

    def play_snotes(self, notes_in):
        notes_in = snotes_to_notes(notes_in)
        accum = []
        for n in notes_in:
            events = n.to_raws()
            accum += events
        self.play_raw(accum)

    def play_notes(self, notes_in):
        accum = []
        for n in notes_in:
            events = n.to_raws()
            if events is not None:
                accum += events
        for i in range(0, len(accum)):
            print(accum[i].time)
        self.play_raw(accum)