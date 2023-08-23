from Interface import Interface
from algo import expand, interpolate, addDistribution, snotesToNotes
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(2, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[12,12,12,12,12,12,12]
    shift_0=[0,2,4,5,7,9,11]
    spans_0=[0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    direction_0=[40,60]
    modulus_1=[12,12,12,12,12,12,12]
    shift_1=[0,2,4,5,7,9,11]
    spans_1=[0.25,0.75,0.25,0.75,0.25,0.75,0.25]
    direction_1=[40,60]
    # randomize order
    interface = Interface(['MidiPipe Input 1'])

    notes = interpolate([scale(modulus_0, shift_0, spans_0, direction_0),scale(modulus_1, shift_1, spans_1, direction_1)],order)
    notes = snotesToNotes(notes)

    interface.play_notes(notes)

main()