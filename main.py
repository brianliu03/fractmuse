import math
from Interface import Interface
from Note import Note
from Motif import Motif
from algo import expand, snotes_to_notes, snotes_to_notes_2, snotes_to_notes_sieve
from Comp import Notes_1

def full_composition_01(modulus, shift):
    output = [] 
    # comp_6 = Comp_8(3, 'chromatic', 1001)
    # output += comp_6.run()
    # comp_8 = Comp_8(3, 'melodic', 1001)
    # outprut += comp_8.run()
    comp = Notes_1(1, sieve=(modulus, shift))
    # set up distribution to discriminate based on related notes e.g. major in the middle range chromatic on the outside
    # throw the note away or create a boundary if the notes are too high or low
    # weighing rhythms too
    # behavoirs morphing into other behavior
    # table that starts as arbitrary (e.g. poisson) distribution, then manipulate it by rotating for example
        # table of 12 tones starts with poisson distribution, then shift it up a tone
    # make notes in constraints of two hands
    
    output += comp.run()
    
    return output

def main():
    modulus = 3
    shift = 2
    interface = Interface(['MidiPipe Input 1'])
    notes = snotes_to_notes_sieve(full_composition_01(modulus, shift), modulus)
    interface.play_notes(notes)

main()