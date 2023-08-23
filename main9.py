from Interface import Interface
from Note import Note
from Motif import Motif
from algo import expand, snotes_to_notes, snotes_to_notes_tritones
from Comp import Comp_4

def full_composition_01():
    output = [] 
    comp_6 = Comp_4(1, 'melodic', 1001)
    output += comp_6.run()
    return output

def main():
    interface = Interface(['MidiPipe Input 1'])
    notes = snotes_to_notes_tritones(full_composition_01())
    interface.play_notes(notes)

main()