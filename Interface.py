import rtmidi
import time
from algo import snotes_to_notes, snotes_to_notes_tritones
from midiutil import MIDIFile

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
    
    def play_raw_control_change(self, raws_in):
        curr_time = 0.0
        for r in raws_in:
            t = r.time + curr_time
            time.sleep(t-curr_time)
            curr_time += t
            self.midiout.send_message(r)

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
        self.play_raw(accum)

    def create_file(self, notes_in):
        midi = MIDIFile(1)
        track = 0
        channel = 0
        midi.addTempo(track, 0, 60)

        for n in notes_in:
            midi.addNote(track, channel, n.pitch + 21, n.time, n.dur, n.vel)
        
        with open("comp.mid", "wb") as output_file:
            midi.writeFile(output_file)
