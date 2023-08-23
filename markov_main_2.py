import time
from mido import MidiFile
from Midi_Interface import MidiInterface
from Motif import Motif
from Note import Note
from algo import expand, snotesToNotes
from Markov_Algo import MarkovGenerator

def main():
    mid = MidiFile('/Users/brianliu03/Documents/Projects/FractMuse-01/midi_files/mozart_sonata_9_1stmvt_k311_PNO.mid', clip=True)
    interface = MidiInterface(['MidiPipe Input 1'])

    motif = Motif([], [], [])

    notes = []
    times = []
    tim = 0
    for msg in mid:
        tim += msg.time
        if msg.type == "note_on":
            notes.append(msg)
            times.append(tim)
    offset = times[0]
    times[:] = [time - offset for time in times]

    delta = times[len(times) - 1] - times[0]
    i = 0
    for msg in notes:
        if i == len(notes) - 1:
            span = 0
        else:
            span = delta - times[i] - (delta - times[i + 1])
        motif.add(msg.note, span, msg.velocity)
        i += 1


    gen = MarkovGenerator(len(motif.spans), 141, 1, 0)
    gen.generateTableSpans(motif.spans)
    spans = [1]*(4700000)
    vels = [70]*(4670000)
    comp_1 = Motif(motif.pitches, gen.createComp(int(round(motif.spans[0], 2)) * 100), vels)
    my_list = []
    for i in range(len(comp_1.spans)):
        comp_1.spans[i] = comp_1.spans[i] / 100

    my_list.append(Note(None, 1.0, 0, 0, span=1, root=0))
    my_list = expand(my_list, comp_1, expPitch=True, expSpan=True, expVel=False)
    my_list = snotesToNotes(my_list)

    interface.playNotes(my_list)

main()