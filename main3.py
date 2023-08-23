from Interface import Interface
from algo import interpolate, addDistribution, snotesToNotes
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[12,12,12,12,12,12,12]
    shift_0=[0,1,4,5,7,10,11]
    spans_0=[0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    direction_0=[30,60]
    # randomize order
    interface = Interface(['MidiPipe Input 1'])

    notes = snotesToNotes(scale(modulus_0, shift_0, spans_0, direction_0))

    interface.play_notes(notes)

main()

# how much information is being delivered at a particular time