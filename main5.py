from Interface import Interface
from algo import expandSnotes, interpolate, addDistribution, snotes_to_notes, snotes_to_notes_tritones
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(2, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def scale2(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[12,4,8,12]
    shift_0=[0,3,1,6]
    spans_0=[1,0.33333,.25,1.5]
    direction_0=[48,73]
    modulus_1=[6,8]
    shift_1=[0,0]
    spans_1=[0.75,0.33333]
    direction_1=[73,48]
    order = [0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0]
    interface = Interface(['MidiPipe Input 1'])
    notes_0 = scale2(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale2(modulus_1, shift_1, spans_1, direction_1)
    notes_2 = interpolate([notes_0, notes_1], order)

    direction_0 = [32, 74]
    direction_1 = [32, 74]

    notes_3 = expandSnotes(notes_2, notes_2, -39, 39)
    # notes_2 = expandSnotes(notes_2, notes_2)

    # notes_3 = interpolate([snotes_to_notes(scale2(modulus_0, shift_0, spans_0, direction_0)), snotes_to_notes(scale2(modulus_1, shift_1, spans_1, direction_1))], order2)



    # interface.play_notes(notes_0 + notes_1)
    interface.play_snotes(notes_3)
    # interface.play_notes(notes_3)

main()