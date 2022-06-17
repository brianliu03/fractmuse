import time
from mido import MidiFile
from Interface import Interface
from Motif import Motif
from Note import Note
from algo import expand, snotes_to_notes, snotes_to_notes_mfile

def main():
    mid = MidiFile('/Users/brianliu03/Documents/midi_files/sonata_58_1_(c)finley.mid', clip=True)
    interface = Interface(['MidiPipe Input 1'])
    motif = Motif([], [], [])
    leftover = []
    time_ = 0
    for msg in mid:
        time_ += msg.time
        if msg.type == "note_on" or msg.type == "note_off":
            motif.add(msg.note, time_, msg.velocity)
            # print(time_)
            # time.sleep(2)

    my_list = []
    my_list.append(Note(None, 1.0, 0, 0, span=1, root=0))
    my_list = expand(my_list, motif, expPitch=True, expSpan=True, expVel=False)
    my_list = snotes_to_notes_mfile(my_list)
    interface.play_notes(my_list)


main()