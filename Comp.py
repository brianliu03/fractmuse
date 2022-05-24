from algo import expand, expand_rand, randPoisDistribution
from Motif import Motif
from Note import Note
import random

class Notes_1:
    def __init__(self, num_expansions, sieve):
        self.modulus, self.shift = sieve
        self.motif = Motif([], [], [])
        for i in range(0, 88):
            self.motif.add(i, 0.5, 60)
        self.num_expansions = num_expansions
    
    def run(self):
        my_list = []
        for i in range(0, len(self.modulus)):
            my_list.append(Note(None, 0.5, 0, 0, span=0.5, root=21, sieve=(self.modulus[i], self.shift[i])))
        print(my_list)
        my_list.sort(key=lambda x: x.pitch)
        print(my_list)
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        my_list.sort(key=lambda x: x.pitch)
        return my_list