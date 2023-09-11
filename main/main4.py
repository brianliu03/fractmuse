import time
from Midi_Interface import MidiInterface
from algorithms.algo import interpolate, addDistribution, snotesToNotes, snotesToNotesTritones
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def scale2(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(2, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[4,14]
    shift_0=[0,0]
    spans_0=[0.5,1.25]
    direction_0=[40,70]
    modulus_1=[6,9]
    shift_1=[0,0]
    spans_1=[0.75,1.5]
    direction_1=[40,70]
    order = [0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0]
    order2 = [0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    interface = MidiInterface(['MidiPipe Input 1'])
    notes_0 = snotesToNotes(scale(modulus_0, shift_0, spans_0, direction_0))
    notes_1 = snotesToNotes(scale(modulus_1, shift_1, spans_1, direction_1))
    notes_2 = interpolate([notes_0, notes_1], order)
    direction_0 = [44, 74]
    direction_1 = [44, 74]
    notes_3 = interpolate([snotesToNotes(scale2(modulus_0, shift_0, spans_0, direction_0)), snotesToNotes(scale2(modulus_1, shift_1, spans_1, direction_1))], order2)


    interface.playNotes(notes_0)
    interface.playNotes(notes_1)
    interface.playNotes(notes_2)
    interface.playNotes(notes_3)

main()