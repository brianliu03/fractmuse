from Midi_Interface import MidiInterface
from algo import interpolate, addDistribution, snotesToNotes, snotesToNotesTritones
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(3, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[4,19]
    shift_0=[0,0]
    spans_0=[0.75,0.25]
    direction_0=[40,70]
    modulus_1=[14,9]
    shift_1=[0,0]
    spans_1=[0.2,0.5]
    direction_1=[40,70]
    order = [0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1]
    interface = MidiInterface(['MidiPipe Input 1'])

    notes = interpolate([scale(modulus_0, shift_0, spans_0, direction_0), scale(modulus_1, shift_1, spans_1, direction_1)], order)
    notes = snotesToNotes(notes)


    interface.playNotes(notes)

main()