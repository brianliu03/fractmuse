from Midi_Interface import MidiInterface
from algo import expandSnotes,expandSnotesNoSpan, interpolate, addDistribution, snotesToNotes, snotesToNotesTritones
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
    shift_0=[4,1]
    spans_0=[.333,0]
    direction_0=[52,62]
    modulus_1=[6,3]
    shift_1=[3,0]
    spans_1=[.75,.25]
    direction_1=[52,62]
    order = [1,0,0,1,1]
    interface = MidiInterface(['MidiPipe Input 1'])
    notes_0 = scale2(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale2(modulus_1, shift_1, spans_1, direction_1)
    notes_2 = interpolate([notes_0, notes_1], order)

    notes_2 = expandSnotesNoSpan(notes_2, notes_2, -100, 100)
    # notes_2 = expandSnotesNoSpan(notes_2, notes_2)

    # notes_3 = interpolate([snotes_to_notes(scale2(modulus_0, shift_0, spans_0, direction_0)), snotes_to_notes(scale2(modulus_1, shift_1, spans_1, direction_1))], order2)



    # interface.play_notes(notes_0 + notes_1)
    interface.playSnotes(notes_2)
    # interface.play_notes(notes_3)

main()