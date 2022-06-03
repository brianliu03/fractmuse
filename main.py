from encodings import normalize_encoding
import math
from Interface import Interface
from Note import Note
from Motif import Motif
from algo import snotes_to_notes_sieve, snotes_to_notes_sieve_distribution, snotes_to_notes_sieve_split, snotes_to_notes
from Comp import Notes_1
import random

def scale(modulus, shift, spans, direction):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift), spans=spans, direction=direction)
    # behavoirs morphing into other behavior
    # table that starts as arbitrary (e.g. poisson) distribution, then manipulate it by rotating for example
        # table of 12 tones starts with poisson distribution, then shift it up a tone
    # make notes in constraints of two hands
    # L - systems
    # RHYTHMS
    # wed at 10am
    output += comp_1.run()
    
    return output

def main():
    modulus_0=[12,12,12,12]
    shift_0=[3,7,10,0]
    spans_0=[1,1,1,1]
    direction_0=[27,39]
    interface = Interface(['MidiPipe Input 1'])
    notes_0 = snotes_to_notes(scale(modulus_0, shift_0, spans_0, direction_0))
    # notes_1 = snotes_to_notes(scale(modulus_1, shift_1, spans_1, direction_1))
    # notes_2 = snotes_to_notes(scale(modulus_2, shift_2, spans_2, direction_2))
    # notes_3 = snotes_to_notes_sieve(scale(modulus_3, shift_3, ascending=True), modulus_3, shift_3, ascending=True)


    interface.play_notes(notes_0)

main()