import time
from Interface import Interface
from algo import expandSnotes,expandSnotesNoSpan, interpolate, addDistribution, snotesToNotes, snotesToNotesWithOffset, snotesToNotesTritones
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def scale2(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    interface = Interface(['MidiPipe Input 1'])

    modulus_0=[5,6,10]
    shift_0=[2,2,8]
    spans_0=[.333,0.3333,0]
    direction_0=[80,26]

    modulus_1=[6,6,7]
    shift_1=[4,7,0]
    spans_1=[.75,0.75,0.25]
    direction_1=[30,70]

    notes_0 = scale2(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale2(modulus_1, shift_1, spans_1, direction_1)
    notes_0 = snotesToNotes(notes_0)
    notes_1 = snotesToNotes(notes_1)
    interface.play_notes(notes_0 + notes_1)
    
    time.sleep(0.6)

    direction_0=[50,60]
    direction_1=[60,50]
    notes_0 = scale2(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale2(modulus_1, shift_1, spans_1, direction_1)
    notes_0 = snotesToNotes(notes_0)
    notes_1 = snotesToNotes(notes_1)
    interface.play_notes(notes_0 + notes_1)

    direction_0 = [30,80]
    direction_1 = [70,30]
    notes_0 = scale2(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale2(modulus_1, shift_1, spans_1, direction_1)
    notes_0 = snotesToNotesTritones(notes_0)
    notes_1 = snotesToNotesTritones(notes_1)
    interface.play_notes(notes_1 + notes_0)

    direction_0=[0,88]
    direction_1=[88,0]
    notes_0 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale(modulus_1, shift_1, spans_1, direction_1)
    notes_2 = expandSnotesNoSpan(notes_0, notes_1, -20, 0)
    notes_2 = snotesToNotes(notes_2)

    direction_0=[0,50]
    notes_0 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_0 = snotesToNotes(notes_0)
    direction_1=[50,20]
    notes_1 = scale(modulus_1, shift_1, spans_1, direction_1)
    notes_1 = snotesToNotesWithOffset(notes_1, notes_0[len(notes_0) - 1].time + notes_0[len(notes_0) - 1].span)
    direction_1=[20,88]
    notes_1 = scale(modulus_1, shift_1, spans_1, direction_1)
    notes_1 = snotesToNotesWithOffset(notes_1, notes_0[len(notes_0) - 1].time + notes_0[len(notes_0) - 1].span)
    
    print(len(notes_2), len(notes_0), len(notes_1))
    notes_2 = notes_2[:30]
    interface.play_notes(notes_2 + notes_0 + notes_1)

    spans_0=[.75,0.5,1.2]
    direction_0 = [45,55]
    spans_1=[.75,0.75,0.2]
    direction_1 = [50,40]
    order = [0,1,1,0,1,0,0]
    notes_0 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale(modulus_1, shift_1, spans_1, direction_1)
    notes_2 = interpolate([notes_0, notes_1], order)
    notes_3 = expandSnotes(notes_2, notes_2, -60, 60)
    notes_3 = expandSnotesNoSpan(notes_3, notes_2, -60, 60)
    notes_3 = notes_3[300:342]
    notes_3 = snotesToNotes(notes_3)
    modulus_0 = [12,12,12]
    shift_0 = [3,7,10]
    spans_0 = [1,1,1]
    direction_0 = [3,28]
    notes_0 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_0 = snotesToNotes(notes_0)
    modulus_0 = [12,12,12]
    shift_0 = [7,7,7]
    spans_0 = [1,5,8]
    direction_0 = [57,30]
    notes_1 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = snotesToNotesWithOffset(notes_1, notes_0[len(notes_0) - 1].time + notes_0[len(notes_0) - 1].span)
    interface.play_notes(notes_3 + notes_0 + notes_1)
    

    

main()