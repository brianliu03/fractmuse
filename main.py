from Interface import Interface
from algo import interpolate, addDistribution, snotes_to_notes
from Comp import Notes_1

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[12,12,12,12,12,12,12]
    shift_0=[0,2,4,5,7,9,11]
    spans_0=[0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    direction_0=[0,88]
    # modulus_1=[4,6,9]
    # shift_1=[0,0,0]
    # spans_1=[0.5,0.5,0.5]
    modulus_1=[12,12,12,12,12,12,12]
    shift_1=[0,2,4,5,7,9,11]
    spans_1=[0.25,0.75,0.25,0.75,0.25,0.75,0.25]
    direction_1=[0,88]
    # randomize order
    order = [0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0]
    interface = Interface(['MidiPipe Input 1'])
    # notes_1 = scale(modulus_1, shift_1, spans_1, direction_1)
    # sum = len(notes_0) + len(notes_1)
    # order = [0,0,1,1,0,1,0]
    # for i in range(sum):
    #     order.append(order[i])

    # print(order)
    # notes_0 = snotes_to_notes([notes_0, notes_1], [0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0])
    # notes_0 = snotes_to_notes(scale(modulus_0, shift_0, spans_0, direction_0))
    # notes_1 = snotes_to_notes(scale(modulus_1, shift_1, spans_1, direction_1))
    notes = snotes_to_notes_interpolate([scale(modulus_0, shift_0, spans_0, direction_0),scale(modulus_1, shift_1, spans_1, direction_1)],order)
    notes_2 = snotes_to_notes_interpolate([scale(modulus_0, shift_0, spans_0, direction_0),scale(modulus_1, shift_1, spans_1, direction_1)],order)
    # notes_2 = snotes_to_notes(scale(modulus_2, shift_2, spans_2, direction_2))
    # notes_3 = snotes_to_notes_sieve(scale(modulus_3, shift_3, ascending=True), modulus_3, shift_3, ascending=True


    interface.play_notes(notes)

main()