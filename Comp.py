from cmath import exp
from algo import expand, expand_rand, randPoisDistribution
from Motif import Motif
from Note import Note
import random

class Notes_1:
    def __init__(self, num_expansions, sieve, spans, ascending):
        self.modulus, self.shift = sieve
        self.ascending = ascending
        self.motif = Motif([], [], [])
        if not ascending:
            self.modulus.reverse()
            self.shift.reverse()
            for i in range(87,-1,-1):
                self.motif.add(i, spans[i % len(spans)], 60)
        else:
            for i in range(0,88):
                self.motif.add(i, spans[i % len(spans)], 60)
        self.num_expansions = num_expansions
        self.rand = random.Random(101)
    
    def run(self):
        my_list = []
        my_list.append(Note(None, 0.5, 0, 0, span=0.5, root=21, sieve=(self.modulus, self.shift)))
        for i in range(self.num_expansions):
            # my_list = expand_rand(my_list, self.motif, expPitch=True, expSpan=True, expVel=False, rand=self.rand)
            my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=False)
        return my_list