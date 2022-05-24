from encodings import normalize_encoding
import math
from Interface import Interface
from Note import Note
from Motif import Motif
from algo import snotes_to_notes_sieve
from Comp import Notes_1

def scale(modulus, shift):
    output = []
    comp_1 = Notes_1(1, sieve=(modulus, shift))
    # set up distribution to discriminate based on related notes e.g. major in the middle range chromatic on the outside
    # throw the note away or create a boundary if the notes are too high or low
    # weighing rhythms too
    # behavoirs morphing into other behavior
    # table that starts as arbitrary (e.g. poisson) distribution, then manipulate it by rotating for example
        # table of 12 tones starts with poisson distribution, then shift it up a tone
    # make notes in constraints of two hands
    
    output += comp_1.run()
    
    return output

def main():
    modulus=[12,12,12,12,12,12,12]
    shift=[0,2,4,5,7,9,11]
    # modulus=[3]
    # shift=[1]
    interface = Interface(['MidiPipe Input 1'])
    notes_1 = snotes_to_notes_sieve(scale(modulus, shift), modulus, shift)
    print(len(notes_1))
    for i in range(0, len(notes_1)):
        print(notes_1[i].pitch)
    interface.play_notes(notes_1)

main()