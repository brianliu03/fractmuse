import time
from Interface import Interface
from algo import expandSnotes,expandSnotesNoSpan, interpolate, addDistribution, snotes_to_notes, snotes_to_notes_tritones
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
    modulus_0=[4,5]
    shift_0=[3,2]
    spans_0=[.5,1.0]
    direction_0=[40,60]

    modulus_1=[6,3]
    shift_1=[3,1]
    spans_1=[.75,.25]
    direction_1=[50,20]

    modulus_2=[5,7,10]
    shift_2=[2,3,5]
    spans_2=[.333,.3333,1.25]
    direction_2=[10,50]

    # order = [1,0,0,1,1]
    interface = Interface(['MidiPipe Input 1'])
    notes_0 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale2(modulus_1, shift_1, spans_1, direction_1)
    notes_2 = scale2(modulus_2, shift_2, spans_2, direction_2)
    # print(len(notes_1))
    # notes_2 = interpolate([notes_0, notes_1], order)

    notes_3 = expandSnotesNoSpan(notes_2, notes_0,-25,10)
    order = [1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1]
    notes_4 = interpolate([notes_3, notes_1], order)

    modulus_2=[5,7,10]
    shift_2=[2,3,5]
    spans_2=[.333,.3333,1.0]
    direction_2=[30,70]

    notes_5 = scale2(modulus_2, shift_2, spans_2, direction_2)

    notes_0 = snotes_to_notes_tritones(notes_0)
    interface.play_notes(notes_0)
    interface.play_snotes(notes_1)
    notes_5 = snotes_to_notes_tritones(notes_5)
    interface.play_notes(notes_5)
    time.sleep(0.25)
    interface.play_snotes(notes_4)
    notes_3 = snotes_to_notes(notes_3)
    interface.play_notes(notes_3 + notes_0)

main()