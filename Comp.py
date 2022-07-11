from cmath import exp
from Markov_Algo import MarkovGenerator
from algo import expand, expand_rand, randPoisDistribution, expand2
from Motif import Motif
from Note import Note
from copy import copy
import random

class Notes_1:
    def __init__(self, num_expansions, sieve, spans, direction):
        self.modulus, self.shift = sieve
        self.motif = Motif([], [], [])
        start = direction[0]
        end = direction[1]
        if start > end:
            for i in range(start,end-1,-1):
                counter = 0
                while True:
                    modulo = self.modulus[counter]
                    base = self.shift[counter]
                    counter +=  1
                    if i % modulo == base:
                        self.motif.add(i, spans[counter - 1], 60)
                        i -= 1
                        break
                    if counter >= len(self.modulus):
                        i -= 1
                        break
        else:
            for i in range(start,end):
                counter = 0
                while True:
                    modulo = self.modulus[counter]
                    base = self.shift[counter]
                    counter +=  1
                    if i % modulo == base:
                        self.motif.add(i, spans[counter - 1], 60)
                        i += 1
                        break
                    if counter >= len(self.modulus):
                        i += 1
                        break
        self.num_expansions = num_expansions
        self.rand = random.Random(101)

    def markovify(self, order, start):
        pitches = self.motif.pitches
        gen = MarkovGenerator(len(pitches), 88, order, 0)
        gen.generateTable(pitches)
        self.motif.pitches = gen.createComp(start)

    
    def run(self):
        my_list = []
        my_list.append(Note(None, 0.25, 0, 0, span=0.5, root=21))
        for i in range(self.num_expansions):
            if i == 0:
                my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=False, offset=0)
            else:
                my_list = expand2(my_list, self.motif, expPitch=True, expSpan=True, expVel=False, offset=0)
        return my_list