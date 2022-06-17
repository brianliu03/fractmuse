from encodings import normalize_encoding
import math
from Interface import Interface
from Note import Note
from Motif import Motif
from algo import snotes_to_notes_sieve, snotes_to_notes_sieve_distribution, snotes_to_notes_sieve_split, snotes_to_notes, snotes_to_notes_interpolate
from Comp import Notes_1
import random
import queue

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(2, sieve=(modulus, shift), spans=spans, direction=direction)
    # table that starts as arbitrary (e.g. poisson) distribution, then manipulate it by rotating for example
        # table of 12 tones starts with poisson distribution, then shift it up a tone
    # make notes in constraints of two hands
    # L - systems
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[12,12,12,12]
    shift_0=[3,10,0,2]
    spans_0=[0.75,0,0.5,.25]
    direction_0=[27,38]
    modulus_1=[12,12,12]
    shift_1=[5,8,1]
    spans_1=[1.5,1.25,.5]
    direction_1=[27,38]
    interface = Interface(['MidiPipe Input 1'])
    notes_0 = scale(modulus_0, shift_0, spans_0, direction_0)
    notes_1 = scale(modulus_1, shift_1, spans_1, direction_1)
    sum = len(notes_0) + len(notes_1)
    order = [0,0,1,1,0,1,0]
    for i in range(sum):
        order.append(order[i])

    # print(order)
    notes_0 = snotes_to_notes_interpolate([notes_0, notes_1], [0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0])
    # notes_1 = snotes_to_notes(scale(modulus_1, shift_1, spans_1, direction_1))
    # notes_2 = snotes_to_notes(scale(modulus_2, shift_2, spans_2, direction_2))
    # notes_3 = snotes_to_notes_sieve(scale(modulus_3, shift_3, ascending=True), modulus_3, shift_3, ascending=True)


    interface.play_notes(notes_0)

main()