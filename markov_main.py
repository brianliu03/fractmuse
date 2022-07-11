import time
from mido import MidiFile
import scipy as sp
from Interface import Interface
from Motif import Motif
from Note import Note
from algo import expand, snotes_to_notes
from Markov_Algo import MarkovGenerator

def main():
    mid = MidiFile('/Users/brianliu03/Documents/midi_files/mozart_sonata_9_1stmvt_k311_PNO.mid', clip=True)
    interface = Interface(['MidiPipe Input 1'])
    # motif = Motif([], [], [])
    rh = Motif([], [], [])
    lh = Motif([], [], [])
    time_ = 0
    for msg in mid:
        time_ += msg.time
        if msg.type == "note_on":
                if msg.note < 60:
                    lh.add(msg.note, time_, msg.velocity)
                else:
                    rh.add(msg.note, time_, msg.velocity)

    
    genRH = MarkovGenerator(len(rh.pitches), 88, 1, 21)
    genLH = MarkovGenerator(len(lh.pitches), 88, 1, 21)

    genRH.generateTable(rh.pitches)
    genLH.generateTable(lh.pitches)

    spansRH = [1]*(4700000) # len(motif.pitches) + 1
    velsRH = [70]*(4670000)
    spansLH = [1]*(4700000) # len(motif.pitches) + 1
    velsLH = [70]*(4670000)

    comp_1RH = Motif(genRH.createComp(62), spansRH, velsRH)
    comp_1LH = Motif(genLH.createComp(38), spansLH, velsLH)

    my_listRH = []
    my_listRH.append(Note(None, 0.5, 0, 0, span=0.25, root=0))
    my_listRH = expand(my_listRH, comp_1RH, expPitch=True, expSpan=True, expVel=False)
    my_listRH = snotes_to_notes(my_listRH)

    my_listLH = []
    my_listLH.append(Note(None, 0.5, 0, 0, span=0.25, root=0))
    my_listLH = expand(my_listLH, comp_1LH, expPitch=True, expSpan=True, expVel=False)
    my_listLH = snotes_to_notes(my_listLH)

    my_list = my_listRH + my_listLH

    interface.play_notes(my_list)


main()