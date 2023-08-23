from Midi_Interface import MidiInterface
from Note import Note
from Motif import Motif
from algo import expand, snotesToNotes, snotesToNotesTritones
from Comp import Comp_4, Comp_7

def full_composition_01():
    output = [] 
    # comp_6 = Comp_8(3, 'chromatic', 1001)
    # output += comp_6.run()
    # comp_8 = Comp_8(3, 'melodic', 1001)
    # output += comp_8.run()
    comp_8 = Comp_7(4, 'melodic', 1001)
    output += comp_8.run()
    
    return output

def main():
    interface = MidiInterface(['MidiPipe Input 1'])
    notes = snotesToNotesTritones(full_composition_01())
    interface.playNotes(notes)

main()